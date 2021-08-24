# Features

## Implemented Features

### Main Function
See if user wants to the play the game or quit
Makes use of yes_no function that handles validation of input for a yes or no question
Include Screenshot of user interface

### Guess Function
See if user imputed alpha keys or not
See if user is repeating a previous guess
See if guess is in word
See if guess is the word
If valid input but not in the word or the word, decrease tries left
Include Screenshot of user interface
Include screenshot of numeric input
Include screenshot of repeated guess
Include screenshot of each stage of hangman body

### Play function
Tells the user “Let’s play hangman”
Shows the hangman board and display_word
Calls the guess function until the game is over
Displays win or lose message
Calls main to see if user wants to play again
Include screenshot of let’s pay message
Include screenshots of each stage of hangman body
Include screenshot of lose message
Include screenshot of win message
## Future Features
Keep track of user’s wins and losses
Display stats at end of game for wins and losses
Collect user name
Store data in spreadsheet so we can look up past stats
Move game over logic out of play and into a model function



### Properties
**word**: randomly generated word from the WORD_LIST
**word_completion**: display of word as user guesses letters in it, unguessed letters are represented by the underscore symbol `_`
**guesed_letters**: empty array to track letters the user has guessed
**guessed**: True/False field to track if user has guessed the answer
**guessed_words**: tempy array to track words the user has guessed
**trials**: tracker for bad guesses that helps show right display of hangman gallows

### Functions
**init**: initializes the game with empty trackers, 6 trials, and a random word
**guess**: validates user input and updates trials, guessed_letters, guessed_words as needed and displays updated game board once a valid guess has been inputted

## Libraries used
None, I used standard libraries for my initial program: random and string


### Validation and testing
<img src="blob:chrome-untrusted://media-app/c7cf77a0-257d-4235-8977-fc50f5ab520c" alt="checking code through pep8.png"/>![image](https://user-images.githubusercontent.com/80925381/130699981-e6a471e6-99da-4603-8b85-0ffff7333616.png)

Manual Testing
Bullet point out things:
Yes not question, put in nothing
Yes no question, put in negative number
Yes no question, put in letters
Guess same letter
Guess same word
Guess don’t enter anything
Guess enter numbers
Guess enter word with number
Guess enter word with space

### Defects

Wrong gallows seen, order seems reversed
User has to run program again if they want to play another game
game over messages not displaying
Not seeing the you already guessed that messaging
PEP8 line too long
PEP8 whitespace in empty line
PEP8 empty line count
PEP8 end of file no new line
