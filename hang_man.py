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

def display_hangman = [

]





