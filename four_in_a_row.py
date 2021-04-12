#############################################################
# FILE : four_in_a_row.py
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

import tkinter
import sys
from ai import AI
from runner import Runner


MAX_PORT = 65535
MIN_PORT = 1000
HUMANPLAYER = "human"
AIPLAYER = "ai"
ILLEGAL_ARGS = "Illegal program arguments."


def running_a_cilent(is_human, port, ip):
    """
    This function runs the client game.
    :param is_human: true if it is, false otherwise
    :param port: the port to connect to (client)
    :param ip: the ip address of the computer of the client
    :return:
    """
    root = tkinter.Tk()
    root.title("Client")
    if is_human:
        runner = Runner(root, port, None, ip)
        runner.run()
    else:
        ai = AI()
        runner = Runner(root, port, ai, ip)
        runner.run()


def running_a_server(is_human, port):
    """
    This function runs the server game. It checks if it is human or not and
    runs according to it
    :param is_human:true if it is, false otherwise
    :param port:the port to connect to (server)
    :return:
    """
    root = tkinter.Tk()
    root.title("Server")
    if is_human:
        runner = Runner(root, port)
        runner.run()
    else:
        ai = AI()
        runner = Runner(root, port, ai)
        runner.run()


def main():
    """
    This function runs the whole game according to the numbers of the arguments
    :return:
    """
    arguments = sys.argv[1:] # the number of the arguments tells us what is the
    # player
    if 2 == len(arguments) or len(arguments) == 3:
        if arguments[0] == HUMANPLAYER:
            is_human = True
        elif arguments[0] == AIPLAYER:
            is_human = False
        if MIN_PORT <= int(arguments[1]) or int(arguments[1] > MAX_PORT):
            if len(arguments) == 3:
                running_a_cilent(is_human, int(arguments[1]), arguments[2])
            elif len(arguments) == 2:
                running_a_server(is_human, int(arguments[1]))
        else:
            print(ILLEGAL_ARGS) # prints an error message
    else:
        print(ILLEGAL_ARGS) # prints an error message



if __name__ == "__main__":
    main()

