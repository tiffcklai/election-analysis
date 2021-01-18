# Election Analysis Challenge with Python and Visual Studio Code

## Resources 
* Data Source: [election_results.csv](Resources/election_results.csv)
* Software: Python 3.8.5, Visual Code Studio 1.52.1
* PyPoll_Challenge Code: [PyPoll_Challenge](PyPoll.py) 

## Overview of Election Audit
Colorado Board of Elections requested data analysis to extract the following information:
  1. Total number of votes cast 
  2. Voter turnout for each county
  3. Percentage of votes from each county out of the total count 
  4. The county with the highest turnout
  5. A complete list of candidates who received votes
  6. Total number of votes each candidate received 
  7. Percentage of votes each candidate received 
  8. The winner of the election based on the popular vote 
  
## Election-Audit Results 
Please refer to the results of the elections in the following txt file:  [election_analysis.txt](analysis/election_analysis.txt)
* In this congressional election, there were a total of **369,711** votes casted. 

* The following counties were involved in the election
    * Jefferson 
      * A total number of **38,855** votes were casted from Jefferson. This makes up **10.5%** of the total vote count.
    * Denver 
      * A total number of **306,055** votes were casted from Jefferson. This makes up **82.8%** of the total vote count.
    * Arapahoe
      * A total number of **24,801** votes were casted from Jefferson. This makes up **6.7%** of the total vote count.

* From the election analysis, it is clear that **Denver** is the county with the highest voter turnout of **306,055**. This county makes up **82.8%** of all voters in this election; significantly higher than the other 2 counties. 

* The following results were determined from the analysis for each candidate: 
    * Charles Casper Stockham - This candidate received **85,213** votes, accounting for **23.0%** of all voters. 
    * Diana DeGette - This candidate received **272,892** votes, accounting for **73.8%** of all voters.
    * Raymon Anthony Doane - This candidate received **11,606** votes, accounting for **3.1%** of all voters. 

* The winner of the election goes to **Diane DeGette** who obtained a total of **272,892** votes. This candidate secured **73.8%** of the total vote count. 

## Election-Audit Summary 

For future elections, this script can be modified to include more statistics. This will provide increased insight towards the election results. The code can be modified to include the political party each candidate represents (e.g. Democratic, Republican, etc.). Additionally, this would be useful for a federal election, where county variables can be changed to represent all the states and which party won which state. Another suggestion, is to determine the percentage of voters against each county population. This can determine the relative voter outcome per county. For example, if Denver has the highest population, then it makes sense they received the highest voter turnout. However, the relative turnout could be similar if Jefferson and Arapahoe have significantly smaller populations. Lastly, the Ballot IDs can be used to determine if any citizen wrongfully voted twice. This can be completed by sorting all the Ballot IDs into a list in ascending order; followed by a for loop that goes through each row to determine if an ID number has occurred twice. 
