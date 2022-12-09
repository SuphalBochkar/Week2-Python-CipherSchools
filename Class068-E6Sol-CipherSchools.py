import random

i=0
win = random.randint(0,100)
#! M-1
while True:
    u=int(input("Num: "))
    if u==win:
        (f"You Won!!!..... You played {i} times")
        break
    else:
        if u<win:
            print("Too low")
        else :
            print("Too high")
    i+=1


    
    
# while True:
#     u=int(input("Num: "))
#     if u<win:
#         print("Too low")
#     elif u>win :
#         print("Too high")
#     else:
#         print(f"You Won!!!..... You played {i} times")
#         break
#     i+=1