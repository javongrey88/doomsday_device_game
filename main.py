from colorama import Fore, Style, init
import random

# Initialize colorama for colored output (cross-platform)
init(autoreset=True)

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

# Track the status of each state (spared or destroyed)
state_grid = {state: " " for state in us_states}

# Store decision history
history_log = []

# Display grid with colored markers for state status
def print_grid(grid):
    print("\n--- Current State Grid ---")
    count = 0
    for state, status in grid.items():
        if status == "X":
            display = Fore.RED + "X" + Style.RESET_ALL
        else:
            display = Fore.GREEN + "_" + Style.RESET_ALL

        print(f"{state[:10]:<12}: {display}", end="  ")
        count += 1
        if count % 3 == 0:
            print()
    print("\n")

# Display progress bar based on number of destroyed states
def print_progress_bar(destroyed, total=50, bar_length=30):
    percent = destroyed / total
    filled_length = int(bar_length * percent)

    # Red bar for destroyed, unfilled is plain
    bar = Fore.RED + "█" * filled_length + Style.RESET_ALL + "█" * (bar_length - filled_length)

    print(f"\nProgress: |{bar}| {destroyed}/{total} states destroyed\n")



# Print initial grid
print_grid(state_grid)

# Track turns for history log
turn = 1

# Main game loop
while True:
    # Get list of states that haven’t been judged
    remaining_states = [state for state, status in state_grid.items() if status == " "]

    if not remaining_states:
        print("All states have been judged. The doomsday device rests... for now.")
        break

    # Randomly select one remaining state
    selected_state = random.choice(remaining_states)

    # Prompt user for decision
    user_input = input(f"Do you wish to DESTROY {selected_state}? (y = destroy, n = spare, q = quit): ").lower()

    if user_input == 'y':
        state_grid[selected_state] = "X"
        entry = f"{turn}. {selected_state} - DESTROYED"
        history_log.append(entry)
        print(f"{entry}\n")
        turn += 1

    elif user_input == 'n':
        entry = f"{turn}. {selected_state} - SPARED"
        history_log.append(entry)
        print(f"{entry}\n")
        turn += 1

    elif user_input == 'q':
        print("Doomsday device shutting down early. The world breathes easy... for now.")
        break

    else:
        print("Invalid input. Please enter 'y', 'n', or 'q'.")
        continue  # Retry without printing grid

    # Display updated grid
    print_grid(state_grid)
    


    # Show updated progress
    destroyed_count = sum(1 for status in state_grid.values() if status == "X")
    print_progress_bar(destroyed_count)

# Print decision history after the loop ends
print("\n--- HISTORY LOG ---")
for entry in history_log:
    print(entry)
print(f"\nTotal Judgments: {len(history_log)}")

