import random 

def play ():
    user = input("Choose |'R' for rock, 'P' for paper, 'S' for scissors|")
    computer= random.choice(['R',"P","S"])

    if user == computer:
        return 'Tie'
    
    if is_win (user, computer):
        return 'You Won'
    return 'You Lost '

def is_win(player,opponent):
    if(player == 'R' and opponent == 'S') or (player == 'S' and opponent =='P') or (player =='P' and opponent == 'R'):
        return True
    
print(play())