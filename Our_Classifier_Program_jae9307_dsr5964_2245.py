
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
    
    
    for record in records:
        assam_votes = 0
        bhuttan_votes = 0
        if record[4] <= 6.810976027645334:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[2] <= 5.173279202451548:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[3] <= 12.56354430268713:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[2] <= 2.966889011637144:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 10.889383876289072:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 146.67044554474546:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 148.12961135565985:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 129.43773832947082:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 152.1709941742522:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 4.081669965600867:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 5.663613452783503:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[5] <= 150.24680856000833:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 130.67524357550099:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[3] <= 13.70897492758305:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[0] <= 33.27168972858012:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 135.54096981653757:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 6.653510903256388:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 4.1715196281195634:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[2] <= 11.796100772994535:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 9.560881011086915:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 137.3238374165482:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 154.78301406739672:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[0] <= 35.66968866906859:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 3.664142069795543:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[3] <= 6.72199312017305:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[3] <= 11.887782640593365:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 8.997614403449774:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[0] <= 60.92494947322736:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 4.566932843968474:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[1] <= 162.28879169654272:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[0] <= 55.121016972252434:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 135.8480121724916:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[3] <= 6.480689769895211:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[2] <= 16.6627472593617:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 156.67217740357069:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[0] <= 25.460172444371537:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 8.624815334800306:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[3] <= 7.066138577392638:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[5] <= 131.69039212249726:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 166.4151655641753:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 168.61284728796386:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 168.1140727401181:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[1] <= 158.8432854925452:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 7.001529444938756:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 160.27358328858136:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 6.908954176435224:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 148.35257663976904:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 3.1163710756346408:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 4.258379665690158:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[1] <= 151.18169192627659:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[3] <= 13.569879001892048:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[1] <= 152.7196168925346:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[3] <= 11.521947512352348:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 8.086279211559903:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 7.980858754056549:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 3.3265994870473587:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 3.001447688520763:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[2] <= 3.0524663209745766:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[0] <= 30.578870562295194:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[2] <= 6.704312604274996:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 5.527018982372341:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[4] <= 7.213841855747936:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[3] <= 13.900612425863894:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[1] <= 150.38225888115502:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[4] <= 4.716401880945215:
            assam_votes += 1
        else:
            bhuttan_votes += 1
        if record[5] <= 174.98370517877433:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[0] <= 29.106143983314503:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        if record[5] <= 148.33362397576266:
            bhuttan_votes += 1
        else:
            assam_votes += 1
        print('Assam' if assam_votes > bhuttan_votes else 'Bhuttan')


def main():
    classifier()

if __name__ == '__main__':
    main()
    