#import os
import os
import csv

#Lists to store data
total_amount = 0
previous_amount = 1088983
monthly_change = 0
amount_change_list = 0
total_months= 0 
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0
average_change = 0

#Create the file path
budget_csv = os.path.join("C:/Users/hsyuk/OneDrive/Desktop/GW Bootcamp/WEEK 3 (AUG 28 - 31)/Starter_Code3/PyBank/Resources/budget_data.csv")
# Open the csv using the UTF-8 encoding
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    # Skip header
    next(csvreader)
    for row in csvreader:
        #Calculate total of months
        total_months += 1
        #Calculate the total amount over the period
        total_amount += float(row[1])
        month=row[0]
        # Find Average Change in Profit/Loss between months
        monthly_change = int(row[1])-previous_amount
        previous_amount = int(row[1])
        amount_change_list = int(amount_change_list) + int(monthly_change)
        # Find the Greatest Increase in Profits and Month over period
        if greatest_increase == 0 or monthly_change > greatest_increase:
            greatest_increase = monthly_change
            greatest_increase_month= month
        # Find the Greatest Decrease in Profits and Month over period
        if greatest_decrease ==0 or monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_month = month
            # Average change amount
average_change = int(amount_change_list)/(total_months - 1)
# Give 2 decimal for average change
average_changes = f"{(average_change):.2f}"
# Print out the summary statistics to the console and a text file
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Amount: $"+ str(total_amount))
print("Average Change: $", average_changes)
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})") 
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
