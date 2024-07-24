import tkinter as tk
from random import randint

class CowsAndBulls:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cows and Bulls")
        self.window.geometry("300x300")

        self.rounds_label = tk.Label(self.window, text="Enter the number of rounds:")
        self.rounds_label.pack()

        self.rounds_entry = tk.Entry(self.window, width=10)
        self.rounds_entry.pack()

        self.start_button = tk.Button(self.window, text="Start", command=self.start_game)
        self.start_button.pack()

        self.guess_label = tk.Label(self.window, text="")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.window, width=10)
        self.guess_entry.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.round_label = tk.Label(self.window, text="Rounds: 0")
        self.round_label.pack()

        self.guess_button = tk.Button(self.window, text="Guess", command=self.check_guess, state="disabled")
        self.guess_button.pack()

        self.window.mainloop()

    def start_game(self):
        self.rounds = int(self.rounds_entry.get())
        self.number_to_guess = str(randint(1000, 9999))
        self.guesses = 0
        self.guess_label.config(text="Enter your 4-digit guess:")
        self.guess_button.config(state="normal")
        self.start_button.config(state="disabled")

    def check_guess(self):
        guess = self.guess_entry.get()
        if len(guess) != 4 or not guess.isdigit():
            self.result_label.config(text="Invalid guess. Please enter a 4-digit number.")
            return

        cows = 0
        bulls = 0
        for i in range(4):
            if guess[i] == self.number_to_guess[i]:
                cows += 1
            elif guess[i] in self.number_to_guess:
                bulls += 1

        self.guesses += 1
        self.round_label.config(text=f"Rounds: {self.guesses}/{self.rounds}")

        if cows == 4:
            self.result_label.config(text=f"Congratulations! You guessed the number in {self.guesses} guesses.\nThe secret code was: {self.number_to_guess}")
            self.guess_button.config(state="disabled")
        elif self.guesses == self.rounds:
            self.result_label.config(text=f"Game over! You didn't guess the number in {self.rounds} rounds.\nThe secret code was: {self.number_to_guess}")
            self.guess_button.config(state="disabled")
        else:
            self.result_label.config(text=f"{cows} cows, {bulls} bulls. Try again!")

if __name__ == "__main__":
    game = CowsAndBulls()
