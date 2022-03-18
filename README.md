
# Checkers
## Intro 
My first Python project using the Pygame Library, coding the game - Checkers!

## Requirements

* <a href="https://pipenv.pypa.io/en/latest/" target="_blank">Pipenv</a>

## Explanation  

The checkers game is split into five different files:
  1. configutaion.py - holds all the components and the configurations
  2. piece.py - all the info regarding each piece is stored using the Piece class + drawing the pieces into the board and crowning       functions
  3. board.py - the Board class is in charge of creating and drawing the board
  4. player.py - As the name impleis the Player class holds all the functions that are related to making the moves
  5. chekers.py - The main file that makes it possible for us to play the checkers game with GUI using the Game class
       
## Run

```
pipenv install --dev
pipenv run python chekers.py 
```
