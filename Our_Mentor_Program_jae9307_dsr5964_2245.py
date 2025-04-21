import pandas as pd

def read_file():
    file_name = "Abominable_Data_HW_LABELED_TRAINING_DATA__v772_2245.csv"

    csv_data = pd.read_csv(file_name)
    # csv_data.drop(['ID', 'Art&Hist', ' Gifts', 'Poetry'], axis=1, inplace=True)

    return csv_data.values

def main():
    records = read_file()

    assam_records = [record for record in records if int(record[-1]) == -1]
    bhuttan_records = [record for record in records if int(record[-1]) == 1]

    print(len(assam_records))
    print(len(bhuttan_records))

if __name__ == "__main__":
    main()