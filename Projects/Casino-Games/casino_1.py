# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        self.credits = 1000
        self.player_name = ""

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Casino Game!").pack(pady=10)
        tk.Button(self.root, text="Start Game", command=self.create_profile_screen).pack(pady=5)
        tk.Button(self.root, text="Credits", command=self.create_credits_screen).pack(pady=5)
        tk.Button(self.root, text="Copyright", command=self.create_copyright_screen).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def create_profile_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter Your Name:").pack(pady=10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        tk.Button(self.root, text="Save and Continue", command=self.save_profile).pack(pady=5)

    def save_profile(self):
        self.player_name = self.name_entry.get()
        if self.player_name:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Please enter your name.")

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome, {self.player_name}!").pack(pady=10)
        self.credit_label = tk.Label(self.root, text=f"Credits: {self.credits}")
        self.credit_label.pack(pady=5)
        tk.Button(self.root, text="Play Slot Machine", command=self.play_slot_machine).pack(pady=5)
        tk.Button(self.root, text="Play Blackjack", command=self.play_blackjack).pack(pady=5)
        tk.Button(self.root, text="Play Roulette", command=self.play_roulette).pack(pady=5)
        tk.Button(self.root, text="Back to Start Screen", command=self.create_start_screen).pack(pady=5)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)
        self.reel_labels = [tk.Label(self.root, text="") for _ in range(3)]
        for label in self.reel_labels:
            label.pack()

    def create_credits_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Credits").pack(pady=10)
        tk.Label(self.root, text="Developed by Your Name").pack(pady=5)
        tk.Label(self.root, text="Music by Artist Name").pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_start_screen).pack(pady=5)

    def create_copyright_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Copyright Information").pack(pady=10)
        tk.Label(self.root, text="\u00A9 2024 Kyle Powell. All rights reserved.").pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_start_screen).pack(pady=5)

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

    def draw_card(self, deck):
        card = random.choice(deck)
        deck.remove(card)
        return card

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
