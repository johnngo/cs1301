#First we create our function.

def check_horse_winner(stats):

#Note that this problem can be done in multiple ways, I decided to
#just use a string and concatenate.
#I created a 'not_out' string that will hold all the Players that are
#not out. My 'not_out_num' is a value that keeps hold of the number of
#players not out since strings cannot hold that value for me.

    not_out = ""
    not_out_num = 0

#We start with a for loop that will go through the list of the players
#score. 'player' variable is a string that will tell us whether the player
#is out or not out.
#In order to determine whether they are out, we compare it with the length of
#"HORSE". It must be ONLY less than since if equal, then player is out.

    for player in range (0, len(stats)):
        

#Now that we have set a condition that will tell us which players are not out
#We add to our 'not_out' string every time a player has a score less than HORSE.
#The if-else statement is solely for formatting. If there are currently nobody
#then we do not add a comma before, if it isn't the first player, then we add
#a comma to the front before concatenating to our 'not_out' string.
#Remember to increment not_out_num as we need to keep track of how many players
#are still in the game.

        if len(stats[player]) < len("HORSE"):
            if (not_out_num == 0):
                not_out += str(player)
            else:
                not_out += ", " + str(player)
            not_out_num += 1 

#At this point we now have stored a string of all the players not out and the
#number of players not out. With this information, we now have to return
#certain statements. If there is only 1 player left then we have a winner.
#If there are multiple players left then we return differently etc.
#Thus, we set conditionals to see how many players are left and from there we
#simply just format our answer to what the autograder expects.

    if not_out_num == 1:
        return "Player " + not_out + " wins!"
    elif not_out_num < len(stats): 
        return "Players " + not_out + ": keep playing!"
    else:
        return "Everyone: keep playing!"

print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))


#The game HORSE is a popular basketball shooting game.
#It can be played with any number of players. One-by-one,
#each player takes a shot from anywhere they want. If they
#make the shot, the next person must make the same shot.
#If they do not, they receive a letter: H, then O, then R,
#then S, then E. Once a player receives all 5 letters, they
#are out of the game.
#
#The game continues until all but one player has all five
#letters.
#
#Write a function called check_horse_winner. This function
#will take as input a tuple of at least two, but potentially
#more, strings. 
#
#check_horse_winner should return the following:
#
# - If only one player is left with fewer than 5 letters,
#   return "Player X wins!", where X is the index of the
#   player in the list (which could be 0).
# - If more than one player has fewer than 5 letters,
#   return "Players X, Y: keep playing!", where X, Y, and
#   potentially more numbers are the indices of all players
#   who have not yet been eliminated.
# - If no player has 5 letters, return "Everyone: keep
#   playing!"


#Write your function here!
from typing import Tuple

def check_horse_winner(players: Tuple[str, ...]) -> str:
    next_round = [str(index) for index, player in enumerate(players) if len(player) < 5]
    
    if len(next_round) == len(players):
        return f'Everyone: keep playing!'
    elif len(next_round) > 1:
        return f'Players {", ".join(next_round)}: keep playing!'
    else:
        return f'Player {next_round[0]} wins!'
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Everyone: keep playing!
#Players 1, 2: keep playing!
#Player 2 wins!
print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))
