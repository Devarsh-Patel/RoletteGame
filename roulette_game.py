import random

# Define the roulette wheel numbers and their colors
ROULETTE_NUMBERS = list(range(0, 37))
RED_NUMBERS = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
BLACK_NUMBERS = set(ROULETTE_NUMBERS) - RED_NUMBERS - {0}

class Player:
    """Represents a player in the roulette game."""
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.lose = 0

    def __str__(self):
        return f"{self.name}: Win={self.win}, Lose={self.lose}"

def spin_wheel():
    """Simulate spinning the roulette wheel."""
    number = random.choice(ROULETTE_NUMBERS)
    if number == 0:
        color = 'green'
    elif number in RED_NUMBERS:
        color = 'red'
    else:
        color = 'black'
    return number, color

def get_bet():
    """Randomly generate a bet for demonstration purposes."""
    bet_type = random.choice(['color', 'number', 'odd_even'])
    if bet_type == 'color':
        return ('color', random.choice(['red', 'black']))
    elif bet_type == 'number':
        return ('number', random.randint(0, 36))
    else:
        return ('odd_even', random.choice(['odd', 'even']))

def resolve_bet(bet, number, color):
    """Determine if the bet wins based on the spin result."""
    bet_type, bet_value = bet
    if bet_type == 'color':
        return color == bet_value
    elif bet_type == 'number':
        return number == bet_value
    elif bet_type == 'odd_even':
        if number == 0:
            return False
        return ('even' if number % 2 == 0 else 'odd') == bet_value
    return False

def main():
    # Create 6 players
    players = [Player(f"Player {i+1}") for i in range(6)]
    rounds = 25

    for round_num in range(1, rounds+1):
        print(f"\n--- Round {round_num} ---")
        number, color = spin_wheel()
        print(f"Roulette spun: {number} ({color})")

        for player in players:
            bet = get_bet()
            amount = random.randint(25, 500)  # Each bet between 25 and 500
            win = resolve_bet(bet, number, color)
            if win:
                player.win += amount
                print(f"{player.name} bet {bet} for {amount} and WON!")
            else:
                player.lose += amount
                print(f"{player.name} bet {bet} for {amount} and lost.")

    print("\n--- Final Results ---")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()