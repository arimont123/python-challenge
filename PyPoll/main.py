import os
import csv
csvpath = "election_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    voterID = []
    county = []
    candidate = []
    for row in csvreader:
        #create lists of data for each column
        voterID.append(row[0]) 
        county.append(row[1])
        candidate.append(row[2])
    total_votes = len(voterID) #calculates total number of votes

    khan_vote = 0
    correy_vote = 0
    li_vote = 0
    otool_vote = 0
    for person in range(0,len(candidate)):
        if candidate[person] == "Khan":
            khan_vote += 1 #adds 1 to khan_vote every time the candidate is encountered 
            khan_perc = (khan_vote/total_votes)*100
        if candidate[person] == "Correy":
            correy_vote += 1
            correy_perc = (correy_vote/total_votes)*100
        if candidate[person] == "Li":
            li_vote +=1
            li_perc = (li_vote/total_votes)*100
        if candidate[person] == "O'Tooley":
            otool_vote += 1
            otool_perc = (otool_vote/total_votes)*100
    #finds the winner based on the largest vote percentage of each candidate
    if khan_perc > correy_perc and li_perc and otool_perc:
        winner = "Kahn"
    elif correy_perc> khan_perc and li_perc and otool_perc:
        winner = "Correy"
    elif li_perc> correy_perc and kahn_perc and otool_perc:
        winner = "Li"
    elif otool_perc> khan_perc and li_perc and correy_perc:
        winner = "O'Tooley"

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"Khan: {round(khan_perc)}% ({khan_vote})")
    print(f"Correy: {round(correy_perc)}% ({correy_vote})")
    print(f"Li: {round(li_perc)}% ({li_vote})")
    print(f"O'Tooley: {round(otool_perc)}% ({otool_vote})")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")