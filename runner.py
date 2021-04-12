#############################################################
# FILE : runner.py
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
import game
import communicator
import gui
from tkinter import messagebox as mb

class Runner():
    """
    This is the main class that runs all the different functions
    """

    def __init__(self, root, port, ai=None, ip=None):
        """

        :param root: a root
        :param port: n endpoint of communication in the computer of the player
        :param ip: the ip address of the client
        :param ai:  True if it is not human, and False otherwise
        """
        self.ai = ai
        self.root = root
        self.port = port
        self.game = game.Game()
        self.communicator = communicator.Communicator(self.root, port, ip)
        self.communicator.connect()
        self.communicator.bind_action_to_message(self.msg_received)
        if ip is not None: # that means that there is a server
            self.player = self.game.PLAYER_TWO
        else:
            self.player = self.game.PLAYER_ONE

        self.gui = gui.Gui(self.root, self, self.game,self.player)

    def run(self):
        """
        This func runs the game in a case of human or not
        :return:
        """
        if self.ai is not None and self.game.get_current_player() != self.player:
            self.ai.find_legal_move(self.game, self.do_a_move)
        self.root.mainloop()

    def do_a_move(self, column):
        """
        This func is the whole process of one move
        :param column: the column that we want to put the disc in
        :return:
        """
        if self.player != self.game.get_current_player() and column is not None:
            try:
                coords = self.game.make_move(column)
            except Exception as e:
                mb.showerror("Error", e)
                return
            if coords is not None:
                new_row = coords[0]
                new_col = coords[1]
                self.gui.update_board(new_row, new_col) # updates the board
                self.communicator.send_message(column) # sends msg to the other
                # player
                self.gui.what_player_is_it(self.player)
                winner, lst = self.game.get_winner()
                self.gui.declare_winner(winner, lst, self.player)



    def msg_received(self, message):
        """
        This function tells the player what to do after getting a message from
        the other player
        :param message: the message that we get from the other plyer that tells
        us where a disc has been put
        :return:
        """
        column = int(message)
        if column is not None:
            new_row, new_col = self.game.make_move(column)
            self.gui.update_board(new_row, new_col)
            winner, lst = self.game.get_winner()
            self.gui.declare_winner(winner, lst, self.player)
            self.gui.what_player_is_it(self.player)
            if self.ai is not None and self.game.get_current_player() != self.player\
                    and self.game.get_is_game_on():
                try:
                    self.ai.find_legal_move(self.game, self.do_a_move)
                except Exception as e:
                    mb.showerror("Error", e)
                    return
