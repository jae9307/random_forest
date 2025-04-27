import pandas as pd
import random
import math
import threading

# Defines a Decision_Stub object which stores a randomly chosen attribute and threshold, as well
# whether Assam is the majority class in the left group of data
class Decision_Stub:
    def __init__(self, left_is_assam_flag, threshold, attribute):
        self.left_is_assam_flag = left_is_assam_flag
        self.threshold = threshold
        self.attribute = attribute

def read_file():
    file_name = "Abominable_Data_HW_LABELED_TRAINING_DATA__v772_2245.csv"

    csv_data = pd.read_csv(file_name)

    return csv_data.values

# Recursive function which finds the last index in the array of records which has a value <= the threshold value for a specific
# attribute. Starts by checking the value at the middle index of the array. If the value is > threshold, the function is called
# again, this time checking at the index in the middle of the group of values to the left of the current index. If the value
# is <= threshold, the function is called again checking at the index in middle of the group of values to the right of the current
# index. The function recursively calls itself in this way until the last instance (index wise) of a value <= the threshold is
# found.
def find_threshold_index(index, drivers, threshold, current_best_index, attribute):
    if drivers[index][attribute] > threshold:
        if index == 0:  # if first element after the previous midpoint is greater than threshold, then the previous midpoint must be the best
            return current_best_index
        return find_threshold_index(math.ceil(drivers[:index].__len__() / 2) - 1, drivers[:index], threshold,
                                    current_best_index, attribute)
    else:
        if drivers.__len__() - 1 == index:  # only happens when there is only driver left (length of drivers is 1)
            return index + 1 + current_best_index  # since the current driver has value <= threshold, it is the
            # one we're looking for, and its index is 1 more than the previous midpoint (index is currently 0)
        return find_threshold_index(math.ceil(drivers[index + 1:].__len__() / 2) - 1, drivers[index + 1:], threshold,
                                    index if index > current_best_index else current_best_index + index + 1, attribute)

def make_decision_stub(records, decision_stubs):
    random_attribute_number = random.randrange(6)

    bhutan_records = []
    assam_records = []
    for record in records:
        if record[7] == "Bhuttan":
            bhutan_records.append(record)
        if record[7] == "Assam":
            assam_records.append(record)

    # maybe grab the 2/3 records in a random order?
    training_data_bhutan_len = math.floor(len(bhutan_records) * (2/3))
    training_data_assam_len = math.floor(len(assam_records) * (2/3))

    training_bhutan_records = [bhutan_records[i] for i in range(training_data_bhutan_len)]
    training_assam_records = [assam_records[i] for i in range(training_data_assam_len)]

    validation_bhutan_records = [bhutan_records[i] for i in range(training_data_bhutan_len, len(bhutan_records))]
    validation_assam_records = [assam_records[i] for i in range(training_data_assam_len, len(assam_records))]

    training_records = training_assam_records + training_bhutan_records
    validation_records = validation_assam_records + validation_bhutan_records
    print("Val record length ", len(validation_records))

    sorted_records = sorted(training_records, key=lambda single_record: single_record[random_attribute_number])
    random_threshold = random.uniform(sorted_records[0][random_attribute_number],
                                      sorted_records[-1][random_attribute_number])

    threshold_index = find_threshold_index(math.ceil(records.__len__() / 2) - 1, sorted_records,
                                           random_threshold, -1, random_attribute_number)

    # create the groups left and right of the threshold using the threshold_index
    left_data = sorted_records[:threshold_index + 1]
    if random_attribute_number == 6:  # the attribute at index 6 is EarLobes, a binary value attribute
        # if the attribute is binary set the random threshold to 0
        left_data = list(filter(lambda record: record[random_attribute_number] == 0, records))
        random_threshold = 0

    left_data_bhuttan_count = sum(int(record[-1]) == 1 for record in left_data)
    left_data_assam_count = sum(int(record[-1]) == -1 for record in left_data)
    left_is_assam = left_data_assam_count > left_data_bhuttan_count
    accuracy = calculate_accuracy(validation_records, random_attribute_number, random_threshold, left_is_assam)

    print("Accuracy ", accuracy)
    if accuracy < 0.5:
        left_is_assam = not left_is_assam
        # Recompute the accuracy after flipping the left is assam flag to see if there is improvement in the accuracy
        accuracy = calculate_accuracy(validation_records, random_attribute_number, random_threshold, left_is_assam)

    if accuracy >= 0.51:
        decision_stubs.append(Decision_Stub(left_is_assam, random_threshold, random_attribute_number))

