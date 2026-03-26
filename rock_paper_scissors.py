import random
import os

CHOICES = ['rock', 'paper', 'scissors']
EMOJIS = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
WIN_MESSAGES = ['You win! 🎉', 'Computer wins! 😔', "It's a tie! 🤝"]


def get_player_choice():
    print("\n╔══════════════════════════════╗")
    print("║   ROCK PAPER SCISSORS        ║")
    print("╠══════════════════════════════╣")
    print("║  1. Rock                     ║")
    print("║  2. Paper                    ║")
    print("║  3. Scissors                ║")
    print("║  0. Quit                    ║")
    print("╚══════════════════════════════╝")
    
    while True:
        choice = input("\nEnter your choice (1/2/3/0): ").strip()
        if choice == '0':
            return None
        if choice in ['1', '2', '3']:
            return CHOICES[int(choice) - 1]
        print("Invalid choice. Please try again.")


def determine_winner(player, computer):
    if player == computer:
        return 2
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return 0
    return 1


def play_round(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    player_choice = get_player_choice()
    if player_choice is None:
        return False

    computer_choice = random.choice(CHOICES)

    print(f"\n  You:   {EMOJIS[player_choice]} {player_choice.upper()}")
    print(f"  PC:    {EMOJIS[computer_choice]} {computer_choice.upper()}")

    result = determine_winner(player_choice, computer_choice)
    print(f"\n  ➜ {WIN_MESSAGES[result]}")

    if result == 0:
        score['wins'] += 1
    elif result == 1:
        score['losses'] += 1
    else:
        score['ties'] += 1

    return True


def main():
    score = {'wins': 0, 'losses': 0, 'ties': 0}

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "═" * 40)
        print("      ROCK PAPER SCISSORS GAME")
        print("═" * 40)
        print(f"\n   Score: Wins: {score['wins']} | Losses: {score['losses']} | Ties: {score['ties']}")
        
        if not play_round(score):
            break

        print(f"\n   Current: Wins: {score['wins']} | Losses: {score['losses']} | Ties: {score['ties']}")
        
        again = input("\n   Play again? (y/n): ").strip().lower()
        if again != 'y':
            break

    print("\n" + "=" * 40)
    print("       FINAL SCORE")
    print("=" * 40)
    print(f"\n   🏆 Wins:    {score['wins']}")
    print(f"   💔 Losses:  {score['losses']}")
    print(f"   🤝 Ties:    {score['ties']}")
    print("\n   Thanks for playing! Goodbye! 👋\n")


if __name__ == '__main__':
    main()
