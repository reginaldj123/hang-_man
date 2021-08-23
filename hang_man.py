import random
from words import word_list
display_hangman = {

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
   /|\\          | 
                |
                |
    ------------O""",

    6: """
    ------------^
    |           |
    O           |
   /|\\          |
     \\          |
                |
    ------------O""",

    7: """
    ------------^
    |           |
    O           |
   /|\\          |
   / \\         |
                |
    ------------O""",
}


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    trials = 6
    print("lets play hangman!")
    print(display_hangman[trials])
    print(word_completion)
    print("\n")
    while not guessed and trials > 0:
        guess = input("please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter", guess)
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
                 
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
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
    

       
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()