# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  # For handling images
import os

# Define symbols and their probabilities for the slot machine
symbols = {
    "Cherry": 0.3,
    "Lemon": 0.2,
    "Orange": 0.2,
    "Plum": 0.1,
    "Bell": 0.1,
    "Bar": 0.05,
    "Seven": 0.05  # Special symbol for jackpot
}

# Payout rules for the slot machine
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

class CasinoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino Game")
        self.root.geometry("800x600")

        # Load background image
        self.background_image = Image.open("background.jpeg")
        self.background_image = self.background_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        self.credits = 1000
        self.player_name = ""

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()

        # Add background
        background_label = tk.Label(self.root, image=self.bg_image)
        background_label.place(relwidth=1, relheight=1)

        # Create a frame for the text and buttons
        frame = tk.Frame(self.root, bg="black", bd=5)
        frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")

        tk.Label(frame, text="Welcome to the Casino Game!", font=("Helvetica", 24), bg="black", fg="gold").pack(pady=10)
        tk.Button(frame, text="Start Game", font=("Helvetica", 18), bg="red", fg="white", command=self.create_profile_screen).pack(pady=5)
        tk.Button(frame, text="Credits", font=("Helvetica", 18), bg="blue", fg="white", command=self.create_credits_screen).pack(pady=5)
        tk.Button(frame, text="Copyright", font=("Helvetica", 18), bg="green", fg="white", command=self.create_copyright_screen).pack(pady=5)
        tk.Button(frame, text="Exit", font=("Helvetica", 18), bg="purple", fg="white", command=self.root.quit).pack(pady=5)

    def create_profile_screen(self):
        self.clear_screen()

        # Add background
        background_label = tk.Label(self.root, image=self.bg_image)
        background_label.place(relwidth=1, relheight=1)

        # Create a frame for the text and buttons
        frame = tk.Frame(self.root, bg="black", bd=5)
        frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")

        tk.Label(frame, text="Enter Your Name:", font=("Helvetica", 18), bg="black", fg="gold").pack(pady=10)
        self.name_entry = tk.Entry(frame, font=("Helvetica", 18))
        self.name_entry.pack(pady=5)
        tk.Button(frame, text="Save and Continue", font=("Helvetica", 18), bg="red", fg="white", command=self.save_profile).pack(pady=5)

    def save_profile(self):
        self.player_name = self.name_entry.get()
        if self.player_name:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Please enter your name.")

    def create_main_menu(self):
        self.clear_screen()

        # Add background
        background_label = tk.Label(self.root, image=self.bg_image)
        background_label.place(relwidth=1, relheight=1)

        # Create a frame for the text and buttons
        frame = tk.Frame(self.root, bg="black", bd=5)
        frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")

        tk.Label(frame, text=f"Welcome, {self.player_name}!", font=("Helvetica", 24), bg="black", fg="gold").pack(pady=10)
        self.credit_label = tk.Label(frame, text=f"Credits: {self.credits}", font=("Helvetica", 18), bg="black", fg="white")
        self.credit_label.pack(pady=5)
        tk.Button(frame, text="Play Slot Machine", font=("Helvetica", 18), bg="red", fg="white", command=self.play_slot_machine).pack(pady=5)
        tk.Button(frame, text="Play Blackjack", font=("Helvetica", 18), bg="blue", fg="white", command=self.play_blackjack).pack(pady=5)
        tk.Button(frame, text="Play Roulette", font=("Helvetica", 18), bg="green", fg="white", command=self.play_roulette).pack(pady=5)
        tk.Button(frame, text="Play Texas Hold'em Poker", font=("Helvetica", 18), bg="purple", fg="white", command=self.play_poker).pack(pady=5)
        tk.Button(frame, text="Play Craps", font=("Helvetica", 18), bg="orange", fg="white", command=self.play_craps).pack(pady=5)
        tk.Button(frame, text="Bet on Horse Race", font=("Helvetica", 18), bg="brown", fg="white", command=self.play_horse_race).pack(pady=5)
        tk.Button(frame, text="Back to Start Screen", font=("Helvetica", 18), bg="pink", fg="white", command=self.create_start_screen).pack(pady=5)
        self.result_label = tk.Label(frame, text="", font=("Helvetica", 18), bg="black", fg="white")
        self.result_label.pack(pady=5)
        self.reel_labels = [tk.Label(frame, text="", font=("Helvetica", 18), bg="black", fg="white") for _ in range(3)]
        for label in self.reel_labels:
            label.pack()

    def create_credits_screen(self):
        self.clear_screen()

        # Add background
        background_label = tk.Label(self.root, image=self.bg_image)
        background_label.place(relwidth=1, relheight=1)

        # Create a frame for the text and buttons
        frame = tk.Frame(self.root, bg="black", bd=5)
        frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")

        tk.Label(frame, text="Credits", font=("Helvetica", 24), bg="black", fg="gold").pack(pady=10)
        tk.Label(frame, text="Developed by Kyle Powell | AI, ML, BI", font=("Helvetica", 18), bg="black", fg="white").pack(pady=5)
        tk.Label(frame, text="Designed Joel Haris | GUI and Front End", font=("Helvetica", 18), bg="black", fg="white").pack(pady=5)
        tk.Label(frame, text="Music by Various Artists", font=("Helvetica", 18), bg="black", fg="white").pack(pady=5)
        tk.Button(frame, text="Back", font=("Helvetica", 18), bg="red", fg="white", command=self.create_start_screen).pack(pady=5)

    def create_copyright_screen(self):
        self.clear_screen()

        # Add background
        background_label = tk.Label(self.root, image=self.bg_image)
        background_label.place(relwidth=1, relheight=1)

        # Create a frame for the text and buttons
        frame = tk.Frame(self.root, bg="black", bd=5)
        frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")

        tk.Label(frame, text="Copyright Information", font=("Helvetica", 24), bg="black", fg="gold").pack(pady=10)
        tk.Label(frame, text="\u00A9 2024 Kyle Powell. All rights reserved.", font=("Helvetica", 18), bg="black", fg="white").pack(pady=5)
        tk.Button(frame, text="Back", font=("Helvetica", 18), bg="red", fg="white", command=self.create_start_screen).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def play_slot_machine(self):
        bet = simpledialog.askinteger("Input", "Enter your bet per payline:")
        paylines = simpledialog.askinteger("Input", "Enter the number of paylines (1-3):")
        if bet * paylines > self.credits:
            messagebox.showerror("Error", "You don't have enough credits to place that bet.")
            return
        
        total_payout = 0
        results = []
        
        for line in range(paylines):
            reels = self.spin_reels()
            results.append(reels)
            payout = self.check_win(reels, bet)
            total_payout += payout
        
        self.credits += total_payout - (bet * paylines)
        self.credit_label.config(text=f"Credits: {self.credits}")
        self.result_label.config(text="Spinning the reels...")
        
        for i, reels in enumerate(results):
            self.reel_labels[i].config(text=" | ".join(reels))
        
        if total_payout > 0:
            self.result_label.config(text=f"Congratulations! Total win: {total_payout} credits!")
        else:
            self.result_label.config(text="Sorry, better luck next time.")
            
        if self.credits <= 0:
            messagebox.showinfo("Game Over", "You are out of credits! Game over.")
            self.root.quit()

    def play_blackjack(self):
        bet = simpledialog.askinteger("Input", "Enter your bet:")
        if bet > self.credits:
            messagebox.showerror("Error", "You don't have enough credits to place that bet.")
            return
        
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        player_hand = [self.draw_card(deck), self.draw_card(deck)]
        dealer_hand = [self.draw_card(deck), self.draw_card(deck)]

        player_total = self.calculate_hand(player_hand)
        dealer_total = self.calculate_hand(dealer_hand)

        while player_total < 21:
            action = simpledialog.askstring("Input", f"Your cards: {player_hand}, total: {player_total}\nDealer's showing: {dealer_hand[0]}\nDo you want to (h)it or (s)tand?")
            if action == 'h':
                player_hand.append(self.draw_card(deck))
                player_total = self.calculate_hand(player_hand)
            else:
                break

        while dealer_total < 17:
            dealer_hand.append(self.draw_card(deck))
            dealer_total = self.calculate_hand(dealer_hand)

        messagebox.showinfo("Result", f"Dealer's cards: {dealer_hand}, total: {dealer_total}")

        if player_total > 21:
            self.result_label.config(text="You busted! Dealer wins.")
            self.credits -= bet
        elif dealer_total > 21 or player_total > dealer_total:
            self.result_label.config(text="You win!")
            self.credits += bet
        elif player_total == dealer_total:
            self.result_label.config(text="It's a tie!")
        else:
            self.result_label.config(text="Dealer wins.")
            self.credits -= bet
        
        self.credit_label.config(text=f"Credits: {self.credits}")
        if self.credits <= 0:
            messagebox.showinfo("Game Over", "You are out of credits! Game over.")
            self.root.quit()

    def play_roulette(self):
        bet = simpledialog.askinteger("Input", "Enter your bet:")
        if bet > self.credits:
            messagebox.showerror("Error", "You don't have enough credits to place that bet.")
            return
        
        bet_type = simpledialog.askstring("Input", "Place your bet on (n)umber, (r)ed, (b)lack, (o)dd, (e)ven:")
        winning_number = random.randint(0, 36)
        winning_color = "red" if winning_number % 2 == 1 else "black"

        if bet_type == 'n':
            chosen_number = simpledialog.askinteger("Input", "Choose a number between 0 and 36:")
            if chosen_number == winning_number:
                self.result_label.config(text=f"The winning number is {winning_number}. You win!")
                self.credits += bet * 35
            else:
                self.result_label.config(text=f"The winning number is {winning_number}. You lose.")
                self.credits -= bet
        elif bet_type == 'r':
            if winning_color == "red":
                self.result_label.config(text=f"The winning color is {winning_color}. You win!")
                self.credits += bet
            else:
                self.result_label.config(text=f"The winning color is {winning_color}. You lose.")
                self.credits -= bet
        elif bet_type == 'b':
            if winning_color == "black":
                self.result_label.config(text=f"The winning color is {winning_color}. You win!")
                self.credits += bet
            else:
                self.result_label.config(text=f"The winning color is {winning_color}. You lose.")
                self.credits -= bet
        elif bet_type == 'o':
            if winning_number % 2 == 1:
                self.result_label.config(text=f"The winning number is {winning_number}. You win!")
                self.credits += bet
            else:
                self.result_label.config(text=f"The winning number is {winning_number}. You lose.")
                self.credits -= bet
        elif bet_type == 'e':
            if winning_number % 2 == 0:
                self.result_label.config(text=f"The winning number is {winning_number}. You win!")
                self.credits += bet
            else:
                self.result_label.config(text=f"The winning number is {winning_number}. You lose.")
                self.credits -= bet

        self.credit_label.config(text=f"Credits: {self.credits}")
        if self.credits <= 0:
            messagebox.showinfo("Game Over", "You are out of credits! Game over.")
            self.root.quit()

    def play_poker(self):
        bet = simpledialog.askinteger("Input", "Enter your bet:")
        if bet > self.credits:
            messagebox.showerror("Error", "You don't have enough credits to place that bet.")
            return

        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)
        
        player_hand = [self.draw_card(deck), self.draw_card(deck)]
        dealer_hand = [self.draw_card(deck), self.draw_card(deck)]
        community_cards = [self.draw_card(deck) for _ in range(5)]

        player_best_hand = self.get_best_hand(player_hand + community_cards)
        dealer_best_hand = self.get_best_hand(dealer_hand + community_cards)

        player_hand_str = f"Your hand: {player_hand}, community cards: {community_cards}, best hand: {player_best_hand}"
        dealer_hand_str = f"Dealer's hand: {dealer_hand}, community cards: {community_cards}, best hand: {dealer_best_hand}"

        messagebox.showinfo("Poker Result", f"{player_hand_str}\n{dealer_hand_str}")

        if self.compare_hands(player_best_hand, dealer_best_hand):
            self.result_label.config(text="You win!")
            self.credits += bet
        else:
            self.result_label.config(text="Dealer wins.")
            self.credits -= bet
        
        self.credit_label.config(text=f"Credits: {self.credits}")
        if self.credits <= 0:
            messagebox.showinfo("Game Over", "You are out of credits! Game over.")
            self.root.quit()

    def play_craps(self):
        bet = simpledialog.askinteger("Input", "Enter your bet:")
        if bet > self.credits:
            messagebox.showerror("Error", "You don't have enough credits to place that bet.")
            return

        # First roll
        roll = self.roll_dice()
        self.result_label.config(text=f"First roll: {roll}")

        if roll in [7, 11]:
            self.result_label.config(text="You win!")
            self.credits += bet
        elif roll in [2, 3, 12]:
            self.result_label.config(text="Craps! You lose.")
            self.credits -= bet
        else:
            point = roll
            self.result_label.config(text=f"Point is set to: {point}")
            roll = 0
            while roll != point and roll != 7:
                roll = self.roll_dice()
                self.result_label.config(text=f"Roll: {roll}")
                if roll == point:
                    self.result_label.config(text="You hit your point! You win!")
                    self.credits += bet
                elif roll == 7:
                    self.result_label.config(text="Seven out! You lose.")
                    self.credits -= bet
        
        self.credit_label.config(text=f"Credits: {self.credits}")
        if self.credits <= 0:
            messagebox.showinfo("Game Over", "You are out of credits! Game over.")
            self.root.quit()

    def play_horse_race(self):
        bet = simpledialog.askinteger("Input", "Enter your bet:")
        if bet > self.credits:
            messagebox.showerror("Error", "You don't have enough credits to place that bet.")
            return
        
        horses = ["Horse 1", "Horse 2", "Horse 3", "Horse 4"]
        chosen_horse = simpledialog.askstring("Input", f"Choose your horse ({', '.join(horses)}):")
        if chosen_horse not in horses:
            messagebox.showerror("Error", "Invalid horse.")
            return
        
        winning_horse = random.choice(horses)
        self.result_label.config(text=f"The winning horse is: {winning_horse}")
        
        if chosen_horse == winning_horse:
            self.result_label.config(text="Your horse wins! You win!")
            self.credits += bet * 4  # 4:1 payout
        else:
            self.result_label.config(text="Your horse loses.")
            self.credits -= bet
        
        self.credit_label.config(text=f"Credits: {self.credits}")
        if self.credits <= 0:
            messagebox.showinfo("Game Over", "You are out of credits! Game over.")
            self.root.quit()

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def draw_card(self, deck):
        return deck.pop()

    def calculate_hand(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card == 'A':
                aces += 1
            elif card in ['K', 'Q', 'J']:
                value += 10
            else:
                value += int(card)
        for _ in range(aces):
            if value + 11 > 21:
                value += 1
            else:
                value += 11
        return value

    def get_best_hand(self, cards):
        # Simplified: just return the sorted cards (actual hand evaluation is complex)
        return sorted(cards, reverse=True)[:5]

    def compare_hands(self, hand1, hand2):
        # Simplified: just compare the highest cards (actual hand evaluation is complex)
        return hand1 > hand2

    def spin_reels(self):
        reels = []
        for _ in range(3):
            symbol = random.choices(list(symbols.keys()), weights=list(symbols.values()))[0]
            reels.append(symbol)
        return reels

    def check_win(self, reels, bet):
        combination = tuple(reels)
        return payouts.get(combination, 0) * bet

if __name__ == "__main__":
    root = tk.Tk()
    app = CasinoGame(root)
    root.mainloop()
