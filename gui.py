#############################################################
# FILE : gui.py
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

from tkinter import *


class Gui:
    """
    This class is the main class of the graphic implementation of all of the
    board. In order to create the board, we divided the pixels board so we got
    a board of 6 X 7 with coordinates that are compatible with the coordinates
    that we gor in the class game.

    """
    LENGTH = 435
    CROP = 0.03908045977011494 * LENGTH
    INIT = CROP
    END = LENGTH - INIT
    TOTAL = END - INIT
    COLUMNS_NUM = 7
    COLUMN_LEN = TOTAL / COLUMNS_NUM
    ROWS_NUM = 6
    ROW_LEN = TOTAL / ROWS_NUM
    ROWS_EDGE = 0.022988505747126436 * LENGTH
    COLUMNS_EDGE = ROWS_EDGE / 2
    YOUR_TURN_MSG = "Time to show me what you got!"
    NOT_YOUR_TURN_MSG = "Not your turn mate!"

    def __init__(self, root, runner, game, player):
        """
              This func initializes the features of this class.

              :param root: a root
              :param runner:This is an object of the class runner
              :param game: this is an object of the class game
              """
        self.__root = root
        self.__runner = runner
        self.__game = game
        self.__player = player
        self.__canvas = Canvas(width=Gui.LENGTH, height=Gui.LENGTH)
        self.__image = PhotoImage(file="4inarow.jpg").subsample(
         2,2)
        self.__loss_photo = PhotoImage(file="lose.png")
        self.__win_photo = PhotoImage(file="win.png").subsample(2, 2)
        self.__draw_photo = PhotoImage(file="its-a-draw.png").subsample(2, 2)
        self.__top_photo = PhotoImage(file="top.gif").subsample(2,2)
        self.restart_canvas()

    def restart_canvas(self):
        """
        This func restarts the canvas board

        :return:
        """
        self.__canvas.pack(side="bottom")
        self.__canvas.create_image(0, 0, image=self.__image, anchor=NW)
        self.__canvas1 = Canvas(width=Gui.LENGTH, height=70, bg="chocolate3")
        self.__canvas1.pack(side="top")
        self.__canvas1.create_image(90, 0, image=self.__top_photo, anchor=NW)
        self.__canvas.bind("<Button-1>", self.callback)
        self.__label = Label(text="", font="Algerian 20 ")
        self.__label.pack(side="bottom")
        self.what_player_is_it(self.__player)

    def what_player_is_it(self, player):
        """
        This function changes the message at the top of the board according to
        the player who is playing right now
        :param player: the actual player
        :return:
        """
        if self.__game.get_current_player() != player:
            self.__label.config(text=self.YOUR_TURN_MSG)
        else:
            self.__label.config(text=self.NOT_YOUR_TURN_MSG)

    def callback(self, event):
        """
        This func connects between the button click on a place at the board
        and the filling of the board (the discs spots on the board), it moves
         if there is no winner
        :param event:the user's click
        :return:
        """
        winner, lst = self.__game.get_winner()
        if winner is None:
            column = self.covert_x_pix_to_col(event.x, event.y)
            self.__runner.do_a_move(column)


    def update_board(self, new_row, new_col):
        """
        This function updates the board after each move of the players and
        places a disc at the correct spot
        :param new_row: This is the row that the player wants to put the
        disc in
        :param new_col: This is the column that the player wants to put the
        disc in
        :return:
        """
        start_x, end_x = self.covert_col_to_pix(new_col)  # the x pixels zone
        start_y, end_y = self.covert_row_to_pix(new_row)  # thw y pixels zone
        self.__canvas.create_oval(start_x + self.COLUMNS_EDGE,
                                  start_y + self.ROWS_EDGE,
                                  end_x - self.COLUMNS_EDGE,
                                  end_y - self.ROWS_EDGE,
                                  fill=self.__game.get_curr_player_color())

    def declare_winner(self, winner, lst, cur_player):
        """
        This function declares who is the winner by popping up a picture to each
         player or draw, depend on the results.
        :param winner: the function get winner
        :param lst: the coordinates of the 4 discs that 'won'
        :param cur_player: the current player that played
        :return:
        """
        if winner is not None:
            self.__game.set_is_game_on(False)
            if winner == cur_player:
                self.change_color_ovals_win(
                    lst)  # it changes the color of the
                # 4 discs of the winner
                self.__root.after(1000, self.printWin)  # a win photo

            elif self.__game.is_board_filled():
                self.__canvas.create_image(70, 30, image=self.__draw_photo,
                                           anchor=NW)  # a draw photo
                self.on_closing()

            else:
                self.change_color_ovals_win(lst)
                self.__root.after(500, self.printLoss)  # a loss photo

    def change_color_ovals_win(self, lst):
        """
        This function changes the color of the ovals that the winner won with
        them
        :param lst:the coordinates of the 4 discs that 'won'
        :return:
        """
        for coord in lst:
            start_x, end_x = self.covert_col_to_pix(coord[1])
            start_y, end_y = self.covert_row_to_pix(coord[0])
            self.__canvas.create_oval(start_x + self.COLUMNS_EDGE,
                                      start_y + self.ROWS_EDGE,
                                      end_x - self.COLUMNS_EDGE,
                                      end_y - self.ROWS_EDGE,
                                      fill=self.__game.WIN_COLOR)

    def printWin(self):
        """
        This function creates a win message for the winner and closes the board
        :return:
        """
        self.__canvas.create_image(120, 100, image=self.__win_photo,
                                   anchor=NW)
        self.on_closing()

    def printLoss(self):
        """
        This function creates a loss message for the loser and closes the board
        :return:
        """
        self.__canvas.create_image(80, 100, image=self.__loss_photo,
                                   anchor=NW)
        self.on_closing()

    def covert_x_pix_to_col(self, x,y):
        """
        This func converts the pixel of the X to the coordinate as we defined
        them in the game class
        :param x: a x pixel
        :return: the column to put it in
        """
        if x >= Gui.INIT and x <= Gui.END and y>= Gui.INIT and y<= Gui.END:
            column = int((x - Gui.CROP) // Gui.COLUMN_LEN)
            return column
        else:
            return None

    def covert_col_to_pix(self, col):
        """
        This function converts the column coordinate to the original pixel zone
        :param col: the current col
        :return: the x pixels zone
        """
        x_pix_start = (col * Gui.COLUMN_LEN) + Gui.INIT
        x_pix_end = ((col + 1) * Gui.COLUMN_LEN) + Gui.INIT
        return x_pix_start, x_pix_end

    def covert_y_pix_to_row(self, y):
        """
        This func converts the pixel of the y to the row as we splitted
        them in the game class
        :param y: a y pixel
        :return: the y row
        """
        if y >= Gui.INIT and y <= Gui.END:
            row = int((y - Gui.CROP) // Gui.ROW_LEN)
            return row

    def covert_row_to_pix(self, row):
        """
        This function converts the row coordinate to the original pixel
        :param row: This is the the row
        :return: the y pixel of the beginning and the end- pixel zone
        """
        y_pix_start = (row * Gui.ROW_LEN) + Gui.INIT
        y_pix_end = ((row + 1) * Gui.ROW_LEN) + Gui.INIT
        return y_pix_start, y_pix_end

    def on_closing(self):
        """
        This function destroys the tk canvas
        :return:
        """
        self.__root.after(1000, self.__root.destroy)
