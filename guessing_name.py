import random,math
random_number = math.ceil(random.random()*100)+1


# function to start the game
attempts = 0
while True:
    user_guessed = int(input("Please Guess the Number...."))
    attempts+=1
    if type(user_guessed)!=int:
        print("The input should be a number")
    if user_guessed==random_number:
        print("Correct","You took ",attempts," to Win.")
        break
    elif user_guessed>random_number:
        print("Too High")
    else:
        print("Too Low")