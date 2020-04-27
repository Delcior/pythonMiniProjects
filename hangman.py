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


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            pass
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    container = []
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            container.append(secret_word[i])
        else:
            container.append("_ ")
    return "".join(container)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    container = list(string.ascii_lowercase)

    for i in range(len(letters_guessed)):
        if letters_guessed[i] in container:
            container.remove(letters_guessed[i])

    return "".join(container)


def hangman(secret_word):
    guesses_left = int(input("Welcome to the game Hangman!\nHow many guesses you want:"))
    warnings_left = 3
    vovels = "aeiou"
    letters_guessed = []
    print("I am thinking of a word that is", len(secret_word), "letters long"
                                                               "\nYou have", warnings_left, "warnings_left left")

    while True:
        print("---------------------\nYou have", guesses_left, "guesses left.\nAvailable letters:",
              get_available_letters(letters_guessed))
        guess = str.lower(input("Please guess a letter: "))
        if guess in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have", warnings_left, "warnings_left left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings_left left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        elif str.isalpha(guess):
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                if guess in vovels and guess not in letters_guessed:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses_left -= 2
                else:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses_left -= 1
            letters_guessed.append(guess)
        else:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings_left left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings_left left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))

        if guesses_left == 0:
            print("---------------\nSorry, you ran out of guesses.The word was:", secret_word)
            break
        elif is_word_guessed(secret_word, letters_guessed):
            print("---------------\nCongratulations! You won!\nYour total score for this game is:",
                  guesses_left * len(set(secret_word)))
            break


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = "".join(my_word.split(' '))
    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] is not "_":
            if my_word[i] != other_word[i]:
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
    '''
    space_counter = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=" ")
            space_counter += 1
            if space_counter == 20:
                print()
                space_counter = 0


def hangman_with_hints(secret_word):
    guesses_left = int(input("Welcome to the game Hangman!\nHow many guesses you want:"))
    warnings_left = 3
    vovels = "aeiou"
    letters_guessed = []
    print("I am thinking of a word that is", len(secret_word), "letters long\nYou have",
          warnings_left, "warnings_left left")

    while True:
        print("\n---------------------\nYou have", guesses_left, "guesses left.\nAvailable letters:",
              get_available_letters(letters_guessed), end="")
        guess = str.lower(input("\nPlease guess a letter: "))
        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have", warnings_left, "warnings_left left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings_left left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        elif str.isalpha(guess):
            if guess in secret_word:
                letters_guessed.append(guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                if guess in vovels and guess not in letters_guessed:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses_left -= 2
                else:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses_left -= 1
        else:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings_left left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings_left left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))

        if guesses_left == 0:
            print("---------------\nSorry, you ran out of guesses.The word was:", secret_word)
            break
        elif is_word_guessed(secret_word, letters_guessed):
            print("---------------\nCongratulations! You won!\nYour total score for this game is:",
                  guesses_left * len(set(secret_word)))
            break


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    print("Which version of the game you want to play?\n[1] with hints\n[2] without hints")
    version = input()

    if version == "1":
        hangman(secret_word)
    else:
        hangman_with_hints(secret_word)
