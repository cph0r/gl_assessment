from player import Player
import random
from turns import Turns
from constants import ENTER_POINTS, ENTE_PLAYER, OUTCOME, PLAYER, ROLL_AGAIN, ROLL_DICE, SKIP_TURN, TURNS, VALID_NUMBER


def takeInputs():
    """Take Inputs from user"""
    players = enterValue(ENTE_PLAYER)
    points = enterValue(ENTER_POINTS)
    return players, points


def enterValue(statement):
    """Input Validation"""
    while True:
        try:
            print(statement)
            n = int(input())
            if n == 0 or n < 0:
                print(VALID_NUMBER)
                continue
            else:
                break
        except:
            print(VALID_NUMBER)
            continue

    return n


def diceRoll():
    """Generate Random Numbe between 1-6"""
    min = 1
    max = 6
    return random.randint(min, max)


def simulateDiceRoll(currentPlayer):
    """Simulate a Dice Roll"""
    print(PLAYER + str(currentPlayer.no) + ROLL_DICE)
    while True:
        s = input()
        if s == 'r' or s == 'R':
            break
        else:
            print(ROLL_AGAIN)
            continue
    points = diceRoll()
    print(OUTCOME, points)
    return points


def getPlayerOrder(players):
    """Get Randomly generated Player Order"""
    player_order = random.sample(range(1, players+1), players)
    print(TURNS, end=" ")
    print(player_order)
    return player_order


def skipTurn(currentPlayer):
    """Function to skip turn"""
    currentPlayer.skip == False
    print(PLAYER+str(currentPlayer.no)+SKIP_TURN)
    currentPlayer.lastTurn = 0


def displayRankings(rank_map, currentPlayer):
    """Display Rankings"""
    rank_map[currentPlayer.no] = currentPlayer.points
    rank = 1
    print('RANK\tPLAYER\t\tPOINTS')
    ranks = sorted(rank_map.items(), key=lambda x: x[1], reverse=True)
    for i in ranks:
        print(str(rank)+'\t'+PLAYER+str(i[0])+'\t'+str(i[1]))
        rank = rank + 1


def initiateGame():
    """Initialise the Game Variables"""
    # TAKE INPUTS
    players, maxPoints = takeInputs()

    # Initilaising the Turn Circle
    turn = Turns()
    # Initialising the rank Map
    rankMap = {}

    # Generate Random Player Order
    player_order = getPlayerOrder(players)
    for i in player_order:
        turn.addTurn(Player(i))
        rankMap[i] = 0

    # Get player with first Turn
    current_turn = turn.getFirstPlayer()
    return maxPoints, rankMap, current_turn
