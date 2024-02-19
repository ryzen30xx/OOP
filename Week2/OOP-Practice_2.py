import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.games_played = 0
        self.results_history = []

    def get_player_choice(self):
        while True:
            player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
            if player_choice in self.choices:
                return player_choice
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'paper' and computer_choice == 'rock') or
            (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def display_scores(self):
        print(f"Player Score: {self.player_score} | Computer Score: {self.computer_score}")

    def play_game(self):
        while self.games_played < 5:
            player_choice = self.get_player_choice()
            computer_choice = self.get_computer_choice()

            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            result = self.determine_winner(player_choice, computer_choice)
            print(result)

            self.results_history.append(result)

            self.display_scores()

            self.games_played += 1

            if self.games_played == 5:
                self.display_summary()

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break

    def display_summary(self):
        print("\nGame Summary:")
        for result in self.results_history:
            print(result)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()


# 