from colorama import Fore, Style, init

# Required on Windows to enable ANSI codes
init(autoreset=True)

import random

# List of all 50 US states
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# Create a dictionary to store the state and its status (default is not destroyed)
state_grid = {state: " " for state in us_states}

# Function to print the grid in a readable format
def print_grid(grid):
    print("\n--- Current State Grid ---")
    count = 0
    for state, status in grid.items():
        # Color code based on status
        if status == "X":
            display = Fore.RED + "X" + Style.RESET_ALL
        else:
            display = Fore.GREEN + "_" + Style.RESET_ALL

        print(f"{state[:10]:<12}: {display}", end="  ")
        count += 1
        if count % 3 == 0:
            print()
    print("\n")

state_grid = {state: " " for state in us_states}
state_grid["Texas"] = "X"
state_grid["California"] = "X"

print_grid(state_grid)


# Main loop
while True:
    # Get a list of remaining states that haven't been destroyed yet
    remaining_states = [state for state, status in state_grid.items() if status == " "]
    
    # Break loop if all states have been processed
    if not remaining_states:
        print("All states have been judged. The doomsday device rests... for now.")
        break

    # Pick a random state to judge
    selected_state = random.choice(remaining_states)
    
    # Ask the user for input
    user_input = input(f"Do you wish to DESTROY {selected_state}? (y = destroy, n = spare, q = quit): ").lower()
    
    if user_input == 'y':
        state_grid[selected_state] = "X"  # Mark as destroyed
        print(f"{selected_state} has been DESTROYED!\n")
    elif user_input == 'n':
        print(f"{selected_state} has been spared... for now.\n")
    elif user_input == 'q':
        print("Doomsday device shutting down early. The world breathes easy... for now.")
        break
    else:
        print("Invalid input. Please enter 'y', 'n', or 'q'.")
        continue  # Skip printing grid if invalid input

    # Show current grid after each decision
    print_grid(state_grid)