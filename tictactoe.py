"""
# This is the ideas
0  |  1  | 2
===========
3  |  4  | 5
===========
6  |  7  | 8


list of slots = [" ",  ]

logic determine if I won

keep track name of the persons playing (in the beginning we want to add the users name)


user name won!

"""


def init_board():
    spaces = [" "," "," "," "," "," "," "," "," "]
    
    return spaces

def clear_board( mylist ):
    """ this does an INPLACE change"""
   
    for i in range(9):
        if mylist[i] != ' ':
            mylist[i] = ' '

    return mylist

def get_names():
    first = input("Enter first Player's name: ")
    second = input("Enter second Player's name: ")
    return (first, second)

def display_board(b):
    return f" {b[0]} | {b[1]} | {b[2]}\n" + \
            "===========\n" + \
           f" {b[3]} | {b[4]} | {b[5]}\n" + \
            "===========\n" + \
           f" {b[6]} | {b[7]} | {b[8]}\n"

def winner(tc, board):
    tc = get_names
    # need to write code for testing Rows
    # need to write code for testing Columns
    # need to write code for testing Diag


    return False 

def main():

    # init board 
    board = init_board()
    
    # ask users names 
    (first, second) = get_names()

    # for up 9 moves, switch users, X is first, 
    for moves in range(9):

        # display board( board )
        db = display_board(board)
        print(db)

        # ask user 1,2 to place piece (0,..,8)
        # pos = ask_user_position(board)
        #        -- routine, is_pos_taken(pos, board)

        # CHECK IF WINNER??
            # if yes, break, declare the user 
        if winner(tc, board):
            # print message, like Bob is the Winner!
            break 
    # if no winner, declare draw 

    # Print nobody has won, it's a draw!



if __name__ == "__main__":
    main()