import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0])== len(l) and l[0] != 0:
            return True
        else:
            return False

    #Horizontal
    for row in current_game:
        print(row)
        if all_same(row):
            print(f"Player{row[0]} is the winner horizontally!")
            return True

    #Diagonal        
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
            print(f"Player{diags[0]} is the winner diagonally (/)!")
            return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player{diags[0]} is the winner diagonally (\\)!")
        return True

    #Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player{check[0]} is the winner vertically!")
            return True

    return False


def game_board(current_game, player=0, row=0, column=0, just_display=False):
    try:
        if current_game[row][column] !=0:
            print("This position is already occupied. Please choose another!")
            return current_game, False
        #List Comprehension. Need clarity
        print("   "+"  ".join([str(i) for i in range(len(current_game))]))
        if not just_display:
            current_game[row][column]=player
        for count,row in enumerate(current_game):
            print(count, row)
        return current_game, True
    except IndexError as e:
        print("Error: There seems to be a problem with row or column index!!!", str(e))
        return current_game, False     
    
    except Exception as e:
        print("Error: Catch All Exception!!!", str(e))
        return current_game, False

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_size = int(input("What size game of Tic Tac Toe do you want to play? "))
    game=[[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    #player_cycle = itertools.cycle(random.shuffle([1, 2]))
    #player_cycle = itertools.cycle([1, 2])
    player_cycle = itertools.cycle(players)
    game, _ = game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        print(f"Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            game, played = game_board(game,player=current_player,row=row_choice,column=column_choice)

        if win(game):
            game_won = True
            play_again = input("The game is over. Would you like to play again? (y/n)")
            if play_again.lower() == "y":
                print("restarting.....")
            elif play_again.lower() == "n":
                print("Bye Bye")
                play = False
            else:
                print("Not a valid entry. Bye Bye")
                play = False

