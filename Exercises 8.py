#Make a two-player Rock-Paper-Scissors game

player1 = input("Player 1, input either Rock, Paper, or Scissors: ")
player2 = input("Player 2, input either Rock, Paper, or Scissors: ")

def compare(p1, p2):
    if p1 == p2:
        return("Tie")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("Rock wins")
        else:
            return("Scissors wins")
    elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins")
        else:
            return("Scissors wins")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors wins")
        else:
            return("Rock wins")
    else:
        return("Try again")
        
print(compare(player1,player2))