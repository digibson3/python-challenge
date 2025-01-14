# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/dianagibson/Desktop/DA/Challenges/python-challenge/PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/dianagibson/Desktop/DA/Challenges/python-challenge/PyBank/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

prev_profit = None
net_change_list = []
months_list = []
greatest_inc = ["",0]
greatest_dec = ["",0]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
        
    # Process each row of data
    for row in reader:

    # Extract first row to avoid appending to net_change_list
        date = row[0]
        profit = int(row[1])

    # Track the total and net change

        # Track the total
        total_months += 1
        total_net += profit
            

        # Track the net change
        if prev_profit is not None:
            net_change = profit - prev_profit
            net_change_list.append(net_change)
            months_list.append(date)
            
        # Calculate the greatest increase in profits (month and amount)            
            if net_change > greatest_inc[1]:
                greatest_inc = [date, net_change]
        # Calculate the greatest decrease in losses (month and amount)        
            if net_change < greatest_dec[1]:
                greatest_dec = [date, net_change]
                
        prev_profit = profit

# Calculate the average net change across the months
average_change = round(sum(net_change_list) / len(net_change_list), 2)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
    f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n"
)

# Print the output

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
