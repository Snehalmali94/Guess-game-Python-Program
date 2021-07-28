import random
randNumber = random.randint(1,100)
print(randNumber)

userGuess = None
guess = 0

while(userGuess != randNumber):
    userGuess = int(input("please enter number:  "))
    guess += 1
    if(userGuess == randNumber):
        print("your guess is correct.")
    else:
         if(userGuess > randNumber):
            print("your guess is wrong.please enter smaller number")

         else:
            print("your guess is wrong .please enter larger number")


print(f"you guessed the number in {guess} guesses ")


with open("hi_score.txt") as f:
    hi_score = int(f.read())

if hi_score > guess:
    print("you have broken the previous score")
    with open("hi_score.txt","w") as f:
         f.write(str(guess))
         

