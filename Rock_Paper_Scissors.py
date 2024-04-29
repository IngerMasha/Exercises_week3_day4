from game import Game
def get_user_menu_choice():
   print("Menu:\n(g) Play a new game\n(x) Show scores and exit.")
   choise = input("Enter: ")
   return choise



def print_result(my_game):
    print(f"You played {my_game.games_amount} total.")
    print("Game Results:")
    for game in my_game.games_results:
        print(f"User: {game['user']} | Computer: {game['comp']} | Result: {game['result']}")


def main():
    my_game = Game()
    while get_user_menu_choice() == 'g':
        my_game.play()
    print_result(my_game)


if __name__=="__main__":
    main()