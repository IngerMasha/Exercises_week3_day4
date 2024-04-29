import random

class Game:
    def __init__(self):
        self.games_amount = 0
        self.games_results = []
        self.game_rules = {
            'rock': {'rock': 'draw', 'paper': 'loss', 'scissors': 'win'},
            'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'loss'},
            'scissors': {'rock': 'loss', 'paper': 'win', 'scissors': 'draw'}
        }
        self.move_mappings = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    def get_users_item(self):
        while True:
            print("Enter your move: 'r' for rock, 'p' for paper, 's' for scissors.")
            user_input = input("Move: ").strip().lower()
            if user_input in ['r', 'p', 's']:
                return self.move_mappings[user_input]
            else:
                print("Invalid input! Please enter 'r' for rock, 'p' for paper, or 's' for scissors.")

    def get_computer_item(self):
        computer_move = random.choice(['rock', 'paper', 'scissors'])
        return computer_move

    def get_game_result(self, user_item, computer_item):
        result = self.game_rules[user_item][computer_item]
        self.games_amount += 1
        return result

    def play(self):
        user_move = self.get_users_item()
        computer_move = self.get_computer_item()
        game_result = self.get_game_result(user_move, computer_move)
        print(f"You selected {user_move}.\nComputer selected {computer_move}")
        print(f"You {game_result}")
        self.games_results.append({'user': user_move, 'comp': computer_move, 'result': game_result})

