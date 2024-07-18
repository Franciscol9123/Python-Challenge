# This will allow us to create file paths across operating systems
import os 

# Module for reading CSV files
import csv

# Define the path to the CSV file
csvpath = '/Users/Leonardo/Documents/python module 1/PyBank/Resources/budget_data.csv'

# Define the path for the output text file
output_file_path = '/Users/Leonardo/Documents/python module 1/PyBank/Analysis Text/financial_analysis.txt'

# Plain Reading of CSV files
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))
    
# variables
unique_months = set()
net_total=0
monthly_changes= []
previous_profit_loss= None
greatest_increase= {'date':None, 'amount': float('-inf')}
greatest_decrease= {'date':None, 'amount': float ('inf')}

# Open and read the CSV file
with open(csvpath, 'r') as file_handler:
    csvreader = csv.reader(file_handler)
    
    # Skip the header row
    next(csvreader)
    
    # Loop through the rows in the file
    for row in csvreader:
        date = row[0]  #the date is in the first column
        profit_loss = int(row[1]) #the profit/loss is in the second column
        
        # add the date to the set of unique months
        unique_months.add(date)

        #add the profit/loss to the net total
        net_total += profit_loss

        #calculate the monthly change and add to the list of changes
        if previous_profit_loss is not None: 
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)

            #check for the greatest increase in profits
            if monthly_change > greatest_increase['amount']:
                greatest_increase['amount']= monthly_change
                greatest_increase['date']= date

            #check for the greatest decrease in profits
            if monthly_change < greatest_decrease['amount']:
                greatest_decrease['amount']= monthly_change
                greatest_decrease['date']= date
        
        # Update the previous profit/loss
        previous_profit_loss = profit_loss

# Count the total number of unique months
total_months = len(unique_months)

#calculate the average change in profit/lossess
if len(monthly_changes) > 0:
    average_change = sum(monthly_changes)/ len(monthly_changes)
else:
    average_change= 0

# Prepare results to be printed and written to the file
results = []
results.append('Financial Analysis')
results.append('------------------')
results.append(f'Total number of months: {total_months}')
results.append(f'Net total amount of "Profit/Losses": ${net_total:,.2f}')
results.append(f'Average Change in "Profit/Losses": ${average_change:,.2f}')
results.append(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]:,.2f})')
results.append(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]:,.2f})')

# Print the results
for line in results:
    print(line)

# Write the results to the output text file
with open(output_file_path, 'w') as outfile:
    for line in results:
        outfile.write(line + '\n')
