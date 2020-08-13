import csv
import os

 # Path to collect data from the Resources folder
open_file = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('Analysis', 'pollResults.txt')

#Lists and Varibles
tBallots = 0
votes = []
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

#votes = [Khan, Li, Correy, OTooley]
results = {Khan: "Khan",Li: "Li",Correy: "Correy",OTooley: "OTooley"}
winner = (results.get(max(results)))

#prints to Terrmial     
print (f"Election Results")
print ("-------------------------") 
print (f"Total Votes")
print (tBallots)
print ("-------------------------")
print (f"Khan: {str(khanPct)}  ({Khan})")
print (f"Correy: {str(correyPct)}  ({Correy})")
print (f"Li: {str(liPct)}  ({Li})")
print (f"O'Tooley: {str(otooleyPct)}  ({OTooley})")
print ("-------------------------")
print (f"The Winner is: " + winner)  

#send Analysis to output file
with open (output_file, 'w') as textfile:
    textfile.write (f"Election Results\n")
    textfile.write ("-------------------------\n") 
    textfile.write (f"Total Votes\n")
    textfile.write (f"{str(tBallots)}\n")
    textfile.write ("-------------------------")
    textfile.write (f"Khan: {str(khanPct)}  ({Khan})\n")
    textfile.write (f"Correy: {str(correyPct)}  ({Correy})\n")
    textfile.write (f"Li: {str(liPct)}  ({Li})\n")
    textfile.write (f"O'Tooley: {str(otooleyPct)}  ({OTooley})\n")
    textfile.write ("-------------------------\n")
    textfile.write ("The Winner is: " + (winner))  



                



  



    

