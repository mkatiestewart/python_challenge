import csv
import os
 

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

monthly_change = []
total_profit = []
 
with open(budget_data_csv_path, newline="") as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
 
    csv_header = next(csvfile)
     
   
    for row in readcsv:
        monthly_change.append(row[0])
        total_profit.append(int(row[1]))
         
    month_count = len(monthly_change)
     
    x = 1
    y = 0
     
    average_change = (total_profit[1]-total_profit[0])
     
    changes = []
     
    for month in range(month_count-1):
        average_change = (total_profit[x] - total_profit[y])
        changes.append(int(average_change))
        x+=1
        y+=1
         
     
    av_mon_chng = round(sum(changes)/(month_count -1),2)
 
    min_change = min(changes)
    max_change = max(changes)
 
    chng_i_min = changes.index(min_change)
    chng_i_max = changes.index(max_change)
     
    min_chng_month = monthly_change[chng_i_min + 1]
    max_chng_month = monthly_change[chng_i_max + 1]
   
 
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Monthly_change: {len(monthly_change)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Monthly Change: {av_mon_chng}")
print(f"Greatest Increase in Profits: {max_chng_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})")
 
analysis = open("Financial_Analysis.txt","w")
 
analysis.write("Financial Analysis\n")
analysis.write("----------------------------\n")
analysis.write(f"Monthly_change: {len(monthly_change)}\n")
analysis.write(f"Total: ${sum(total_profit)}\n")
analysis.write(f"Average Monthly Change: {av_mon_chng}\n")
analysis.write(f"Greatest Increase in Profits: {max_chng_month} (${max_change})\n")
analysis.write(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})\n")
 
  
analysis.close()


