import matplotlib.pyplot as plt

class Voter:
    def __init__(self, id, name, surname, choice, location):
        self.id = id
        self.name = name
        self.surname = surname
        self.choice = choice
        self.location = location

    def __str__(self):
        return f"{self.id}, {self.name}, {self.surname}, {self.choice}, {self.location}"

voters = []

# Function to check if a voter has already voted
def has_voted(voter_id):
    for voter in voters:
        if voter.id == voter_id:
            return True
    return False

# Function to end the election and display the results
def end_election():
    # Save the voter information to a text file
    with open("voter_info.txt", "w") as f:
        for voter in voters:
            f.write(str(voter) + "\n")
    
    # Create a bar chart of the election results for each location
    choices = ["Python ittifakı", "Java ittifakı"]
    locations = ["x", "y", "z", "t"]
    choice_counts_by_location = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for voter in voters:
        choice = voter.choice
        location = voter.location
        if choice == "a":
            choice_counts_by_location[locations.index(location)][0] += 1
        elif choice == "b":
            choice_counts_by_location[locations.index(location)][1] += 1
    
    total_votes = len(voters)
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    for i in range(len(locations)):
        row = i // 2
        col = i % 2
        axs[row, col].bar(choices, choice_counts_by_location[i])
        axs[row, col].set_title(f"Election Results for Location {locations[i]}")
        axs[row, col].set_xlabel("Party")
        axs[row, col].set_ylabel("Votes")
    plt.suptitle(f"Election Results by Location (Total Votes: {total_votes})", fontsize=16)
    plt.tight_layout()
    plt.show()

# Main loop to accept voter inputs
while True:
    # Get voter information
    voter_id = input("Enter your ID: ")
    voter_name = input("Enter your name: ")
    voter_surname = input("Enter your surname: ")
    voter_choice = input("Enter your choice (a for Python ittifakı, b for Java ittifakı): ")
    voter_location = input("Enter your location (x, y, z, or t): ")
    
    # Check if the voter has already voted
    if has_voted(voter_id):
        print("You have already voted. Your vote will not be counted.")
    else:
        # Add the voter to the list of voters
        voter = Voter(voter_id, voter_name, voter_surname, voter_choice, voter_location)
        voters.append(voter)
        print("Thank you for voting!")
    
    # Check if the election should end
    end_input = input("Enter q to end the election: ")
    if end_input.lower() == "q":
        end_election()
        break
