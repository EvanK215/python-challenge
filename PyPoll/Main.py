import csv
import os

 # Path to collect data from the Resources folder
open_file = os.path.join('Pypoll', 'Resources', 'election_data.csv')
output_file = os.path.join('Pypoll', 'Resources', 'pollResults.txt')

#Lists and Varibles
tBallots = 0
voters = []
counties = []
candidates = []
Correy = 0 
Khan = 0
Li =0 
OTooley =0 

# Read in the CSV file
with open(open_file, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #id first row as header
    header_row = next(csvreader)
    #row = next(csvreader)

    #loop each row of data 
    for row in csvreader:
    #running totals for total ballots received
        tBallots = tBallots + 1
        #Add candi of the row to the correct list 

        Candidate =(row[2])
            # find the candidate and add that to their vote count 
        if Candidate == "Correy":
            Correy += 1
        elif (row[2]) == "Khan":
            Khan += 1 
        elif (row[2]) == "Li":
            Li += 1
        else: OTooley += 1
        #calculate percentages
        correyPct = "{:.3%}".format (Correy / tBallots)
        khanPct = "{:.3%}".format (Khan /tBallots)
        liPct = "{:.3%}".format (Li/tBallots)
        otooleyPct = "{:.3%}".format (OTooley /tBallots)
        
   
    #print 
   
    print ("Election Results")
    print ("-------------------------") 
    print ("Total Votes")
    print(tBallots)
    print ("-------------------------")
    print("Correy: {str(correyPct)},  ({correy})")
    #print (f"Correy: {int((Khan)/(tBallots)"% ("(khan)
    print (Khan)
    print (Li)
    print (OTooley)



                



  



    

