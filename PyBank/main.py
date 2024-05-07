
import os


import csv

csvpath = "Resources/budget_data.csv"

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)



# Specify the file to write to
output_path = "analysis/budget_analysis.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:
    textfile.write("")

    
