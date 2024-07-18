# Python-Challenge
In the following code, I created python scripts for analyzing the finaancial records of PyBank and the election results of PyPoll. 

* PyBank: Analysis on monthly Profit/Loss data
* PyPoll: Analysis on election result

## PyBank
![revenue-per-lead](https://github.com/user-attachments/assets/17051060-408b-4469-81ea-96f42df0f4a9)
In this work, I created a Python script for analyzing the financial records of PyBank. With a set of financial data called budget_data.csv, the dataset is composed of two columns: Date and Profit/Losses.

Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period
* Lastly, printing the results to text

Financial Analysis
------------------
Total number of months: 86
Net total amount of "Profit/Losses": $22,564,198.00
Average Change in "Profit/Losses": $-8,311.11
Greatest Increase in Profits: Aug-16 ($1,862,002.00)
Greatest Decrease in Profits: Feb-14 ($-1,825,558.00)

## PyPoll
![Vote_counting](https://github.com/user-attachments/assets/ec32745d-353a-4f5a-9f43-17aca5ee6cc4)

In this work, I created a Python script for analyzing the votes of election result of PyPoll.

With a set of poll data called election_data.csv, the dataset is composed of three columns: Voter ID, County, and Candidate.

Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote
* Lastly, printing the results to text

Election Results
----------------
Total number of Votes: 369711
----------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
----------------
Winner: Diana DeGette
----------------
