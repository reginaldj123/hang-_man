import random
from constants import WORD_LIST, DISPLAY_HANGMAN


class Game:
    def __init__(self):
        """
        Initialize the Game
        1. randomly select a word from WORD_LIST
        2. update the word_completion to all dashes of the length of the word
        3. set trials to 6
        4. set guessed_letters to empty array
        5. set guessed to false
        6. set guessed_words to empty array
        """
        self.word = random.choice(WORD_LIST).upper()
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.guessed = False
        self.guessed_words = []
        self.trials = 6


def guess(self):
    """
    Get input from the user
    check if it's a letter or a word or invalid
    if letter, see if letter is in word or was already guessed
    if word, see if word is correct or was already guessed
    if bad guess, decrease trials
    track guessed letters and words as needed
    """
    guess = input("please guess a letter or word:\n").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in self.guessed_letters:
            print("you already guessed the letter " + guess)
        elif guess not in self.word:
            print(guess + " is not in the word.")
            self.trials -= 1
            self.guessed_letters.append(guess)
            else:
                print("good job," + guess + "is in the word")
                self.guessed_letters.append(guess)
                word_as_list = list(self.word_completion)
                indices = [
                    i for i, letter in enumerate(game.word) if letter == guess
                ]
                for index in indices:
                    word_as_list[index] = guess
                self.word_completion = "".join(word_as_list)
                if "_" not in self.word_completion:
                    self.guessed = True
        elif len(guess) > 0 and guess.isalpha():
            if guess in game.guessed_words:
                print("You already guessed the word " + guess)
            elif guess != self.word:
                print(guess + " is not the word.")
                self.trials -= 1
                game.guessed_words.append(guess)
            else:
                self.guessed = True
                self.word_completion = self.word

        else:
            print("not a valid guess.")
        print(DISPLAY_HANGMAN[game.trials])
        print(self.word_completion)
        print("\n")


def get_word():
    """
    creating the hidden word for game out of words list
    """
    word = random.choice(WORD_LIST)
    return word.upper()


def play():
    """
    Initiliaze the game object
    Check what the program should do if guess is right or wrong,
    Check user won or game is over
    Ask if they want to play again
    """
    game = Game()
    print("lets play hangman!")
    print(DISPLAY_HANGMAN[self.trials])
    print(game.word_completion)
    print("\n")
    while not game.guessed and self.trials > 0:     
  
        
if game.guessed:
    print("congratulations you got the word, " + self.word)
    else:
        print("sorry you ran out of tries the word was, " + self.word)
    main()


def yes_no(question):
    """
    creating the introducing question input choice answer
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1", "2"): 
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer


def main():
    """
    main program to see if user wants to play hang m an yes or no
    """
    answer = yes_no("do you want to play hang man ?")
    if answer == "1":
        play()
    else:
        print("goodbye")


if __name__ == "__main__":
    main()