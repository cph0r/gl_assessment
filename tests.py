from utils import displayRankings, skipTurn, updateRanks
from constants import ANOTHER_CHANCE, GAME_COMPLETED, OUTCOME, PENALIZED, PLAYER, WINS
import unittest
from player import Player

def initiateGame(players):
    """Initialise the Game Variables"""
    # Generate Random Player Order
    player_order = [3,1,2]
    
    firstPlayer = Player(player_order[0]) 
    unranked = {firstPlayer}
    player = firstPlayer

    for i in player_order:
        if player_order.index(i) == 0:
            continue
        elif player_order.index(i) == players -1:
            unranked.add(player)
            player.next= Player(i)
            player = player.next
            player.next = firstPlayer
        else:
            player.next = Player(i)
            player = player.next
        unranked.add(player)
    return firstPlayer ,unranked


class TestStringMethods(unittest.TestCase):
    def main(self):
        players = 3
        maxPoints = 7
        # Initialise values
        player, unranked = initiateGame(players)
        winners = []   
        diceRolls = [1,1,6,4,1,5,1,6,2,3,4]
        i = 0 
        # Start Game
        while True:
            # Skip Turn is player has already won
            if player.win == True:
                player = player.next

            # Skip Turn is 1 occurs 2 times
            elif player.skip == True:
                # SKIP TESTING
                skipTurn(player)
                player = player.next

            # Else Player Rolls the Dice
            else:
                points = diceRolls[i]
                # Update last Turn value for the player
                print(player.no)
                player.points = player.points + points
                print(OUTCOME, points)

                # Player Completes The Game
                if player.points >= maxPoints:
                    updateRanks(player, winners,unranked)
                    player.lastTurn = points
                    player = player.next

                    # Check game completion condition
                    if players == len(winners):
                        print(GAME_COMPLETED)
                        displayRankings(winners,unranked)

                        # RANK TESTING
                        self.rankTest(winners)
                        break
                    

                elif points == 1 and player.lastTurn == 1:
                    # Skip Next Turn
                    self.skipTurnTest(player,i)
                    print(PLAYER + str(player.no) + PENALIZED)
                    player.lastTurn = points
                    player.skip = True
                    player = player.next

                elif points == 6:
                    # Give Extra Chance
                    self.extraChanceIndexCheck(player, i)
                    player.lastTurn = points
                    print(PLAYER + str(player.no) + ANOTHER_CHANCE)

                else:
                    # Increment Turn
                    player.lastTurn = points
                    player = player.next

                # Display Ranking
                displayRankings(winners,unranked)

                # TESTS
                self.extraChanceTest(player, i)
                self.skipChanceTest(player,i)
                i = i + 1

    def rankTest(self, winners):
        self.assertEqual(winners[0].no, 2)
        self.assertEqual(winners[1].no, 1)
        self.assertEqual(winners[2].no, 3)

    

    def skipTurnTest(self, player, i):
        self.assertEqual(i, 4)
        self.assertEqual(player.no, 3)
    
    def extraChanceTest(self, player, i):
        # EXTRA CHANCE TEST
        if i == 2:
            self.assertEqual(player.no, 2)

    def skipChanceTest(self, player, i):
        # SKIP CHANCE TEST
        if i == 4:
            self.assertEqual(player.skip, True)

    def extraChanceIndexCheck(self, player, i):
        
        self.assertEqual(i, 2)
        self.assertEqual(player.no, 2)   


if __name__ == '__main__':
    unittest.main()

