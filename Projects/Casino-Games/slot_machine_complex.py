import random

# Define the symbols for the slot machine
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]

# Payout rules based on the combination of symbols
payouts = {
    ("Cherry", "Cherry", "Cherry"): 100,
    ("Lemon", "Lemon", "Lemon"): 50,
    ("Orange", "Orange", "Orange"): 40,
    ("Plum", "Plum", "Plum"): 30,
    ("Bell", "Bell", "Bell"): 200,
    ("Bar", "Bar", "Bar"): 300,
    ("Cherry", "Cherry", "Bar"): 20,
    ("Lemon", "Lemon", "Bar"): 10,
    ("Orange", "Orange", "Bar"): 10,
    ("Plum", "Plum", "Bar"): 10,
    ("Bell", "Bell", "Bar"): 50,
}

# Function to spin the reels
def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

# Function to check for a win and calculate payout
def check_win(reels):
    combination = tuple(reels)
    return payouts.get(combination, 0)

# Function to play the slot machine
def play_slot_machine():
    reels = spin_reels()
    print("Spinning the reels...")
    print(" | ".join(reels))
    
    payout = check_win(reels)
    if payout > 0:
        print(f"Congratulations! You won {payout} credits!")
    else:
        print("Sorry, better luck next time.")

# Main game loop
def main():
    credits = 1000  # Initial credits
    while credits > 0:
        print(f"Current credits: {credits}")
        bet = int(input("Enter your bet: "))
        if bet > credits:
            print("You don't have enough credits to place that bet.")
            continue
        
        play_slot_machine()
        payout = check_win(spin_reels())
        credits += payout - bet
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    if credits <= 0:
        print("You are out of credits! Game over.")

if __name__ == "__main__":
    main()
