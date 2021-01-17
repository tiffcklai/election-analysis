#The data we need to retrieve.
#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')

#Create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join('analysis','election_analysis.txt')

#1a. The total number of votes cast
total_votes = 0

#2a. A complete list of candidates who received votes 
candidate_options = []

#3a. Declare the empty dictionary
candidate_votes = {}

#5a. Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read the file 
with open(file_to_load) as election_data:

    #To do: perform analysis
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row 
    headers=next(file_reader)
    
    #print each row in the CSV file 
    for row in file_reader: 

        #1b. Add to the total vote count 
        total_votes +=1

        #2b. Print the candidate name from each row 
        candidate_name = row[2]

        #2c. If candidate does not match an exiting candidates 
        if candidate_name not in candidate_options:

            #2d. Add candidate name to candidate options
            candidate_options.append(candidate_name)

            #3b. Begin tracking the candidate's vote count 
            candidate_votes[candidate_name]=0

        #3c. Add a vote to the candidate's count 
        candidate_votes[candidate_name] +=1

#Save results to our text file 
with open(file_to_save, 'w') as txt_file:

#Print the final vote count to the terminal.
    election_results = ( 
        f'\nElection results\n'
        f'---------------------------------\n'
        f' Total Votes : {total_votes:,}\n'
        f'---------------------------------\n')

    print(election_results, end = '')

    #Save the final vote count to the text file 
    txt_file.write(election_results)
        
    #4.a Determine the percentage of votes for each vandidate by looping through the counts 
    for candidate_name in candidate_votes: 

        #4b. Retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]

        #4c. Calculate the percentage of votes 
        vote_percentage = float(votes)/float(total_votes)*100 

        #To do: print out each candidate's name, vote count, and percentage of # votes to the terminal 
        candidate_results=(f'{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n')

        #Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)

        #Save the candidate results to our text file 
        txt_file.write(candidate_results)

        #5b. Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count 
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            #5c. If true, then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes 
            winning_percentage = vote_percentage 
            #5d. Set the winning_candidate equal to the candidate's name 
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f'-----------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-----------------------------\n')
    print(winning_candidate_summary)

    #Save the winning candidate's results to the text file 
    txt_file.write(winning_candidate_summary)
