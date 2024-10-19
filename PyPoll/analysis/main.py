
import csv
import os
#importing packages

file_to_load = os.path.join("..", "Resources", "election_data.csv")  
file_to_output = os.path.join("election_analysis.txt")  
# file path for the csv file and the txt file


total_votes = 0  
vote_count = {}
# initializing the value for these two variables


with open(file_to_load) as election_data: # Open the csv file
    reader = csv.reader(election_data, delimiter=",") 
    # Reads the csv file and acknowledges the data is split between the commoas

    header = next(reader) # reads the header row

   
    for row in reader:
        total_votes += 1
        vote = row[2]
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
# code above used to count the number of votes

winner = max(vote_count, key=vote_count.get) 
# determine winner by getting the candidate with the most votes
count_charles = (vote_count["Charles Casper Stockham"])
count_diana = (vote_count["Diana DeGette"])
count_raymon = (vote_count["Raymon Anthony Doane"])
# counting the votes for each candidate

election_outcome = (
f"Election Results\n"
f"\n"
f"------------------------\n"
f"\n"
f"Total Votes: {total_votes}\n"
f"\n"
f"------------------------\n"
f"\n"
f"Charles Casper Stockham: {(count_charles/total_votes):.3%}, ({count_charles})\n"
f"Diana DeGette: {(count_diana/total_votes):.3%}, ({count_diana})\n"
f"Raymon Anthony Doane: {(count_raymon/total_votes):.3%}, ({count_raymon})\n"
f"\n"
f"------------------------\n" 
f"\n"


f"Winner: {winner}\n"
f"\n"
f"------------------------\n"
)
# Created a variable called election outcome to store all the required 
# data for the assignment so that the data can easily be written to a text file. 

print(election_outcome)
        
with open(file_to_output, "w") as election_analysis:
    election_analysis.write(election_outcome)
# writes the data stored in election_outcome to a text file called election_analysis.txt
 