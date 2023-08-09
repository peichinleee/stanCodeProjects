"""
File: hangman.py
Name: Pei
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game with the number of lives by constant: N_TURNS.
    Illegal format will be checked and ask for a new input.
    No matter win or lose, the program reveals the answer in the end.
    """
    guess = ''
    ans = random_word()
    life = N_TURNS
    for i in range(len(ans)):
        guess += '-'
    print('The word looks like ' + guess)
    print('You have ' + str(life) + ' wrong guesses left.')
    while True:
        # user makes a guess
        ch = input('Your guess: ')
        ch = ch.upper()
        if ch.isalpha() is False or len(ch) > 1:
            print('Illegal format.')
        elif ch in ans:
            # correct guess, replace the input_ch into guess
            print('You are correct!')
            guess = replace(guess, ch, ans)
            if guess == ans:
                # break if user wins the game
                print('You win!!')
                break
            print('The word looks like ' + guess)
            print('You have ' + str(life) + ' wrong guesses left.')
        else:
            # wrong guess
            life -= 1
            print("There is no " + ch + "'s in the word.")
            if life == 0:
                # break if user lost the game
                print('You are completely hung : (')
                break
            print('The word looks like ' + guess)
            print('You have ' + str(life) + ' wrong guesses left.')
    print('The word was: ' + ans)


def replace(guess, ch, ans):
    """
    The function updates the correct guess: input_ch into the dashed sequence.
    """
    new_guess = ''
    for i in range(len(ans)):
        if ans[i] == ch:
            new_guess += ch
        else:
            new_guess += guess[i]
    return new_guess


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
