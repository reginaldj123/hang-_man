import string

LETTERS = list(string.ascii_lowercase)

"""def logic():


    word = "Secret" 
    allowed_errors = 7
    guesses = []
    done = False


    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")

            else:

                print("_", end=" ")

        print("")

        guesses = input(f"Allowd errors left {allowed_errors}, Next Guess: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

            if done:
                print(f"you found the word! it was {word}!")
            else
                print(f"Game over! The word was {word}!")
    
"""            
def yes_no(question):
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1","2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer


def users_guess(options):
    print("enter a letter from the availabe options")
    print(options)
    answer = input("enter your answer here \n").strip()
    while answer not in options:
        print(f"please choose from:",options)
        answer = input("enter your answer here \n").strip()
    return answer

def start_game():
    available_letters = LETTERS
    word = "Secret" 
    allowed_errors = 7
    guesses = []
    done = False
    guess = users_guess(available_letters)


def main():
    print("Welcome")
    answer = yes_no("do you want to play hang man ?")
    if answer == 1 :
        print("lets play")
    else: 
        print("goodbye")
    start_game()


  

main()