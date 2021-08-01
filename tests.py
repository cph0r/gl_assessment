from utils import displayRankings, skipTurn
from constants import ANOTHER_CHANCE, GAME_COMPLETED, PENALIZED, PLAYER, WINS
import unittest
from player import Player



class TestStringMethods(unittest.TestCase):
    def createTestCircle(player_len):
        rankMap = {}
        for i in range(1,player_len+1):
            rankMap[i] = 0

        return  rankMap


    def main(self):
        # Initialise Test values
        maxPoints = 6
        current_turn , rankMap = self.createTestCircle(3)
        winners = 0
        iteration = 0

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
                points = currentPlayer.no
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
                iteration = iteration + 1
                currentPlayer.lastTurn = points


        # RANK MAP TESTING
        self.assertEqual(rankMap[1], 6)
        self.assertEqual(rankMap[2], 6)
        self.assertEqual(rankMap[3], 6)


if __name__ == '__main__':
    unittest.main()


