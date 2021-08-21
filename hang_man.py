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
            word_as_list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                gussed = True

        elif len(guess) == len(word) and guess.isalpha():
        

        else:
            print("not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
        



display_hangman = [

    0: """
    ------------^
                |
                |
                |
                |
                |
    ------------O""",

    1: """
    ------------^
    |           |
                |
                |
                |
                |
    ------------O""",
    
    2: """
    ------------^
    |           |
    O           |
                |
                |
                |
    ------------O""",

    3: """
    ------------^
    |           |
    O           |
    |           |
                |
                |
    ------------O""",


    4: """
    ------------^
    |           |
    O           |
   /|           |
                |
                |
    ------------O""",

    5: """
    ------------^
    |           |
    O           |
   /|\          |
                |
                |
    ------------O""",









    



    













  

]





