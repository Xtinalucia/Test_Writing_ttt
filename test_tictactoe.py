import tictactoe

def test_init_board():
    """ Make sure that init_board returns 
    a list 
    of 9 spaces"""
    assert len(tictactoe.init_board()) == 9
    assert tictactoe.init_board() == list(" "*9)

def test_clear_board():
    """ Make sure that clear_board returns 
    given a list of X, O, returns 
    a list 
    of 9 spaces only"""
    
    lst = [
        "X", "O", "X",
        "X", "O", "X",
        "X", "O", "X",
    ]

    assert len(tictactoe.clear_board(lst)) == 9
    # forces the issue, I DO want an INPLACE change of the values 
    # of my list
    assert lst[0] == " "
    assert lst == list(" "*9)

    
    