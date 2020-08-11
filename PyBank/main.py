
import csv
import os

 # Path to collect data from the Resources folder
open_file = os.path.join('PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join('PyBank','analysis', 'report.txt')

totalMonths = 0 
totalProfitLoss= 0
monthlyChange=[]
monthYrList=[]
greatestIncrease = 0
greatestDecrease = 0



# Read in the CSV file
with open(open_file, 'r') as csvfile:
  
  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')
  #id first row as header
  header_row = next(csvreader)
  row = next(csvreader)

  totalProfitLoss= 0
  priorChange = int(row[1])
   
  #loop each row of data 
  for row in csvreader:

    #running totals month count and profit loss
    totalMonths = totalMonths + 1 
    totalProfitLoss =  totalProfitLoss + int(row[1])

    #find month to month change in profits 
    profitChange = int(row[1]) - priorChange
    monthlyChange.append(profitChange)
    monthYrList.append(row[0])
    priorChange = int(row[1])

    #find greatest monthly increase in profit change
    if profitChange > greatestIncrease:
        greatestIncrease = profitChange
        greatestIncreaseMonthYr = row[0]

    #find Greatest monthly decrease in profit change 
    if profitChange < greatestDecrease:
        greatestDecrease = profitChange
        greatestDecreaseMonthYr = row[0]

# find average Monthly profit change 
avgProfitChg = sum(monthlyChange) / len(monthlyChange)


  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increa
  # se in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

# Print out the Financial Analysis to terminal 
analysis = (
  print("Financial Analysis"),
  print("-----------------------------------------------------------------"),
  print(f"Total Months: {str(totalMonths)}"),
  print(f"Total Profit/Loss: ${str(totalProfitLoss)}"),
  print(f"Average Monthly Profit change: ${avgProfitChg:.2f}"),
  print(f"Greatest Profit Increase: {str(greatestIncreaseMonthYr)} (${int(greatestIncrease)})"),
  print(f"Greates Profit Decrease: {str(greatestDecreaseMonthYr)} (${int(greatestDecrease)})"))

#send Analysis to output file
f = open(output_file, "w")
f.write(analysis)
f.close
