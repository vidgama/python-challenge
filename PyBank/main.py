import os
import csv
import sys

# Output File 
stdoutOrigin=sys.stdout 
sys.stdout = open(os.path.join('Analysis','financial_results.txt'), "w")

# Input File 
csvpath = os.path.join('Resources','budget_data.csv')
norm_path = os.path.normpath(csvpath)

# Variables 
total_months = [ ]
total = [ ]
profit = [ ]

# Open Input File
with open(norm_path) as csvfile:

	csvreader = csv.reader(csvfile,delimiter=',')
	csvreader.__next__()
	
	for row in csvreader:
	
	    # Total of months and total profit
		total_months.append(row[0])
		total.append(int(row[1]))
	
	# Iteration for profit 
	for i in range(len(total)-1):

		# Monthly profit change
		profit.append(total[i+1]-total[i])

# Max and min overall
max_increase_value = max(profit)
max_decrease_value = min(profit)

# Max and min for next month
max_increase_month = profit.index(max(profit)) + 1
max_decrease_month = profit.index(min(profit)) + 1

# DRY method to print results
def printResults():
	print("------------------------------")
	print("Financial Analysis")
	print("------------------------------")
	print(f"Total Months: {len(total_months)}")
	print(f"Total: ${sum(total)}")
	print(f"Average Change: ${round(sum(profit)/len(profit),2)}")
	print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
	print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Print results to Output File
printResults()
sys.stdout.close()

# Print results to Console
sys.stdout=stdoutOrigin
printResults()