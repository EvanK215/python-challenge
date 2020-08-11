import csv
import os

 # Path to collect data from the Resources folder
open_file = os.path.join('Pypoll', 'Resources', 'election_data.csv')
output_file = os.path.join('Pypoll', 'Resources', 'pollResults.txt')

tBallots = 0


# Read in the CSV file
with open(open_file, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #id first row as header
    header_row = next(csvreader)
    #row = next(csvreader)
    #Lists
    voters = []
    counties = []
    candidates = []
    Bamoo = 0
    Marsh = 0
    Queen = 0
    Raffah = 0
    Trandee = 0

    #loop each row of data 
    for row in csvreader:
    #running totals for total ballots received
        tBallots = tBallots + 1
        #Add contant of the row to the correct list 
        voter.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
            # count 
            if county in counties == "Marsh"


    print(tBallots)



    

