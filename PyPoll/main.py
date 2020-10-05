import csv

csvpath = "Resources/election_data.csv"

votes= []
candidates= {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    for row in csvreader:

        votes.append(row[0])
        voted_candidate= row[2]
        if voted_candidate in candidates:
            candidates[voted_candidate] += 1
        else:
            candidates[voted_candidate] = 1
unique_votes = set(votes)

winner_votes= 0
winner = ""
candidate_result = ""
for candidate, c_votes in candidates.items():
    percentage = c_votes/len(unique_votes)*100.0
    if c_votes > winner_votes:
        winner= candidate
        winner_votes= c_votes
    candidate_result += f"{candidate} %{percentage:.2f} ({c_votes})\n"



result= f"""
Election Results
-----------------------
Total votes: {len(unique_votes)}
-----------------------
{candidate_result}
-----------------------
Winner: {winner}
"""


print(result) 



with open("Analysis/election_data.txt", "w") as result_f:
    result_f.write(result)


