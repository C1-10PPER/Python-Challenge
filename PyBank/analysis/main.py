import csv
import os





file_to_load = os.path.join("..", "Resources", "budget_data.csv")  
file_to_output = os.path.join("analysis", "budget_analysis.txt")  

total_months = 0
total_net = 0

print("Financial Analysis")
print("------------------------")

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")



    header = next(reader)
    # print(f'Header: {header}')


    for row in reader:
        total_months += 1
        total_net +=int(row[1])

print(f"Total Months: {total_months}")
print(f"Total: {total_net}")
# month_index = header.index('Date')
# num_months = set(row[month_index] for row in data)
# print(f'Total Months: {len(num_months)}')
# print(f'Total: ')

# PL_Index = header.index('Profit/Losses')
# PL_Totals = sum(float(row['Profit/Losses']) for row in data if row['Profit/Losses'])
# print(f'Total: {PL_Totals}')
   


# print("Financial Analysis")
# print("----------------------------------------")

# def budget_num(Fin_data):
#     Date = Fin_data[0]
#     P_L = int(Fin_data[1])


#     Date_count = len(Date)
#     Total_PL = (P_L)
#     return Date_count, Total_PL


# for row in reader:
    # Date_count, Total_PL = budget_num(row)
    # print(f"Total Months: {Date_count}, Total P/L: {Total_PL}")

# with open(file_to_output, "w") as txt_file:
#     txt_file.write(output)
