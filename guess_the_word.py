secret_word = "pizza"
user_guess = ""
count = 0

while user_guess != secret_word:        # loop will run until this statement is true
    user_input = input("Guess the word! ")
    user_guess = user_input.lower()
    count += 1                          # counts the number of guesses
    if user_guess == secret_word:       # automatically breaks the loop when condition is true
        print("Hurray! You've won! The answer is pizza.")
    elif 2 <= count < 4:     # After the 1st guess, the user is alerted about the wrong answer. only 4 guesses are
        print("Nope! try again!")       # allowed in total (count = (0-3)) and this statement is printed 2 times
    elif count == 1:                    # after the 1st guess the user is given a hint.
        print("Hint: It is a circle shaped food, cut up into 8 pieces of triangle served in a square box!")
        print("what's not to love about it?")
    elif count > 3:                     # after the 4th guess, if the answer is still wrong, the game ends.
        print("Sorry, you lose!! The word is pizza! So cheesy right?!")
        break                           # the break statement ends the loop once the game is over.

print("Thank you for playing the secret word guessing game!!")
