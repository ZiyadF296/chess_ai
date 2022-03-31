## Chess AI

- An AI terminal application that you can play AI against. 
- The chess game is played on the terminal and is optimized to be played on a terminal. It has been made as user friendly as possible. Considering a UI.
- To run the app, make sure you are in the same directory as the app. Then run the following command:
    `python main.py`

## How does it work?

Each piece has their own heatmap of how good the position of the piece is if it were to be in that position.

We used an external library (`NUMPY`) to create the heatmap. This library based on the heatmap and given input of the board state will output the best prediction of the next move the black player (AI) will make. User is always the white player.

## It is still possible for the AI to make a mistake.

This AI model is not perfect, it will eventually make mistakes giving you the chance to win. Also, you can still fool the AI, nevertheless, it is still a good way to learn how to play chess.

## How we validate pieces?

Each piece has a subclass inside the main class (Piece). Each subclass contain static and public methods that can be used to validate the position of the piece.

### Have a look at what it looks like when you run the program [here](./sample.png)

### Disclaimer:
Some of the code logic is based on online article since they are the best sources for chess moves logic (as I don't really know how to play chess and what are considered valid moves). This is used to validate the chess AI move when it makes a move and let it retry, or when the player makes an invalid move.