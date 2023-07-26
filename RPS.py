import random

user_score = 0
comp_score = 0
options = ['rock', 'paper', 'scissors']

while True: 
    user_pick = input("Type 'rock', 'paper', 'scissors', or 'q' to quit the game: ")
    user_pick = user_pick.lower()
    
    if user_pick == 'q':
        break

    if user_pick not in options:
        continue 

    comp_pick = random.choice(options)

    outcome = {'rock':{'paper':'Loss', 'scissors':'win'},
               'paper':{'scissors':'Loss', 'rock':'win'},
               'scissors':{'rock':'Loss', 'paper':'win'}}

    if user_pick == comp_pick:
        print('It was a tie!')
    elif outcome[user_pick][comp_pick] == 'win':
        print('You win!')
        user_score += 1
    else:
        print('Computer wins!')
        comp_score += 1
        
    print('Your score: ' + str(user_score))
    print('Computer score: ' + str(comp_score))


print('Thanks for playing, see you next time!')
print('Final score: You - ' + str(user_score) +', Computer - ' + str(comp_score))
