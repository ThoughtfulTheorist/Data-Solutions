import random

# Define the symbols for the slot machine with their respective probabilities
symbols = {
    "Cherry": 0.3,
    "Lemon": 0.2,
    "Orange": 0.2,
    "Plum": 0.1,
    "Bell": 0.1,
    "Bar": 0.05,
    "Seven": 0.05  # Special symbol for jackpot
}

# Function to spin the reels with weighted probabilities
def spin_reels():
    reels = []
    for _ in range(3):
        symbol = random.choices(list(symbols.keys()), weights=list(symbols.values()))[0]
        reels.append(symbol)
    return reels

# Payout rules based on the combination of symbols
payouts = {
    ("Cherry", "Cherry", "Cherry"): 100,
    ("Lemon", "Lemon", "Lemon"): 50,
    ("Orange", "Orange", "Orange"): 40,
    ("Plum", "Plum", "Plum"): 30,
    ("Bell", "Bell", "Bell"): 200,
    ("Bar", "Bar", "Bar"): 300,
    ("Seven", "Seven", "Seven"): 1000,  # Jackpot
    ("Cherry", "Cherry", "Bar"): 20,
    ("Lemon", "Lemon", "Bar"): 10,
    ("Orange", "Orange", "Bar"): 10,
    ("Plum", "Plum", "Bar"): 10,
    ("Bell", "Bell", "Bar"): 50,
}

# Function to check for a win and calculate payout
def check_win(reels):
    combination = tuple(reels)
    return payouts.get(combination, 0)

# Function to play the slot machine
def play_slot_machine(bet):
    reels = spin_reels()
    print("Spinning the reels...")
    print(" | ".join(reels))
    
    payout = check_win(reels)
    if payout > 0:
        print(f"Congratulations! You won {payout} credits!")
        return payout
    else:
        print("Sorry, better luck next time.")
        return 0

# Main game loop
def main():
    credits = 1000  # Initial credits
    while credits > 0:
        print(f"Current credits: {credits}")
        bet = int(input("Enter your bet: "))
        if bet > credits:
            print("You don't have enough credits to place that bet.")
            continue
        
        payout = play_slot_machine(bet)
        credits += payout - bet
        
        if payout >= 1000:  # Trigger bonus round if jackpot is hit
            print("Jackpot! You've won a bonus round!")
            bonus_credits = random.randint(100, 500)
            print(f"You won an additional {bonus_credits} credits in the bonus round!")
            credits += bonus_credits
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    if credits <= 0:
        print("You are out of credits! Game over.")

if __name__ == "__main__":
    main()
