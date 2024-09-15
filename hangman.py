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
choose_word(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if ''.join(letters_guessed) == secret_word:
        return True
    else:
        return False
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = []
    out = []
    for i in letters_guessed:
        if i in secret_word:
            guessed.append(i)
    for j in secret_word:
        if j in guessed:
            out.append(j)
        else:
            out.append('_ ')
    return ''.join(out)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lk = list(string.ascii_lowercase)
    empt = []
    for i in lk:
        if i not in letters_guessed:
            empt.append(i)
    return ''.join(empt)
        

def uniq(secret_word):
    m = list(secret_word)
    for i in secret_word:
        m1 = m[:]
        m1.remove(i)
        if i in m1:
            m.remove(i)
    return len(m)
        


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word) ,'letters long. ')
    print('-------------')
    letters_guessed = []
    owe = ['a', 'e', 'i', 'o', 'u']
    gs = 6
    warn = 3
    while gs > 0:
        print('You have', gs, 'guesses left. ')
        print('Available letters:', get_available_letters(letters_guessed))
        get2 = get_available_letters(letters_guessed)[:]
        lets = letters_guessed[:]
        letters_guessed.append(str.lower(input('Please guess a letter:')))
        if letters_guessed[len(letters_guessed)-1] not in get2:
            warn = warn - 1
            if letters_guessed[len(letters_guessed)-1] not in lets:
                if warn < 0:
                    print('Oops! That is not a valid letter.')
                else:
                    print('Oops! That is not a valid letter. You have', warn, 'warnings left:')
            else:
                if warn < 0:
                    print('Oops! That is not a valid letter.')
                else:
                    print('Oops! You have already guessed that letter.', warn, 'warnings left:')
            if warn < 0:
                gs = gs - 1
                print('You have no warnings left :(, so you lose 1 guess')
        else:
            if letters_guessed[len(letters_guessed)-1] in secret_word:
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                if get_guessed_word(secret_word, letters_guessed) == secret_word:
                    print('-------------')
                    print('Congratulations, you won! ')
                    Tot = gs * uniq(secret_word)
                    return 'Your score is: ' + str(Tot)
            else: 
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                if letters_guessed[len(letters_guessed)-1] in owe:
                    gs = gs - 2
                else:
                    gs = gs - 1
    print('-------------')
    return 'Sorry, you ran out of guesses. The word was: ' + secret_word



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
    m = list(my_word)
    n = []
    for i in m:
        if i != ' ':
            n.append(i)
    wor = ''.join(n)       
    if len(wor) != len(other_word):
        return False
    else:
        for i in range(len(wor)):
            if wor[i] != other_word[i] and wor[i] != '_':
                return False
            elif wor[i] == '_' and other_word[i] in wor:
                return False
        return True
            
    
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    m = []
    n = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            m.append(i)
    if m == n:
        return 'No matches found'
    print('Possible word matches are:')           
    return ' '.join(m)



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
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word) ,'letters long. ')
    print('-------------')
    letters_guessed = []
    owe = ['a', 'e', 'i', 'o', 'u']
    gs = 6
    warn = 3
    while gs > 0:
        print('You have', gs, 'guesses left. ')
        print('Available letters:', get_available_letters(letters_guessed))
        get2 = get_available_letters(letters_guessed)[:]
        lets = letters_guessed[:]
        letters_guessed.append(str.lower(input('Please guess a letter:')))
        if letters_guessed[len(letters_guessed)-1] == '*':
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        elif letters_guessed[len(letters_guessed)-1] not in get2:
            warn = warn - 1
            if letters_guessed[len(letters_guessed)-1] not in lets:
                if warn < 0:
                    print('Oops! That is not a valid letter.')
                else:
                    print('Oops! That is not a valid letter. You have', warn, 'warnings left:')
            else:
                if warn < 0:
                    print('Oops! That is not a valid letter.')
                else:
                    print('Oops! You have already guessed that letter.', warn, 'warnings left:')
            if warn < 0:
                gs = gs - 1
                print('You have no warnings left :(, so you lose 1 guess.')
        else:
            if letters_guessed[len(letters_guessed)-1] in secret_word:
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                if get_guessed_word(secret_word, letters_guessed) == secret_word:
                    print('-------------')
                    print('Congratulations, you won! ')
                    Tot = gs * uniq(secret_word)
                    return 'Your score is: ' + str(Tot)
            else: 
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                if letters_guessed[len(letters_guessed)-1] in owe:
                    gs = gs - 2
                else:
                    gs = gs - 1
    print('-------------')
    return 'Sorry, you ran out of guesses. The word was: ' + secret_word


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    
    secret_word = choose_word(wordlist)
    print(hangman_with_hints(secret_word))


    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
