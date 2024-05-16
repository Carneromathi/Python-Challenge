
import os


import csv

csvpath = "Resources/budget_data.csv"

# The total number of months included in the dataset
months_list=[]
# The net total amount of "Profit/Losses" over the entire period
pnl_list=[]
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
change_list=[]
counter=1
# The greatest increase in profits (date and amount) over the entire period
inc_profit=0
inc_month=""
# The greatest decrease in profits (date and amount) over the entire period
dec_profit=1999999999
dec_month=""
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        months_list.append(row[0])
        pnl_list.append(int(row[1]))

        if counter>1:
            currentvalue=int(row[1])
            change=currentvalue-previousvalue
            change_list.append(change)
            if change>inc_profit:
                inc_profit=change
                inc_month=row[0]
            if change<dec_profit:
                dec_profit=change
                dec_month=row[0]
        counter +=1
        previousvalue=int(row[1])

# print(len(months_list))
# print(sum(pnl_list))
# print(round(sum(change_list)/len(change_list),2))
#print(inc_profit,inc_month,dec_profit,dec_month)
output=(

f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months_list)}\n"
f"Total: ${sum(pnl_list)}\n"
f"Average Change: ${round(sum(change_list)/len(change_list),2)}\n"
f"Greatest Increase in Profits: {inc_month} (${inc_profit})\n"
f"Greatest Decrease in Profits: {dec_month} (${dec_profit})"
)
print(output)
# Specify the file to write to
output_path = "analysis/budget_analysis.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:
    textfile.write(output)

    
