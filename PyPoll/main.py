import os
import csv
#python script is saved in same folder as csv
csvpath = "election_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    voterID = [] #create empty lists for each column 
    county = []
    candidate = []
    for row in csvreader:
        #pupulate lists with data from each column
        voterID.append(row[0]) 
        county.append(row[1])
        candidate.append(row[2])
    total_votes = len(voterID) #calculates total number of votes
    #set count for each candidates vote to zero 
    khan_vote = 0 
    correy_vote = 0
    li_vote = 0
    otool_vote = 0
    #loop through candidate column
    for person in range(0,len(candidate)):
        if candidate[person] == "Khan":
            #adds 1 to vote count every time the candidate is encountered 
            khan_vote += 1 
            #calculates percentage of candidates votes
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
    #prints results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"Khan: {round(khan_perc)}.000% ({khan_vote})")
    print(f"Correy: {round(correy_perc)}.000% ({correy_vote})")
    print(f"Li: {round(li_perc)}.000% ({li_vote})")
    print(f"O'Tooley: {round(otool_perc)}.000% ({otool_vote})")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")
    #Export text file with results
    f= open("Poll_Results.txt", 'w+') 
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    f.write(f"Khan: {round(khan_perc)}.000% ({khan_vote})\n")
    f.write(f"Correy: {round(correy_perc)}.000% ({correy_vote})\n")
    f.write(f"Li: {round(li_perc)}.000% ({li_vote})\n")
    f.write(f"O'Tooley: {round(otool_perc)}.000% ({otool_vote})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------")
    
    