def calculate_accuracy(validation_records, random_attribute_number, random_threshold, left_is_assam):
    mistakes = 0
    for record in validation_records:
        is_assam = False
        if left_is_assam:
            if record[random_attribute_number] <= random_threshold:
                is_assam = True
            else:
                is_assam = False
        else:
            if record[random_attribute_number] <= random_threshold:
                is_assam = False
            else:
                is_assam = True
        if is_assam and record[7] == "Bhuttan":
            mistakes += 1
        if not is_assam and record[7] == "Assam":
            mistakes += 1

    accuracy = (len(validation_records) - mistakes) / len(validation_records)
    return accuracy

# make the code for the classifier
def make_classifier(decision_stubs):
    classifer_program = f"""
import os
import re
import numpy as np
import argparse
import pandas as pd

def read_file(file_name):
    #file_name = "Abominable_Data_HW_LABELED_TRAINING_DATA__v772_2245.csv"

    csv_data = pd.read_csv(file_name)

    return csv_data.values

def classifier():
    parser = argparse.ArgumentParser(prog='classifier', description='Classifies snow people as Assam or Bhuttan')
    parser.add_argument('filename')
    args = parser.parse_args()

    records = read_file(args.filename)

    #classification_file = open("Classifications.csv", "w")
    #classification_file.write("")
    #classification_file.close()
    
    """

    main_string = """
def main():
    classifier()

if __name__ == '__main__':
    main()
    """

    classifer_program += "\n" + write_decision_conditionals(decision_stubs)

    file = open("Our_Classifier_Program_jae9307_dsr5964_2245.py", "w")
    file.write(classifer_program)
    file.write("\n" + main_string)
    file.close()

def write_decision_conditionals(decision_stubs):
    decisions_string = ""

    for_string = (f"    for record in records:\n"
                  f"        assam_votes = 0\n"
                  f"        bhuttan_votes = 0\n")
    for stub in decision_stubs:
        if_string = f"        if record[{stub.attribute}] <= {stub.threshold}:\n"
        if_vote_string = "            assam_votes += 1\n" if stub.left_is_assam_flag else "            bhuttan_votes += 1\n"
        else_string = f"        else:\n"
        else_vote_string = "            bhuttan_votes += 1\n" if stub.left_is_assam_flag else "            assam_votes += 1\n"
        decisions_string += if_string + if_vote_string + else_string + else_vote_string
    print_majority_class_string = f"        print('Assam' if assam_votes > bhuttan_votes else 'Bhuttan')\n"
    return for_string + decisions_string + print_majority_class_string

def compare_classifier_labels_to_training_labels():
    classifier_file = open("classifier_labels.csv", "r")
    training_file = open("Abominable_Data_HW_LABELED_TRAINING_DATA__v772_2245.csv", "r")
    classifier_list = classifier_file.readlines()
    training_list = training_file.readlines()

    mistakes = 0
    false_positives = 0
    false_negatives = 0
    true_positives = 0
    true_negatives = 0
    # Assam is the "positive" label in this case
    for i in range(1, 2401):
        training_label = training_list[i].split(",")[7].strip()
        classifier_label = classifier_list[i].strip()
        if classifier_label == "Assam" and training_label == "Assam":
            true_positives += 1
        elif classifier_label == "Assam" and training_label == "Bhuttan":
            false_positives += 1
        elif classifier_label == "Bhuttan" and training_label == "Assam":
            false_negatives += 1
        else:
            true_negatives += 1

    print(f"True positives: {true_positives}\n"
          f"False positives: {false_positives}\n"
          f"False negatives: {false_negatives}\n"
          f"True negatives: {true_negatives}")

    #accuracy = (2400 - mistakes) / 2400

def main():
    records = read_file()

    threads = []
    decision_stubs = []

    for index in range(100):
        thread = threading.Thread(target=make_decision_stub(records, decision_stubs), daemon=False)
        thread.start()
        threads.append(thread)

    for index in range(100):
        threads[index].join()

    make_classifier(decision_stubs)

if __name__ == "__main__":
    main()
    compare_classifier_labels_to_training_labels()