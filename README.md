# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the voter turnout for each county.
3. Calculate the percentage of votes from each county out of hte total count.
4. Determine the county wih the highest turnout.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.


## Resources
- Data Source: election_results.csv
- Software: Pythin 3.9.7, Visual Studio Code, 1.63.2

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county turnout results were:
    - Jefferson County accounted for 10.5% of the vote with 38,855 votes.
    - Denver County accounted for 82.8% of the vote with 306,055 votes.
    - Arapahoe County accounted for 6.7% of the vote with 24,801 votes.
- County with the largest Number of votes cast:
    - Denver County accounted for 82.8% of the vote with 306,055 votes. 
- The candidate results were:
    - Charles CVasper Stockham received 23.0% of the vote with 85,213 votes.
    - Diana DeGette received 73.8% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was:
    - Diane DeGette received 73.8% of the vote with 272,892 votes.

 ## Election Audit Summary
The results demonstrate that all of the requirements have been met. The total votes have been tabulated. The county turnout has been recorded for total votes cast and the percentage of total vote for each county. The candidate votes have also been tabulated and considered by percentage of total vote, and the election winner has been identified. Even though this code runs well as is, there are limitations. Any future election results will need to be added to the same folder and the file name will need to match. In addition, the file structure will also need to match the current column order of the .csv file, otherwise the code will not run correctly.

### Modification Options
When considering file location as a limitation, a potenital solution could look something like this:

![Prompt the user for folder location and file name](Resources/User_input_solution.png)

This code prompts the user to provide the path to the folder and the file name that holds the election results. Similar code could also be added for file storage.


A potential solution for the .csv file column order could look like this:

![Filter the header to determine the correct index for the county and candidate data in the .csv](Resources/Dynamic_header_filter.png)

This set of filters will identify the correct index for the county and candidate columns, allowing for files whos columns may be in a different order.


Both of these options will make the code more dynamic and useful for analyzing election results for other election audits.
