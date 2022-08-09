import os
import csv

election_data_path = os.path.join("Resources", "election_data.csv")

vote_list = []
candidate = []
percentage_votes = []
count_candidate = []
winner = []
total_votes = []

with open(election_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        vote_list.append(row[2])
        
    for row in csvreader:
        total_votes.append(row[0])
        vote_list.append(int(row[1]))

for name in vote_list:
   if name not in candidate:
        candidate.append(name)
        x = name

count = 0
candidate = vote_list[0]
last_count = 0


print ("Election results :")
print(total_votes)
print(candidate)
print(percentage_votes)
print(total_votes)
print(winner)


analysis = open("election_results.txt","w")
 
analysis.write("Election Results\n")
analysis.write("----------------------------\n")
analysis.write(f"Total_Votes: {len(total_votes)}\n")
analysis.write(f"Candidate: {candidate}\n")
analysis.write(f"Percentage Votes: {percentage_votes}\n")
analysis.write(f"WINNER!!: + winner\n")

analysis.close()
