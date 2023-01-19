import os
import csv
import sys
import operator

# Output File 
stdoutOrigin=sys.stdout 
sys.stdout = open(os.path.join('Analysis','poll_results.txt'), "w")

# Input File 
csvpath = os.path.join('Resources','election_data.csv')
norm_path = os.path.normpath(csvpath)

# Variables 
total_votes = [ ]
candidates = [ ]
candidate_votes = { }
vote_count = 0

# Open Input File
with open(norm_path) as csvfile:

	csvreader = csv.reader(csvfile,delimiter=',')
	csvreader.__next__()
	csvreader = sorted(csvreader, key=operator.itemgetter(2))

	for row in csvreader:

		# Total of votes
		total_votes.append(row[2])
		
		# Candidates 
		if row[2] not in candidates:
			candidates.append(row[2])
			vote_count = 0

		# Votes per Candidate
		for candidate in candidates:
			if row[2] == candidate:
				vote_count+=1
				candidate_votes[candidate] = vote_count

# DRY method to print results
def printResults():
	print("------------------------------")
	print("Election Results")
	print("------------------------------")
	print(f"Total Votes: {len(total_votes)}")
	print("------------------------------")
	for candidate,votes in candidate_votes.items():
		print(f'{candidate}: {"%.3f"%(votes*100/len(total_votes))}% ({votes})')
	print("------------------------------")
	print(f'Winner: {max(candidate_votes, key=candidate_votes.get)}')
	print("------------------------------")

# Print results to Output File
printResults()
sys.stdout.close()

# Print results to Console
sys.stdout=stdoutOrigin
printResults()