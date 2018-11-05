import csv
import os

budget1 = "/Users/lauradu/Desktop/budget_data_1.csv"

total_months = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

revenue_changes =[]

with open(budget1) as revenue_data:
    reader = csv.DictReader(revenue_data)

for row in reader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(first_row[1])
    
        revenue_change = int(first_row[1]) - prev_revenue
      
        prev_revenue = int(first_row[1])

revenue_change = int(first_row[1]) - prev_revenue
        prev_revenue = int(row[first_row[1]])
       
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        
        revenue_changes.append(int(row[first_row[1]]))
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

