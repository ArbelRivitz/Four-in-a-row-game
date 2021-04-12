#############################################################
# FILE : ai.py
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

import random


class AI:
    """
    This is the class that manages the artificial intelligence of the server in
    a case that the player is not human
    """
    NO_MOVES = "No possible AI moves"

    def find_legal_move(self, g, func, timeout=None):
        """
        This function describes the way of the player (that is not human) of
         how to play. In our game the player checks first where there is an
         available spot, and then places the disc randomly in oon of the
         available spots
        :param g: a game object
        :param func: the function do a move
        :param timeout:
        :return:
        """
        if g.get_is_game_on:
            legal_columns = []
            board = g.get_board()
            for column in range(len(board[0])):
                if board[0][column] == g.EMPTY_PLACE:
                    legal_columns.append(column)
            if len(legal_columns) > 0:
                func(random.choice(legal_columns))
            else:
                raise Exception(AI.NO_MOVES) # when there is no more possible
                # moves it raises an exception
