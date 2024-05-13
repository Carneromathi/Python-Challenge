
import os


import csv

csvpath = "Resources/election_data.csv"

# The total number of votes cast
totalvotes=0
# A complete list of candidates who received votes
candidates_list=[]
votes={}
# The percentage of votes each candidate won
percentages={}
# The total number of votes each candidate won

# The winner of the election based on popular vote
winner=""
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        totalvotes +=1

        candidate_name=row[2]

        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            votes[candidate_name]=0
        votes[candidate_name]+=1

    for k,v in votes.items():
        percentages[k]=round(v/totalvotes*100,3)
        


print(totalvotes)
print(candidates_list)
print(votes)
print(percentages)       
# Get the key with the maximum value
max_key = max(votes, key=lambda k: votes[k])

print("Key with the maximum value:", max_key)


# Specify the file to write to
output_path = "analysis/election_analysis.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:
    textfile.write("")

    
