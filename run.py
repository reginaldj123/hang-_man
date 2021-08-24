import random
from words import word_list
"""
creting the hangman wrong answer game display stages
"""
display_hangman = {
    

    7: """
    ------------^
                |
                |
                |
                |
                |
    ------------O""",

    6: """
    ------------^
    |           |
                |
                |
                |
                |
    ------------O""",

    5: """
    ------------^
    |           |
    O           |
                |
                |
                |
    ------------O""",

    4: """
    ------------^
    |           |
    O           |
    |           |
                |
                |
    ------------O""",

    3: """
    ------------^
    |           |
    O           |
   /|           |
                |
                |
    ------------O""",

    2: """
    ------------^
    |           |
    O           |
   /|\\          | 
                |
                |
    ------------O""",

    1: """
    ------------^
    |           |
    O           |
   /|\\          |
     \\          |
                |
    ------------O""",

    0: """
    ------------^
    |           |
    O           |
   /|\\          |
   / \\         |
                |
    ------------O""",
}


def get_word():
    """
    creating the hidden word for game out of words list
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    creating the number of trials the user will get.
    creating where the letters will show up in the game.
    creating the option to guess words and letters.
    estabishing what the program should do if guess is right or wrong,
    """
    word_completion = "_" * len(word)    
    guessed_letters = []
    guessed = False
    guessed_words = []
    trials = 6
    print("lets play hangman!")
    print(display_hangman[trials])
    print(word_completion)
    print("\n")
    while not guessed and trials > 0:
        guess = input("please guess a letter or word:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter " + guess)
            elif guess not in word:
                print(guess + " is not in the word.")
                trials -= 1
                guessed_letters.append(guess)
            else:
                print("good job," + guess + "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                 
        elif len(guess) > 0 and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word " + guess)
            elif guess != word:
                print(guess + " is not the word.")
                trials -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("not a valid guess.")
        print(display_hangman[trials])
        print(word_completion)
        print("\n")
    if guessed:
        print("congratulations you got the word, " + word)
    else:
        print("sorry you ran out of tries the word was, " + word)
    
def yes_no(question):
    """
    creating the introducing question input choice answer
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1","2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer
       
def main():
    """
    main program to see if user wants to play hang m an yes or no
    """
    answer = yes_no("do you want to play hang man ?")
    if answer == "1":
        word = get_word()
        play(word)
    else:
        print("goodbye")


if __name__ == "__main__":
    main()