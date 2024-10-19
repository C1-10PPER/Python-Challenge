import csv
import os
# importing packages

file_to_load = os.path.join("..", "Resources", "budget_data.csv")  
file_to_output = os.path.join("budget_analysis.txt")  
# file path to open and read the data from the csv file and write to the txt file


total_months = 0
total_net = 0
values = [0]
dates = [0]
# initializing the value for these four variables


with open(file_to_load) as financial_data: # Open the csv file
    reader = csv.reader(financial_data, delimiter=",") 
    # Reads the csv file and acknowledge the data is split between the commoas
    header = next(reader) # reads the header row

    for row in reader:
        total_months += 1 # counts the total number of months
        total_net += int(row[1]) # calculates the total amount
        values.append(int(row[1])) # appending the value in the P&L column
        dates.append(row[0]) # appending the value in the date column


    changes = [values[i+1] - values[i] for i in range(1, len(values)-1)] 
    # calculating the value of the change between current row and the proceeding 
    # row through the entire rows in the P&L column

    avg_chg = sum(changes)/(len(changes))
    max_chg = max(changes)
    min_chg = min(changes)
#  The three lines of code above is used to determine the average change, 
#  the amount of the greatest increase in profits and the amount of the greatest 
#  decrease in profits.

    max_index = changes.index(max(changes))+2
    max_date = dates[max_index]
    # Code is executed to determine the date of the greatest increase in profits. 
    min_index = changes.index(min(changes)) + 2
    min_date = dates[min_index]
    # Code is executed to determine the date of the greatest decrease in profits. 


financial_results = (
f"Financial Analysis\n"
f"\n"
f"------------------------\n"
f"\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: ${avg_chg:.2f}\n"
f"Greatest Increase in Profits: {max_date} (${max_chg})\n"
f"Greatest Decrease in Profits: {min_date} (${min_chg})\n"
)
# Created a variable called financial_results to store all the required 
# data for the assignment so that the data can easily be written to a text file. 

print(financial_results)
#prints the results        
with open(file_to_output, "w") as budget_analysis:
    budget_analysis.write(financial_results)
# writes the data stored in financial_results to a text file called budget_analysis.txt