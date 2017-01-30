import random
import time

guesses = []

while len(guesses) < 6:
    try:
        guess = int(input("Please enter your chosen ball: "))
        if guess not in guesses:
            guesses.append(guess)
        else:
            print ("Sorry thats already one of your guesses!")
    except ValueError:
        print ("Sorry you must enter a number!")    
    
    
anotherGo = "y"

while anotherGo.lower() == "y":
    balls = []
    ballsDrawn = 0

    print ("\n** Welcome to the lottery **\n")

    error = True
    while error == True:
        try:
            ballsPossible = int(input("How many balls are in the machine? "))
            error = False
        except ValueError:
            print ("Sorry you must enter a number!")

    error = True
    while error == True:
        try:
            ballsToDraw = int(input("How many balls would you like to draw? "))
            error = False
        except ValueError:
            print ("Sorry you must enter a number!")
        

    while ballsDrawn < ballsToDraw:
        ball = random.randint(1,ballsPossible)
        if ball not in balls:
            print (ball)
            balls.append(ball)
            ballsDrawn += 1
            time.sleep(1)
        
    print ("** Draw complete!! **\n")

    correctGuesses = 0
    counter = 0

    while counter < len(guesses):        
        if guesses[counter] in balls:
            correctGuesses += 1
        counter = counter + 1

    if correctGuesses in [0,1]:
        print ("you win £0")
    elif correctGuesses == 3:
        print ("you win £100,000")
    elif correctGuesses == 4:
        print ("you win £500,000")
    elif correctGuesses == 5:
        print ("you win £1,000,000")
    else:
        print ("you win £10,000,000")
    anotherGo = input("Draw again? (y/n)")


