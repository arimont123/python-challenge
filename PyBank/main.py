import os
import csv
csvpath = "budget_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    date =  [] #create empty lists for the data
    prof_loss = []
    change = []
    
    for row in csvreader:
        date.append(row[0]) #populate list with data
        num_months = len(date)
        prof_loss.append(float(row[1]))
        net_prof_loss = (sum(prof_loss))
    for i in range(1,len(prof_loss)):
        change.append(prof_loss[i]-prof_loss[i-1])
        avg_change = sum(change)/len(change)
        max_change = max(change)
        min_change = min(change)
        #for loop is in range of 1 to length of prof/loss column
        #Add 1 to the index of max/min change in order to match index of date
        max_date = str(date[change.index(max(change))+1]) 
        min_date = str(date[change.index(min(change))+1])
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: $ {round(net_prof_loss)}")
    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {max_date} (${round(max_change)})")
    print(f"Greatest Decrease in Profits: {min_date} (${round(min_change)})")
   

    