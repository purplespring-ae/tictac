def play():
    current_grid = [
        [" ", "|", " ", "|", " "],
        [" ", "|", " ", "|", " "],
        [" ", "|", " ", "|", " "]
    ]

    square_names = [
        ["top left", "", "top middle", "", "top right"],
        ["middle left", "", "middle middle", "", "middle right"],
        ["bottom left", "", "bottom middle", "", "bottom right"]
    ]

    player_markers = ["O", "X"]
    current_player = 0

    def display_grid():
        for row in range(len(current_grid)):
            for sq in current_grid[row]:
                print(sq, end="")
            print("")
            if not row == len(current_grid)-1:
                print("-"*5)

    def switch_player(current_player):
        # this is tidy. will always toggle between 0 and 1
        next_player = 1 - current_player
        current_player = next_player
        print(
            f"It's Player {current_player}'s turn ({player_markers[current_player]}).")
        return True

    def gpos_from_name(square_name):
        # get row index from square name
        r_name = square_name[0:3]
        if r_name == "top":
            r_i = 0
        elif r_name == "mid":
            r_i = 1
        elif r_name == "bot":
            r_i = 2
        else:
            print("That's not a row in this grid!")
            raise Exception
        # get col index from square name and row index
        c_name = square_name[-3:]
        if c_name == "eft":
            c_i = 0
        elif c_name == "dle":
            c_i = 2
        elif c_name == "ght":
            c_i = 4
        else:
            print("That's not a playable square!")
            raise Exception

        return (r_i, c_i)

    def square_taken(sq):
        # if square is taken, return marker found there. Otherwise return False
        # TODO: if tuple, grid array ref. if string, names array ref.
        if type(sq) == str:
            r, c = gpos_from_name(sq)[0], gpos_from_name(sq)[1]

        found_value = current_grid[r][c]
        if found_value == " ":
            return False
        elif found_value in player_markers:
            return found_value
        else:
            print(
                "Something went wrong. Didn't find a blank space or either player's marker.")
            raise Exception

    def make_move(square_name):
        current_marker = player_markers[current_player]

        if not square_taken(square_name):
            r, c = gpos_from_name(square_name)[
                0], gpos_from_name(square_name)[1]
            current_grid[r][c] = current_marker
        else:
            print("That square is taken.")
            return False

        display_grid()
        switch_player(current_player)

    def check_win():
        win_combinations = [
            # rows
            ("top left", "top middle", "top right"),
            ("middle left", "middle middle", "middle right"),
            ("bottom left", "bottom middle", "middle right"),
            # columns
            ("top left", "middle left", "bottom left"),
            ("top middle", "middle middle", "bottom middle"),
            ("top right", "middle right", "middle left"),
            # diagonals
            ("top left", "middle middle", "bottom right"),
            ("top right", "middle middle", "bottom left")
        ]

        for combination in win_combinations:
            for sq in combination:
                if square_taken(sq)

    def say_free_squares():
        # TODO: print to console available squares (as help prompt)
        pass

    display_grid()
    make_move("top right")
    make_move("top right")
    check_win


if __name__ == "__main__":
    play()
