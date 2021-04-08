#Import module to make data managable
import os
#Import module to read/manage csv files
import csv

csvpath = os.path.join('/Users','barbarahernandezrivero','Desktop','RepoGitLab','tdm-mxc-virt-data-pt-03-2021-u-c','Lessons','03-Python','Homework','Instructions','PyBank','Resources','budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)



    