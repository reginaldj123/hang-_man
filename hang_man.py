import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    gussed = False
    gussed_letters = []
    guessed_word = []
    tries = 6
    print("lets play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and trials > 0:
        guess = input("please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
        if guess in gussed_letters
        print("you already guessed the letter",guess)
        elif guess not in word:
            print(guess,"is not in the word.")
            tries -= 1
            gussed_letters.append(guess)
        else:
            print("good job," guess, "is in the word")
            gussed_letters.append(guess)

        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("not a valid guess.")
        



def display_hangman = [

]





