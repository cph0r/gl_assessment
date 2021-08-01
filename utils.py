from player import Player
import random
from constants import ENTER_POINTS, ENTE_PLAYER, OUTCOME, PLAYER, ROLL_AGAIN, ROLL_DICE, SKIP_TURN, TURNS, VALID_NUMBER, WINS


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


def simulateDiceRoll(player):
    """Simulate a Dice Roll"""
    print(PLAYER + str(player.no) + ROLL_DICE)
    while True:
        s = input()
        if s == 'r' or s == 'R':
            break
        else:
            print(ROLL_AGAIN)
            continue
    points = diceRoll()
    player.points = player.points + points
    print(OUTCOME, points)
    return points



def getPlayerOrder(players):
    """Get Randomly generated Player Order"""
    player_order = random.sample(range(1, players+1), players)
    print(TURNS, end=" ")
    print(player_order)
    return player_order


def skipTurn(player):
    """Function to skip turn"""
    player.skip == False
    player.lastTurn = 0
    print(PLAYER+str(player.no)+SKIP_TURN)
    


def displayRankings(winners,unranked):
    """Display Rankings"""
    rank = 1
    
    print('RANK\tPLAYER\t\tPOINTS')
    # DISPLAY RANKED PLAYERS
    for player in winners:
        print(str(rank)+'\t'+PLAYER+str(player.no)+'\t'+str(player.points))
        rank = rank + 1
    
    # DISPLAY UNRANKED PLAYERS
    unranked = sorted(unranked, key=lambda x: x.points, reverse=True)
    for i in unranked:
        print('Unranked'+'\t'+PLAYER+str(i.no)+'\t'+str(i.points))
        rank = rank + 1


def initiateGame(players):
    """Initialise the Game Variables"""
    # Generate Random Player Order
    player_order = getPlayerOrder(players)
    
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


def updateRanks(player, winners,unranked):
    winners.append(player)
    player.win = True
    player.rank = len(winners)
    unranked.remove(player)
    print(PLAYER + str(player.no) + WINS+ str(len(winners)))