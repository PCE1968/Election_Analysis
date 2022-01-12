# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# creat a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalize a  total votes counter.
total_votes = 0
#votes = 0
# Declare list for candidates
candidate_options = []

# Declare dictionary for candidate vote counts
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # to do: perform analysis.
    #print(election_data)
    file_reader = csv.reader(election_data)



     # Print the header row.
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        # 2. Add to the total votes count.
        total_votes += 1
 
        # Print the candidate name from each row
        candidate_name = row[2]
        
        # Add if statement to find unique candidate names
        if candidate_name not in candidate_options:
            
            # Add the candidate name to teh candidate list.
            candidate_options.append(candidate_name)
            #votes = 0
        
            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and the percentage of votes.
    print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.")

# Print the candidate list
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)

# 3. Print the total votes
#print(total_votes)

# Using the open() function with the "w" mode we will write data to teh file
#with open(file_to_save, "w") as txt_file:
#write some data to the file.
#outfile.write("Hello World")

    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
#txt_file.close()