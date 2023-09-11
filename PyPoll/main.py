# import csv
import os
import csv
# Create variables
total_votes = 0
CCS_votes = 0
DD_votes = 0
RAD_votes = 0
winner = None
candidates = []
candidate_votes= {}
# Create a file path 
poll_csv=os.path.join("C:/Users/hsyuk/OneDrive/Desktop/GW Bootcamp/WEEK 3 (AUG 28 - 31)/Starter_Code3/PyPoll/Resources/election_data.csv")
# Open the csv using the UTF-8 encoding
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    # Skip header
    next(csvreader)
    for row in csvreader:
    # Calculate the total number of votes cast
        total_votes += 1
    # Calculate the candidates who got votes
        # Charles Casper Stockham
        if row[2] == 'Charles Casper Stockham':
            CCS_votes += 1
            CCS_percent = f"{((CCS_votes/total_votes)*100):.3f}%"
        # Diana DeGette
        if row[2] == 'Diana DeGette':
            DD_votes += 1
            DD_percent = f"{(DD_votes/total_votes)*100:.3f}%"
        # Raymon Anthony Doane
        if row[2] == 'Raymon Anthony Doane':
            RAD_votes += 1
            RAD_percent = f"{(RAD_votes/total_votes)*100:.3f}%"

    # Find the winner of the election based on popular votes
        if CCS_votes > DD_votes and CCS_votes > RAD_votes:
            winner = "Charles Casper Stockham"
        if DD_votes > CCS_votes and DD_votes > RAD_votes:
            winner = "Diana DeGette"
        if RAD_votes > CCS_votes and RAD_votes > DD_votes:
            winner = "Raymon Anthony Doane"
      
print(candidates)
# Print out summary statistics
print("Election Results")
print("--------------------------")
print("Total Votes:" , total_votes)
print("--------------------------")
print(f"Charles Casper Stockham: {CCS_percent} ({CCS_votes})")
print(f"Diana DeGette: {DD_percent} ({DD_votes})")
print(f"Raymon Anthony Doane: {RAD_percent} ({RAD_votes})")
print("--------------------------")
print("Winner:", winner)
print("--------------------------")
