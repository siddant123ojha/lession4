import random
from colorama import init, Fore, Style

init(autoreset=True)

def displayboard(board):
    print()
    print(' ' + formatsymbol(board[0]) + ' | ' + formatsymbol(board[1]) + ' | ' + formatsymbol(board[2]))
    print(Fore.CYAN + '-----------')
    print(' ' + formatsymbol(board[3]) + ' | ' + formatsymbol(board[4]) + ' | ' + formatsymbol(board[5]))
    print(Fore.CYAN + '-----------')
    print(' ' + formatsymbol(board[6]) + ' | ' + formatsymbol(board[7]) + ' | ' + formatsymbol(board[8]))
    print()

def formatsymbol(symbol):
    if symbol == 'X':
        return Fore.RED + symbol
    elif symbol == 'O':
        return Fore.GREEN + symbol
    else:
        return Fore.YELLOW + symbol

def playerchoice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O?: ").upper()
    return (symbol, 'O' if symbol == 'X' else 'X')

def player_move(board, symbol, playername):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input(Fore.GREEN + f"{playername}, Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print(Fore.RED + "Invalid move. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a number between 1 and 9.")
    board[move - 1] = symbol

def botmove(board, botsymbol, playersymbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = botsymbol
            if checkwin(board_copy, botsymbol):
                board[i] = botsymbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = playersymbol
            if checkwin(board_copy, playersymbol):
                board[i] = botsymbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = botsymbol

def checkwin(board, symbol):
    winconditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in winconditions)

def checkfull(board):
    return all(not spot.isdigit() for spot in board)

def tictactoe():
    print(Fore.YELLOW + "Welcome to Tic-Tac-Toe!")
    playername = input(Fore.GREEN + "Please enter your name: ")
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        playersymbol, botsymbol = playerchoice()
        turn = "Player"
        gameon = True

        while gameon:
            displayboard(board)
            if turn == "Player":
                player_move(board, playersymbol, playername)
                if checkwin(board, playersymbol):
                    displayboard(board)
                    print(Fore.GREEN + f"Congratulations, {playername}, you won!")
                    gameon = False
                elif checkfull(board):
                    displayboard(board)
                    print(Fore.YELLOW + "It's a tie!")
                    gameon = False
                else:
                    turn = "Bot"
            else:
                print(Fore.RED + "The Bot is making its move... (Choose your next move wisely!)")
                botmove(board, botsymbol, playersymbol)
                if checkwin(board, botsymbol):
                    displayboard(board)
                    print(Fore.RED + "AI has won the game.")
                    print(Fore.WHITE + "(Told you to choose your next move wisely!)")
                    gameon = False
                elif checkfull(board):
                    displayboard(board)
                    print(Fore.YELLOW + "It's a tie!")
                    gameon = False
                else:
                    turn = "Player"

        playagain = input(Fore.GREEN + f"{playername}, do you want to play again against the bot? (yes/no): ").lower()
        if playagain != "yes":
            print(Fore.CYAN + "Thank you for playing!")
            break

if __name__ == "__main__":
    tictactoe()
