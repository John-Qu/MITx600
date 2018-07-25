# -*- coding: utf-8 -*-
# Hangman game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True


def test_isWordGuessed(secretWord = "able", lettersGuessed = ['a', 'l', 'b', 'e']):
    print("Is the word '" + secretWord + "' guessed? " + str(isWordGuessed(secretWord, lettersGuessed)))


#test_isWordGuessed("a", [])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ''
    for l in secretWord:
        if l in lettersGuessed:
            guessed_word += l
        else:
            guessed_word += "_"
    return guessed_word


def test_getGuessedWord(secretWord="able", lettersGuessed = ['a', 'l']):
    print("Your guessed word is " + getGuessedWord(secretWord, lettersGuessed))


# test_getGuessedWord()


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = ""
    for i in range(97,123):
        if chr(i) not in lettersGuessed:
            available_letters += chr(i)
    return available_letters


def test_getAvailableLetters(lettersGuessed = ['a', 'l']):
    print('Available letters are ' + getAvailableLetters(lettersGuessed))


# test_getAvailableLetters()


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    guess_times_lefted = 8
    lettersGuessed = []
    guessed_word = getGuessedWord(secretWord, lettersGuessed)
    while guess_times_lefted > 0:
        print("-------------")
        print("You have " + str(guess_times_lefted) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed) + "")
        inputed_letter = input('Please guess a letter: ')
        if inputed_letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", guessed_word)
        else:
            lettersGuessed.append(inputed_letter)
            if inputed_letter in secretWord:
                guessed_word = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess:", guessed_word)
                if isWordGuessed(secretWord, lettersGuessed):
                    print("-------------")
                    print("Congratulations, you won!")
                    return
            else:
                print("Oops! That letter is not in my word:", guessed_word)
                guess_times_lefted -= 1
    print("-------------")
    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = "tact"
hangman(secretWord)
