import random
from player import Player
from utils import displayRankings, initiateGame, simulateDiceRoll, skipTurn, sumOfLastPoints, takeInputs, updateRanks
from constants import *


def startGame():
    players, maxPoints = takeInputs()
    # Initialise values
    player, unranked = initiateGame(players)
    winners = []    
    # Start Game
    while True:
        # Skip Turn is player has already won
        if player.win == True:
            player = player.next

        # Skip Turn is 1 occurs 2 times
        elif player.skip == True:
            skipTurn(player)
            player = player.next

        # Else Player Rolls the Dice
        else:
            points = simulateDiceRoll(player)
            player.lastTurn = points
            player.history.append(points)


            # Player Completes The Game
            if player.points >= maxPoints:
                updateRanks(player, winners,unranked)
                player = player.next

                # Check game completion condition
                if players == len(winners):
                    print(GAME_COMPLETED)
                    displayRankings(winners,unranked)
                    break

            elif points == 1 and player.lastTurn == 1:
                # Skip Next Turn
                print(PLAYER + str(player.no) + PENALIZED)
                player.skip = True
                player = player.next

            elif points == 6:
                # Give Extra Chance
                print(PLAYER + str(player.no) + ANOTHER_CHANCE)

            elif sumOfLastPoints(player,HISTORY) == HISTORYSUM:
                # Check Sum
                print(PLAYER + str(player.no) + ANOTHER_CHANCE_SUM,str(HISTORYSUM))

            else:
                # Increment Turn
                player = player.next

            # Display Ranking
            displayRankings(winners,unranked)


# START GAME
if __name__ == '__main__':
    startGame()
