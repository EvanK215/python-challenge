
import csv
import os

 # Path to collect data from the Resources folder
Budget = os.path.join('..', 'Resources', 'Budget_data.csv')

# Read in the CSV file
with open(Budget, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# Define the function and have it accept the 'Banking_csv' as its sole parameter
def results(Budget):
    # assign values to variables with descriptive names
    #MonthYr = str(Budget[0])
    #PL = int(Budget[1])
   
  # The total number of months included in the dataset
    totalMonths =  len(list(csvreader))
  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

      # Print out the Financial Analysis

    print (f"Total Months: {str(totalMonths)}")
    #print(f"WIN PERCENT: {str(win_percent)}")
    #print(f"LOSS PERCENT: {str(loss_percent)}")
    #print(f"DRAW PERCENT: {str(draw_percent)}")
    #print(f"{name} is a {type_of_wrestler}")
