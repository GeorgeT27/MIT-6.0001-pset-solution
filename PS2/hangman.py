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
  for word in secret_word:
    if word not in letters_guessed:
      return False
  return True

  '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct_letter=[]
    for word in secret_word:
      if word in letters_guessed:
        correct_letter.append(word)
      else:
        correct_letter.append('_ ')
    return ''.join(correct_letter)


# secret_word = 'pear'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed))   



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alp_letter=string.ascii_lowercase
    for letter in letters_guessed:
      alp_letter=alp_letter.replace(letter,'')
    return alp_letter
  
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print (get_available_letters(letters_guessed) )
    



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    vowels = ['a', 'e', 'i', 'o', 'u']
    run=True
    guess=6
    print("Welcome to the game Hangman!")
    print(f'I am thinking of a word that is {len(secret_word)} character long.')
    print("----------")
    letters_guessed=[]
    warning=3
    while run:
      if guess<=0:
        run=False
        print('You have used all the chances!')
        print(f'The correct word is {secret_word}')
        break
      print(f'You have {guess} guess left')
      print(f'Available letter are:{get_available_letters(letters_guessed)}',2*'\n')
      letter=input('Please input a guess letter:').lower()
      if not letter.isalpha():
        warning-=1
        print("That is not a valid input! \n Please only input an alphabet!")
        if warning<0:
          guess-=1
          warning=0
        print('Have {} warning left'.format(warning))
        continue
      if letter in letters_guessed:
        warning-=1
        if warning<0:
          guess-=1
          warning=0
        print(f"That is the repeated guess! \n You have {warning} left!")
      else:
        letters_guessed.append(letter)
      if is_word_guessed(secret_word,letters_guessed):
        print(f"You get the correct word!----{secret_word}")
        unique_letter=set(secret_word)
        total_score=guess*len(unique_letter)
        run=False
        return total_score
      
      if letter in secret_word:
        print(f'Good guess:{get_guessed_word(secret_word,letters_guessed)}')
      else:
        print("That's not the correct letter!")
        print(f'Current guess is {get_guessed_word(secret_word,letters_guessed)}')
        if letter in vowels:
          guess-=2
        else:
          guess-=1
      
      
      
# print(hangman('hangman')  )    

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
    modi_my_word=my_word.replace(" ","")#get rid of all the space
    current_letter=set(modi_my_word)#This will contain _
    try:
      current_letter.remove("_")
    except ValueError:
      pass
    
    if len(modi_my_word)!=len(other_word):
      return False
    else:
      for index,chr in enumerate(modi_my_word):
        if chr!="_":
          if chr!=other_word[index]:
            return False
        else:
          if other_word[index] in current_letter:
            return False
      return True
    
#print(match_with_gaps("p_ ar ", "pear"))
    


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
    possible_list=[]
    for word in load_words():
      if match_with_gaps(my_word,word):
        possible_list.append(word)
        
    return possible_list
            
        

    
          
#print(show_possible_matches("t_ _ t"))



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
    vowels = ['a', 'e', 'i', 'o', 'u']
    run=True
    guess=6
    print("Welcome to the game Hangman!")
    print(f'I am thinking of a word that is {len(secret_word)} character long.')
    print("----------")
    letters_guessed=[]
    warning=3
    while run:
      if guess<=0:
        run=False
        print('You have used all the chances!')
        print(f'The correct word is {secret_word}')
        break
      print(f'You have {guess} guess left')
      print(f'Available letter are:{get_available_letters(letters_guessed)}',2*'\n')
      letter=input('Please input a guess letter:').lower()
      if not letter.isalpha() and letter!="*":
        warning-=1
        print("That is not a valid input! \n Please only input an alphabet!")
        if warning<0:
          guess-=1
          warning=0
        print('Have {} warning left'.format(warning))
        continue
      elif letter=="*":
        print("Relevant words are:")
        print(show_possible_matches(get_guessed_word(secret_word,letters_guessed)))
        continue
      if letter in letters_guessed:
        warning-=1
        if warning<0:
          guess-=1
          warning=0
        print(f"That is the repeated guess! \n You have {warning} left!")
      else:
        letters_guessed.append(letter)
      if is_word_guessed(secret_word,letters_guessed):
        print(f"You get the correct word!----{secret_word}")
        unique_letter=set(secret_word)
        total_score=guess*len(unique_letter)
        run=False
        return total_score
      
      if letter in secret_word:
        print(f'Good guess:{get_guessed_word(secret_word,letters_guessed)}')
      else:
        print("That's not the correct letter!")
        print(f'Current guess is {get_guessed_word(secret_word,letters_guessed)}')
        if letter in vowels:
          guess-=2
        else:
          guess-=1
      



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
# #     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
