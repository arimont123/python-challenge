import os
import csv
#python file in same folder as budget_data.csv
csvpath = "budget_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #start reading in data after first row of text
    csvheader = next(csvreader)
    #create empty lists to store data from each column 
    date = []
    prof_loss = []
    #loop through columns in file
    for row in csvreader: 
        date.append(row[0])
        prof_loss.append(float(row[1]))
    num_months = len(date) #calculates total number of months
    net_prof_loss = sum(prof_loss) #calculates net prof/loss over entire period
    #create empty list to store changes in prof/loss over time
    change = [] 
    for i in range(1,len(prof_loss)):
        #calculates difference in current month and previous month
        change.append(prof_loss[i]-prof_loss[i-1])
        avg_change = sum(change)/len(change)
        #find max and min change
        max_change = max(change)
        min_change = min(change)
        #For loop loops from 1 to length of prof/loss column
        #Add 1 to the index of change in order to match index of date
        max_date = str(date[change.index(max(change))+1])
        min_date = str(date[change.index(min(change))+1])
    #Print results to terminal 
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: $ {round(net_prof_loss)}")
    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {max_date} (${round(max_change)})")
    print(f"Greatest Decrease in Profits: {min_date} (${round(min_change)})")
    #Output results into text file
    f= open("bank_results.txt", 'w+') 
    f.write("Financial Analysis\n")
    f.write("-----------------------------------\n")
    f.write(f"Total Months: {num_months}\n")
    f.write(f"Total: $ {round(net_prof_loss)}\n")
    f.write(f"Average Change: ${round(avg_change,2)}\n")
    f.write(f"Greatest Increase in Profits: {max_date} (${round(max_change)})\n")
    f.write(f"Greatest Decrease in Profits: {min_date} (${round(min_change)})\n")