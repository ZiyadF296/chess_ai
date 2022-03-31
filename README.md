## Chess AI

- An AI terminal application that you can play AI against. 

## How does it work?

Each piece has their own heatmap of how good the position of the piece is if it were to be in that position.

We used an external library called NUMPY to create the heatmap. This library based on the heatmap and given input of the board state will output the best prediction of the next move the black player (AI) will make. User is always the white player.

## It is still possible for the AI to make a mistake.

This AI model is not perfect, it will eventually make mistakes giving you the chance to win. Also, you can still fool the AI, but it is still a good way to learn how to play chess.

## How we validate pieces?

Each piece has a subclass inside the main class (Piece). Each subclass contain static and public methods that can be used to validate the position of the piece.