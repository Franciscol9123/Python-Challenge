# This will allow us to create file paths across operating systems and read the CSV file
import os
import csv

# Define the path to the CSV file
csvpath = '/Users/Leonardo/Documents/python module 1/PyPoll/Resources/election_data.csv'

# Define the path for the output text file
output_file_path = '/Users/Leonardo/Documents/python module 1/PyPoll/Analysis Text/election_results.txt'

# Data Variables
unique_Ballot_ID = set()  # Set to store unique ballot IDs
vote_counts = {}  # Dictionary to store vote counts for each candidate

# Function to determine the winner based on popular vote
def determine_winner(vote_counts):
    max_votes = max(vote_counts.values())  # Get the maximum number of votes
    winners = [candidate for candidate, votes in vote_counts.items() if votes == max_votes]  # Get all candidates with maximum votes
    if len(winners) == 1:
        return winners[0]  # Return the single winner
    else:
        return "It's a tie!"  # Handle tie scenarios

# Open and read the CSV file "Election Data"
with open(csvpath, 'r') as file_handler:
    csvreader = csv.reader(file_handler)
    
    # Skip the header row
    next(csvreader)
    
    # Loop through the rows in the file
    for row in csvreader:
        Ballot_ID = row[0]  # Ballots are in the first column
        candidate_name = row[2]  # Candidates are in the third column
        
        # Add the Ballot ID to the set of unique IDs
        unique_Ballot_ID.add(Ballot_ID)

        # Count votes for each candidate
        if candidate_name in vote_counts:
            vote_counts[candidate_name] += 1
        else:
            vote_counts[candidate_name] = 1

# Calculate total number of votes
total_ballots = len(unique_Ballot_ID)

# Prepare results to be printed and written to the file
results = []
results.append('Election Results')
results.append('----------------')
results.append(f'Total number of Votes: {total_ballots}')
results.append('----------------')

# Calculate and store the percentage of votes each candidate won
for candidate, votes in vote_counts.items():
    percentage = (votes / total_ballots) * 100
    results.append(f'{candidate}: {percentage:.3f}% ({votes})')

results.append('----------------')

# Determine and store the winner based on popular vote
winner = determine_winner(vote_counts)
results.append(f'Winner: {winner}')
results.append('----------------')

# Print the results
for line in results:
    print(line)

# Write the results to the output text file
with open(output_file_path, 'w') as outfile:
    for line in results:
        outfile.write(line + '\n')
