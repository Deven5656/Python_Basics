""" @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to simulate Tic Tac Toe game
"""


board = ['-','-','-','-','-','-','-','-','-']   #Global List


def display_instruction():
    """
        Description :
            This function is used to display the instruction
        Parameters :
            none
        return :
            none
            
    """
    print(f"for a position enter value from 1-9")
    print(f"| 1 | 2 | 3 |")
    print(f"| 4 | 5 | 6 |")
    print(f"| 7 | 8 | 9 |\n")


def display_board():
    """
        Description :
            This function is used to display the tic tac toe board
        Parameters :
            none
        return :
            none
            
    """
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')

def check_winner(board):
    """
        Description :
            This function is used to check whether player 1 or player 2 wins
        Parameters :
            board (list) : tic tac toe board 
        return :
            boolean : True or False
            
    """
    p1='x'
    p2='o'
    if board[0] == board[1] == board[2] == p1 or board[0] == board[1] == board[2] == p2:
        return True
    elif board[3] == board[4] == board[5] == p1 or board[3] == board[4] == board[5] == p2:
        return True
    elif board[6] == board[7] == board[8] == p1 or board[6] == board[7] == board[8] == p2:
        return True
    elif board[0] == board[3] == board[6] == p1 or board[0] == board[3] == board[6] == p2:
        return True
    elif board[1] == board[4] == board[7] == p1 or board[1] == board[4] == board[7] == p2:
        return True
    elif board[2] == board[5] == board[8] == p1 or board[2] == board[5] == board[8] == p2:
        return True
    elif board[0] == board[4] == board[8] == p1 or board[0] == board[4] == board[8] == p2:
        return True
    elif board[2] == board[4] == board[6] == p1 or board[2] == board[4] == board[6] == p2:
        return True
    else: 
        return False
    

def user_input(board):
    """
        Description :
            This function is used to take input from user
        Parameters :
            board (list) : tic tac toe board 
        return :
            x(int) or recursive call 
            
    """
    x=int(input("Enter the position \n"))
    if board[x-1] != '-':
        print("Value already exist please enter new value")
        return user_input(board)
    else:
        return x


def main():
    player1=input("Player 1 name : ")
    player2=input("Player 2 name : ")
    display_instruction()
    display_board()

    for i in range(9):
        if i%2==0:
            print(f"\n{player1} turn")
            x=user_input(board)
            board[x-1]='x'
            display_board()
            if check_winner(board):
                print(f"{player1} wins")
                break
        else:
            print(f"\n{player2} turn")
            x=user_input(board)
            board[x-1]='0'
            display_board()
            if check_winner(board):
                print(f"{player2} wins")
                break

    print("Game over")

if __name__ == "__main__":
    main()
