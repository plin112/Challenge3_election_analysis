# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

# Initialize a total vote counter.
total_votes = 0
# canditate options
candidate_options = []
# declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# counties involed in election
county_list = []
# declare dictionary
county_votes = {}

# largested county turnout
largest_county = ""
largest_count = 0
largest_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
        county_involved = row[1]

        if county_involved not in county_list:
            county_list.append(county_involved)
            county_votes[county_involved] = 0
        county_votes[county_involved] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    txt_file.write("County Votes: \n")

    # generate list of county
    for county in county_votes:
        # retrieve vote counte in each county
        votes_c = county_votes[county]
        # calculate the percentage of votes in each county
        vote_percentage_c = float(votes_c)/float(total_votes) * 100
        # print the county name, vote count, and percentage of count in each county
        county_result = (
            f"{county}: {vote_percentage_c:.1f}% ({votes_c:,})\n")
        #print in terminal
        print(county_result)
        # save the county result to text file
        txt_file.write(county_result)

        # Determine largest county turnout using if function
        if (votes_c > largest_count) and (vote_percentage_c > largest_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            largest_count = votes_c
            largest_percentage = vote_percentage_c
            # Set the winning_candidate equal to the candidate's name.
            largest_county = county
    
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
          
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate     

    # The winner of the election based on popular vote
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)