# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


## test "is_word_guessed" function
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # guessed_word: string
    guessed_word = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word += "_ "
        else:
            guessed_word += letter
    return guessed_word


# test "get_guessed_word" function
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # lower_case_letters: string
    lower_case_letters = string.ascii_lowercase
    # available_letters: string
    available_letters = ""
    for letter in lower_case_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters


# test "get_available_word" function
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_available_letters(letters_guessed))


def update_warning_guessing(warnings_remaining, guesses_remaining, warnings, guesses, guessed_word):
    """
    Update the warnings and guesses remaining, and tell the messages combined
    with guessed word
    :param warnings_remaining: int
    :param guesses_remaining: int
    :param warnings: int
    :param guesses: int
    :param guessed_word: str
    :return warnings_remaining: int:
    :return guesses_remaining: int:
    """
    if warnings != 0:
        if warnings_remaining != 0:
            warnings_remaining -= warnings
            print("You have", warnings_remaining, "warnings left:", guessed_word)
        else:
            guesses_remaining -= warnings
            print("You have no warnings left so you lose one guess:", guessed_word)
    else:
        guesses_remaining -= guesses
        print(guessed_word)
    return warnings_remaining, guesses_remaining



def minus_waring_or_guessing(warnings_left, guesses_left):
    """
    :param warings_left: int
    :param guessed_left: int
    :return same as param:
    """
    if warnings_left > 0:
        warnings_left -= 1
    else:
        guesses_left -= 1
    return warnings_left, guesses_left


def hangman(secret_word):
    """
    Starts up an interactive game of Hangman.
    :param secret_word: string, the secret word to guess.
    :return None: print to screen.
    """
    ##Initiate guesses left and warnings left.
    ##Tell the user the length of the secret word, and the game rounds start.
    ##Initiate letters guessed and letters available.
    ##Begin the rounds of guessing.
    ##Remind the user of how many guesses s/he has left after each guess
    ##Update all the letters the user has not guessed so far and
    ## tell the user.
    ##Ask the user to supply one guess at a time.
    ##Check whether the user input one symbol. Ask again otherwise.
    ##Check whether the input is alphabets. Warn him otherwise.
    ##Check whether the input is already in letters guessed. Warn him otherwise.
    ##Update warnings remaining or guesses remaining in the minus cases above.
    ##Update guesses remaining in the plus cases above.
    ##If the input passes all the above tests and put it into letters guessed.
    ##Check whether the guess is good. Tell him.
    ## 1. Good guess
    ## 2. Oops! That letter is not in my word
    ##Init or update the guessed word. Tell him in the same line.
    ##Check if the num of guesses left has reached zero. Then game over.
    ## Tell him the results and what the secret word is.
    ##Check whether the secret word is all in the letters guessed.
    ## If so, then game over. Ohterwise next round.
    ## Tell him the results and what the secret word is.
    ##Count the scores in this game. Tell him.
    ##
    ##
    ###Initiate guesses left and warnings left.
    guesses_remaining, warnings_remaining, = 6, 3
    ##Tell the user the length of the secret word, and the game rounds start.
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word)), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    ##Initiate letters guessed and letters available.
    # letters_guessed: list (of letters)
    letters_guessed = []
    # letters_available: string
    letters_available = get_available_letters(letters_guessed)
    # guessed_word: string, with _ and space
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    ##Begin the rounds of guessing.
    ##Remind the user of how many guesses s/he has left after each guess
    # game_over: bool, True if guessed or guess chances run out.
    lost, win = False, False
    while not game_over:
        print("-----------")
        print("You have", guesses_remaining, "guesses left")
    ##Update all the letters the user has not guessed so far and
    ## tell the user.
        letters_available = get_available_letters(letters_guessed)
        print("Available Letters:", letters_available)
    ##Ask the user to supply one guess at a time.
        guess_letter = input("Please guess a letter:").lower()
    ##Check whether the user input one symbol. Ask again otherwise.
        while not len(guess_letter) == 1:
            guess_letter = input("Please guess a letter:").lower()
    ##Check whether the input is alphabets. Warn him otherwise.
        if not guess_letter.isalpha():
            print("Oops! That is not a valid letter.")
            warnings_remaining, guesses_remaining = update_warning_guessing(warnings_remaining, guesses_remaining, 1, 0, guessed_word)
            break
    ##Check whether the input is already in letters guessed. Warn him otherwise.
        if guess_letter in letters_guessed:
            print("Oops! You've already guessed that letter.")
            warnings_remaining, guesses_remaining = update_warning_guessing(warnings_remaining, guesses_remaining, 1, 0, guessed_word)
            break
    ##Update warnings remaining or guesses remaining in the minus cases above.
        pass
    ##Update guesses remaining in the plus cases above.
        pass
    ##If the input passes all the above tests and put it into letters guessed.
    ## Update the guessed word.
        letters_guessed += guess_letter
        guessed_word = get_guessed_word(secret_word, letters_guessed)
    ##Check whether the guess is good. Tell him.
    ## 1. Good guess
    ## 2. Oops! That letter is not in my word
        if guess_letter in secret_word:
            print("Good guess:")
            warnings_remaining, guesses_remaining = update_warning_guessing(warnings_remaining, guesses_remaining, 0, 0, guessed_word)
        else:
            print("Oops! That letter is not in my word:")
            if guess_letter in "aeiou":
                warnings_remaining, guesses_remaining = update_warning_guessing(warnings_remaining, guesses_remaining, 0, 2, guessed_word)
            else:
                warnings_remaining, guesses_remaining = update_warning_guessing(warnings_remaining, guesses_remaining, 0, 1, guessed_word)
    ##Init or update the guessed word. Tell him in the same line.
        pass
    ##Check if the num of guesses left has reached zero. Then game over.
        if guessed_word == secret_word:
            win = True
        if guesses_remaining <= 0:
            lost = True
    ## Tell him the results and what the secret word is.
    print("-----------")
    if lost:
        print("Sorry, you ran out of guesses. The word was", secret_word)
    if win:
        print("Congratulations, you won!")
    ##Count the scores in this game. Tell him.
        unique_letters = []
        for letter in secret_word:
            if letter not in unique_letters:
                unique_letters += letter
        score = guesses_remaining * len(unique_letters)
        print("Your total score for this game is:", score)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
