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

    random_num = random.randint(0,2)
    comp_pick = options[random_num]

    if user_pick == 'rock' and comp_pick == 'scissors':
        print('You win!')
        user_score += 1
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))
    if comp_pick == 'rock' and user_pick == 'scissors':
        print('Computer wins!')
        comp_score += 1
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))

    if user_pick == 'paper' and comp_pick == 'rock':
        print('You win!')
        user_score += 1
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))
    if comp_pick == 'paper' and user_pick == 'rock':
        print('Computer wins!')
        comp_score += 1
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))

    if user_pick == 'scissors' and comp_pick == 'paper':
        print('You win!')
        user_score += 1
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))
    if comp_pick == 'scissors' and user_pick == 'paper':
        print('Computer wins!')
        comp_score += 1
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))

    if user_pick == comp_pick:
        print('It was a tie!')
        print('Your score: ' + str(user_score))
        print('Computer score: ' + str(comp_score))


print('Thanks for playing, see you next time!')
print('Final score: You - ' + str(user_score) +', Computer - ' + str(comp_score))
