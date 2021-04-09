#Import module to make data managable
import os
#Import module to read/manage csv files
import csv

#Open csv file to work in
csvpath = os.path.join('/Users','barbarahernandezrivero','Desktop','RepoGitLab','tdm-mxc-virt-data-pt-03-2021-u-c','Lessons','03-Python','Homework','Instructions','PyBank','Resources','budget_data.csv')

#List to store data
months = []
profit = []

#Structure data to manage into the scrip
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #Add months
        months.append(row[0])

        #Add profit and losses
        profit.append(row[1])

    for result in profit:
            

print(str(len(months)))

def sumalista(profit):
    total = 0.0
    for number in profit:
        total += int(number)
    return total
print(sumalista([profit]))

