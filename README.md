# Four-in-a-row-game
Four-in-a-row game, including server-client
In order to run the game, run the four_in_a_row.py script. Each game requires two participants - server and client. They can be on different or the same computer.
The program requires 4 arguments:
four_in_a_row.py <is_human> <port> <ip>
is_human - human if the player is human, ai if the player is AI
port - The port number used for communication (e.g., 8000)
ip - only required by the client 
For example - 
From the client side - python3 four_in_a_row.py ai 8000
From the server side - python3 four_in_a_row.py human 8000 10.0.0.7

  

