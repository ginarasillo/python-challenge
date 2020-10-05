

import csv

csvpath = "Resources/budget_data.csv"

months= []
total= 0
total_change = 0
last_value = None
g_increase= 0
g_decrease= 0
increase_month= ""
decrease_month= ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    # (skip this step if there is now header)
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:

        months.append(row[0])
        profit = float(row[1])
        total += profit
        if last_value:
            change = profit - last_value
            total_change += change
            if change > g_increase:
                g_increase= change
                increase_month= row[0]
            if change < g_decrease:
                g_decrease=change
                decrease_month= row[0]

        last_value = profit

        



        # si profit es mayor a mi greatest
            # mi nuevo greatest es profit
            # mi nuevo greatest_month es month

unique_months = set(months)


result= f"""
Financial Analysis
-----------------------
Total Months: {len(unique_months)}
Total: ${total}
Average Change: {total_change/(len(months)-1):.2f}
Greatest Increase in Profits: {increase_month} (${g_increase})
Greatest Decrease in Profits: {decrease_month} (${g_decrease})
"""

print(result)

with open("Analysis/budget_result.txt", "w") as result_f:
    result_f.write(result)
