import random
randomNumber = random.randint(1,100)
print(randomNumber)
userGuess = None
guessCount = 0
while(userGuess != randomNumber):
    userGuess = int(input("please enter your choice from 1 to 100:  "))
    guessCount +=1
    if userGuess==randomNumber:
       print("your guess is correct")

    else:
         if (userGuess < randomNumber):
           print("plz enter larger no")   
         else:
           print("plz enter lower no") 

print(f"you guessed number in {guessCount} guesses.")

with open("guessCount.txt","r") as f:
    hi_score = int(f.read()

if(hi_score > guessCount):
    print("you have broken the previous score")
    with open("guessCount.txt","w") as f:
         f.write(str(guessCount)
else:
    print("try again")         