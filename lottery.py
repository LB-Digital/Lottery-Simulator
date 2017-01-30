import random
import time

balls = []
ballsDrawn = 0

print("*** Initial Lottery Configuration ***")  # game options are set outside the main 'anotherGo' loop as they should be same every draw for the user

error = True
while error == True:
    try:
        ballsPossible = int(input("How many balls are in the machine? "))
        if ballsPossible < 1:   # ensure number of balls entered is positive
            error = True
        else:
            error = False
    except ValueError:
        print ("Sorry you must enter a number!")

error = True
while error == True:
    try:
        ballsToDraw = int(input("How many balls would you like to draw? "))
        if ballsToDraw < 1 or ballsToDraw > ballsPossible:   #ensure number of balls entered is positive and not greater than number of balls in machine
            error = True
        else:
            error = False
    except ValueError:
        print ("Sorry you must enter a valid integer!")     # changed error message from 'number' to 'positive integer' to improve UX of program



anotherGo = "y"
guesses = []
while anotherGo == "y":     # remove .lower() and added to input later on to improve code efficiency

    print ("\n** Welcome to the lottery **\n")

    # Nested guess choosing loop within 'anotherGo' loop so that user can choose new numbers each time
    if guesses != []:   # Added option to use same balls as last time if not their first draw to improve UX
        sameGuesses = ""
        while sameGuesses not in ["y","n"]:
            sameGuesses = input("Would you like to choose the same balls as last time? (y/n) ").lower()
    else:
        for guessNum in range(ballsToDraw):  # Changed from while loop to for loop due to known number of iterations
            error = True
            while error == True:  # loops until a valid positive integer is entered less than or equal to number of balls in machine
                try:
                    guess = int(
                        input("Please enter ball choice {}: ".format(guessNum + 1)))  # displays choice number to improve UX
                    if guess in guesses:
                        print("Sorry that's already one of your guesses!")  # grammar: missing apostrophe in "that's"
                        error = True
                    elif guess < 1 or guess > ballsPossible:  # ensure guess is positive and not greater than number of balls in machine
                        print("Sorry, your guess must be a positive integer between 1 and {}".format(ballsPossible))
                        error = True
                    else:
                        guesses.append(guess)
                        error = False  # will exit the while loop
                except ValueError:
                    print("Sorry you must enter a number!")
                    error = True



    for drawNum in range(ballsToDraw):  # Changed from while loop to for loop due to known number of iterations

        ball = random.randint(1,ballsPossible)
        while ball in balls:    # added while loop to keep generating random integer until not a duplicate
            ball = random.randint(1,ballsPossible)

        print (ball)
        balls.append(ball)
        ballsDrawn += 1
        time.sleep(1)
        
    print ("** Draw complete!! **\n")

    correctGuesses = 0
    counter = 0

    for guess in guesses:   # changed from while to foreach loop as known number of elements in array object
        if guess in balls:
            correctGuesses += 1

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

    anotherGo = ""
    while anotherGo not in ["y","n"]:
        anotherGo = input("Draw again? (y/n) ").lower()     # added a space before input.  Reason: Come on, it looks weird without it :)