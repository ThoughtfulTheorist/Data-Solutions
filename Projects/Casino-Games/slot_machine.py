
import random

# Define the symbols for the slot machine
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]

# Function to spin the reels
def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

# Function to check for a win
def check_win(reels):
    # If all three symbols are the same, it's a win
    if reels[0] == reels[1] == reels[2]:
        return True
    return False

# Function to play the slot machine
def play_slot_machine():
    reels = spin_reels()
    print("Spinning the reels...")
    print(" | ".join(reels))
    
    if check_win(reels):
        print("Congratulations! You won!")
    else:
        print("Sorry, better luck next time.")

# Main game loop
def main():
    while True:
        play_slot_machine()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
