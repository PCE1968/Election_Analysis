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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # to do: perform analysis.
    print(election_data)

# Using the open() function with the "w" mode we will write data to teh file
with open(file_to_save, "w") as txt_file:
#write some data to the file.
#outfile.write("Hello World")

    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()