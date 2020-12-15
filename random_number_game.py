"""
This program will serve as a form of entertainment for the user.

A random number will first be selected between 0 and 100.
The user is allowed an unlimited number of guesses to guess the correct number.

If the user guesses a lower amount than the selected number, the program will print to
the user that the guess is "too low."

If the user guesses a higher amount than the selected number, the program will print to
the user that the guess is "too high."

If the user guesses a lower amount than zero or a higher amount than one hundred, the program will print to the user that
the guess is "invalid."

If the user inputs their guess in a word format, the program will print to the user
"You did not enter a number".

Once the user guesses the correct number, the program will print to the user "Correct!"
and will report how many guesses they attempted.
"""

"""
from random import randint
from itertools import count

print "Hello human, what is your name?"
myName = input()

print "Well, " + myName + ", I want to play a game." + 
"I am thinking of a number that you need to solve for." +
"For each incorrect answer, you will lose $1 from your checking account. I know where you live..."

#Generate a Random Number between 0 and 100 and store it as 'numberToguess'

Set function name as numberToGuess and constrained to (minimum, maximum)
    numberToGuess = random value between 0 and 100
    Start for loop as "for tries in count"
      Convert user input into valid integer #Get the user to enter a number using the 'input' function and
                                        #convert in to an integer using the 'int' function
    Try userGuess = input converted to integer #Compare this number, userGuess, with the numberToGuess -
      if userGuess is lower than zero
          print "You entered an invalid number!" + " No numbers less than 0. Try again."
      if else userGuess is higher than numberToGuess # Display the right message if the userGuess is greater than, lower than or equal to the numberToGuess
          print "Too high!"
      if else userGuess is lower than numberToGuess
          print "Too low!"
      if else userGuess is equal to numberToguess  
          return tries
    Except value error
      print "You did not enter a number! Please enter a valid number:"

print "Correct! You took (number of attempted guesses) guesses."


#End of game - exit the for loop

"""
