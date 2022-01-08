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

def main():
    
    # init board 
    board = init_board()
    
    # ask users names 
    # (first, second) = get_names()

    # for up 9 moves, switch users, X is first, 

        # display board( board )

        # ask user 1,2 to place piece 

            # check if piece can go there, else loop to ask again 


        # CHECK IF WINNER??
            # if yes, break, declare the user 

    # if no winner, declare draw 
    
if __name__ != "__main__":
    main()