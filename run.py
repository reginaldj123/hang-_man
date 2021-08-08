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
        done = True