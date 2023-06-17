import random

# Define the snakes and ladders
snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}

# Initialize the positions of the two players
player1_pos = 0
player2_pos = 0

# Define a function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Define a function to move the player's position
def move_player(player_pos, dice_roll):
    new_pos = player_pos + dice_roll
    if new_pos > 100:
        new_pos = player_pos
    elif new_pos in snakes:
        new_pos = snakes[new_pos]
    elif new_pos in ladders:
        new_pos = ladders[new_pos]
    return new_pos

# Start the game
print("Let's start the game!")
while True:
    # Player 1's turn
    input("Player 1, press Enter to roll the dice.")
    dice_roll = roll_dice()
    print("Player 1 rolled a {}.".format(dice_roll))
    player1_pos = move_player(player1_pos, dice_roll)
    print("Player 1 is now at position {}.".format(player1_pos))
    if player1_pos == 100:
        print("Player 1 has won the game!")
        break

    # Player 2's turn
    input("Player 2, press Enter to roll the dice.")
    dice_roll = roll_dice()
    print("Player 2 rolled a {}.".format(dice_roll))
    player2_pos = move_player(player2_pos, dice_roll)
    print("Player 2 is now at position {}.".format(player2_pos))
    if player2_pos == 100:
        print("Player 2 has won the game!")
        break
    
    
    
    
    
    
    