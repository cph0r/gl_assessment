import random
from player import Player
from turns import Turns
from utils import displayRankings, initiateGame, simulateDiceRoll, skipTurn
from constants import *


def startGame():
    # Initialise values
    maxPoints, rankMap, current_turn = initiateGame()
    
    # Start Game
    winners = 0
    while True:
        currentPlayer = current_turn.data

        if currentPlayer.win == True:
            # Skip Turn is player has already won
            current_turn = current_turn.next

        elif currentPlayer.skip == True:
            # Skip Turn is 1 occurs 2 times
            skipTurn(current_turn, currentPlayer)
            current_turn = current_turn.next

        else:
            # Else Player Rolls the Dice
            points = simulateDiceRoll(currentPlayer)
            currentPlayer.points = currentPlayer.points + points

            # Display Ranking
            displayRankings(rankMap, currentPlayer)

            if currentPlayer.points >= maxPoints:
                print(PLAYER + str(currentPlayer.no) + WINS)
                currentPlayer.win = True

                # Check completion condition
                winners = winners + 1
                if winners == len(rankMap):
                    print(GAME_COMPLETED)
                    break
                current_turn = current_turn.next

            elif points == 1 and currentPlayer.lastTurn == 1:
                # Skip Next Turn
                print(PLAYER + str(currentPlayer.no) + PENALIZED)
                current_turn = current_turn.next

            elif points == 6:
                # Give Extra Chance
                print(PLAYER + str(currentPlayer.no) + ANOTHER_CHANCE)

            else:
                # Increment Turn
                current_turn = current_turn.next

            # Update last Turn value for the player
            currentPlayer.lastTurn = points


# START GAME
if __name__ == '__main__':
    startGame()
