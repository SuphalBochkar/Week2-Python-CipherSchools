import random

# ~ DRY- Dont Repet Yore Self
# win=random.randint(1,100)
win=random.randint(1,100)
guess = 1
number = int(input("guess a number between 1 and 100: "))
game_over = False

while not game_over:
    if number == win:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if number < win:
            print("too low ")
        else:
            print( "too high")

        guess += 1
        number = int(input("guess again"))



