Code for Great Learning Assessment
HOW TO RUN:
-> Clone the project and run main.py file


Problem Statement:
-> Make a Dice rolling game with following functionalities
    1. Take inputs from user for no of players and max points
    2. Simulate Dice roll
    3. add dice roll value to points of player
    4. Skip the chance in case of double 1
    5. Give extra chance in case of 6
    6. Show ranks after every roll
    7. Once player points go over reuired points he completes the games
    8. Game is finished when every person get his points over the the required points

Assumptions:
1. only positive integers would be entered by the users for input for no' of players and max points, even then validation has been applies
2. dice roll is randomly simulated in python by generating a random number between 1 - 6
3. Upper Bounds on No of players and max points is equal to  max value that can be stored in int data type and min value is 1 for both

Issues:
    1. Ranking system should have been made as a doubly linked list for faster display

Bonus:
1. Tests are created for checking ranks
