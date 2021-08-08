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
    

        guesss = input(f"Allowd errors left {allowed_errors}, Nex Guess: ")
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
   
        