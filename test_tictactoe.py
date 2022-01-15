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
    
def test_get_names():
    assert 1 != 2 
    # v1, v2 = tictactoe.get_names()
    
def test_display_board_empty():
    ib = tictactoe.init_board()
    v = tictactoe.display_board(ib)
    
    res = "   |   |   \n"+\
          "===========\n"+\
          "   |   |   \n"+\
          "===========\n"+\
          "   |   |   \n"
    assert len(res.split("\n")) == len(v.split("\n"))
    
    for rline, vline in zip(res.split("\n"), v.split("\n")):
        print(f"\n{rline=}\n{vline=}")
        assert vline == rline
        
def test_display_board_X():
    ib = tictactoe.init_board()

    for idx in range(9):
        ib[idx] = 'X'

    v = tictactoe.display_board(ib)

    res = " X | X | X\n" + \
          "===========\n" + \
          " X | X | X\n" + \
          "===========\n" + \
          " X | X | X\n"
          
    assert len(res.split("\n")) == len(v.split("\n"))

    for rline, vline in zip(res.split("\n"), v.split("\n")):
        print(f"\n{rline=}\n{vline=}")
        assert vline == rline

def test_display_board_O():
    ib = tictactoe.init_board()

    for idx in range(9):
        ib[idx] = 'O'

    v = tictactoe.display_board(ib)

    res = " O | O | O\n" + \
          "===========\n" + \
          " O | O | O\n" + \
          "===========\n" + \
          " O | O | O\n"

    assert len(res.split("\n")) == len(v.split("\n"))

    for rline, vline in zip(res.split("\n"), v.split("\n")):
        print(f"\n{rline=}\n{vline=}")
        assert vline == rline
def test_display_board_all_rows_XO():
    for ch in ["X","O"]:
        # Row 1
        b = tictactoe.init_board()
        b[0] = b[1] = b[2] = ch
        assert tictactoe.winner(ch, b) == True 

        # Row 2
        b = tictactoe.init_board()
        b[3] = b[4] = b[5] = ch
        assert tictactoe.winner(ch, b) == True 

        # Row 3
        b = tictactoe.init_board()
        b[6] = b[7] = b[8] = ch
        assert tictactoe.winner(ch, b) == True
    
def test_display_board_all_cols_XO():
    for ch in ["X","O"]:
        # cols 1
        b = tictactoe.init_board()
        b[0] = b[3] = b[6] = ch
        assert tictactoe.winner(ch, b) == True 

        # cols 2
        b = tictactoe.init_board()
        b[1] = b[4] = b[7] = ch
        assert tictactoe.winner(ch, b) == True 

        # cols 3
        b = tictactoe.init_board()
        b[2] = b[5] = b[8] = ch
        assert tictactoe.winner(ch, b) == True
    
def test_display_board_all_diag_XO():
    for ch in ["X","O"]:
        # cols 1
        b = tictactoe.init_board()
        b[0] = b[4] = b[8] = ch
        assert tictactoe.winner(ch, b) == True 

        # cols 2
        b = tictactoe.init_board()
        b[2] = b[4] = b[6] = ch
        assert tictactoe.winner(ch, b) == True