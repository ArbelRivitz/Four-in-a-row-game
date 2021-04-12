#############################################################
# FILE : game.py
# WRITER : arbelr, noamiel,207904632, 314734302,Arbel Rivitz, Noa Amiel
# EXERCISE : intro2cs ex12 2017-2018
# DESCRIPTION:
# In this excercise we made the game four in a row. This game is moduled to different parts. There is some pares at this
# this game.
# There is the Game class that has all the game rules and methods.
# there is the Gui class that includes all the  graphic parts of the game.
# there is the runner class, that has all the functions for the game to run
# there is the communicator class, that communicates between the server and the client in this game.
#  there  is the ai class that has the way of how to play
# and there is the four in a row file that that runs the whole game.
#############################################################

class Game:
    """
    This class includes the whole game methods, here we implement the game
    rules and then use this class in the other classes.

    """
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2
    ROW_LENGTH = 6
    COLUMN_LENGTH = 7
    FIRST_SPOT = 0
    MY_ERROR = 'Illegal move'
    EMPTY_PLACE = "-"
    PLAYER_ONE_COLOR = 'red4'
    PLAYER_TWO_COLOR = "sienna3"
    WIN_COLOR = "goldenrod2"

    def __init__(self):
        """
        This function initializes the different features of the class.
        We initialize a board and the game status and the current player status.

        """
        self.__board = []  # gotta check if its possible
        for x in range(6):
            sub_lst = []
            for y in range(7):
                sub_lst.append(self.EMPTY_PLACE)
            self.__board.append(sub_lst)
        self.__is_game_on = True

        self.__current_player = self.PLAYER_TWO

    def get_current_player(self):
        """

        :return: the current player number
        """
        return self.__current_player

    def set_current_player(self, new_player):
        """
        This func sets the player to the new current player.

        :param new_player: this is the new current player to be
        :return:
        """
        self.__current_player = new_player

    def get_board(self):
        """

        :return: a board (a list of lists)
        """
        return self.__board

    def get_is_game_on(self):
        """

        :return: True if game is on, False otherwise.
        """
        return self.__is_game_on

    def get_curr_player_color(self):
        """
        This func checks who is the current player and returns its color.
        :return: the current's player.
        """
        if self.get_current_player() == self.PLAYER_ONE:
            return self.PLAYER_ONE_COLOR
        elif self.get_current_player() == self.PLAYER_TWO:
            return self.PLAYER_TWO_COLOR

    def make_move(self, column):
        """
        This function represents a move in the game. First, it checks if
        the move is available, and if it is, it makes a move (the disc moves)
        :param column: the column that we want to put a disc in it
        :return: the disc's coordinates: x and Y, raises exception otherwise
        """
        if column < self.COLUMN_LENGTH and self.__is_game_on and \
                    self.__board[self.FIRST_SPOT][
                        column] == self.EMPTY_PLACE:
            self.change_player()
            for i in range(self.ROW_LENGTH, 0, -1):
                if self.__board[i - 1][column] == self.EMPTY_PLACE:
                    self.__board[i - 1][column] = str(
                        self.get_current_player())
                    return (i - 1, column)
        else:
            raise Exception(self.MY_ERROR)




    def change_player(self):
        """
        It checks what is the current player and changes it to the other player
        according to the answer.
        :return:
        """
        if self.get_current_player() == self.PLAYER_ONE:
            self.set_current_player(self.PLAYER_TWO)
        else:
            self.set_current_player(self.PLAYER_ONE)

    def print_board(self):
        """
        This function prints the board
        :return:
        """
        # for row in range(len(self.__board)):
        #     for column in range(len(self.__board[0])):
        print(self.__board)

    def set_is_game_on(self, new_state):
        """
        This func sets the player to the new current player.

        :param new_state:This is the new state of the game to be.
        :return:
        """
        self.__is_game_on = new_state

    def get_winner(self):
        """
        This function checks if there is a winner or not and returns the current
        state of the board
        :return: the winner,and the line winner or a draw
        """
        diagons_lst = self.split_diagonals_left_to_right() + \
                      self.split_diagonals_right_to_left()
        columns_lst = self.split_columns()
        rows_lst = self.split_rows()
        final_lst = diagons_lst + columns_lst + rows_lst # all the options
        # of sets of four discs
        for lst in final_lst:
            winner1, lst1 = self.is_winner_helper(lst, self.PLAYER_ONE)
            winner2, lst2 = self.is_winner_helper(lst, self.PLAYER_TWO)
            if winner1:  # case no. 1
                return self.PLAYER_ONE, lst1
            elif winner2:  # case no. 2
                return self.PLAYER_TWO, lst2
            elif self.is_board_filled():  # this is a draw case
                return self.DRAW, None
        return None, None

    def is_board_filled(self):
        """
        This func checks if the board is filled
        :return: True if it is, False otherwise
        """
        counter = 0
        for r in range(len(self.__board[0])):
            if self.__board[0][r] != self.EMPTY_PLACE:
                counter += 1
        if counter == self.COLUMN_LENGTH:
            return True
        else:
            return False

    def get_player_at(self, row, col):
        """
        This func checks if there is a disc in a spot and returns the location
        of this disc
        :param row: this is the row cord
        :param col: this is the col cord
        :return: none if there is no disc, the location if there is
        """

        player_at = self.__board[row][col]
        if player_at == self.EMPTY_PLACE:
            return None
        else:
            return player_at

    def is_winner_helper(self, lst, player):
        """
        This function checks if there is a winner at the board at a specific
        time

        :param lst: one of the lists of the funals lists (all the srt options of
        4 discs)
        :param player: a number of a player
        :return:True if one if the player has actually one entire set in its
        color, and the coordinates set. Else, it returns False and None
        """
        board = self.get_board()
        counter = 0
        coords_set = set()
        for i in range(len(lst) - 1):
            if board[lst[i][0]][lst[i][1]] == \
                    board[lst[i + 1][0]][lst[i + 1][1]] == str(player):
                counter += 1
                coords_set.update([(lst[i][0], lst[i][1])])
                coords_set.update([(lst[i + 1][0], lst[i + 1][1])])
            else:
                if counter >= 3:
                    return True, coords_set
                counter = 0
                coords_set.clear()
        if counter >= 3:
            return True, coords_set
        else:
            return False, None

    def split_diagonals_right_to_left(self):
        """
        This func splits the diagonals from right to left and returns a list
         of all of the coordinates that we got.
        :return:list of all of the coordinates that we got.
        """
        board = self.get_board()
        num_of_row = len(board)
        num_of_column = len(board[0])
        coords_lst = []
        for item in range(num_of_column + num_of_row - 1):
            sub_lst = []
            for row in range(num_of_row):
                for column in range(num_of_column):
                    if row + column == item:
                        sub_lst.append((row, column))
            if len(sub_lst) >= 4:
                coords_lst.append(sub_lst)
        return coords_lst

    def split_diagonals_left_to_right(self):
        """
        This func splits the diagonals ftom left to right and returns a list
         of all of the coordinates that we got.

        :return: list of all of the
        coordinates that we got.
        """
        board = self.get_board()
        num_of_row = len(board)
        num_of_column = len(board[0])
        coords_lst = []
        for item in range(-num_of_column, num_of_column):
            sub_lst = []
            for row in range(num_of_row):
                for column in range(num_of_column):
                    if (row - column) == item:
                        sub_lst.append((row, column))
            if len(sub_lst) >= 4:
                coords_lst.append(sub_lst)
        return coords_lst

    def split_columns(self):
        """
        This function splits all the coloumns and returns a list of coordinates
        of all of the columns
        :return: list of coordinates
        of all of the columns
        """
        board = self.get_board()
        num_of_row = len(board)
        num_of_column = len(board[0])
        coords_lst = []
        for column in range(num_of_column):
            sub_lst = []
            for row in range(num_of_row):
                sub_lst.append((row, column)
                               )
            coords_lst.append(sub_lst)
        return coords_lst

    def split_rows(self):
        """
        This function splits all the rows and returns a list of coordinates
        of all of the rows
        :return: list of coordinates
        of all of the rows
        """
        board = self.get_board()
        num_of_row = len(board)
        num_of_column = len(board[0])
        coords_lst = []
        for row in range(num_of_row):
            sub_lst = []
            for column in range(num_of_column):
                sub_lst.append((row, column)
                               )
            coords_lst.append(sub_lst)
        return coords_lst
