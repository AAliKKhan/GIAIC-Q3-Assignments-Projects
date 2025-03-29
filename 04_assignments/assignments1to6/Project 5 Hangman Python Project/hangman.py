
import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Ensure the word is in uppercase for consistency

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed

    lives = 6

    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current status
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
          
        # Display the current word with guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # End of game
    if lives == 0:
        print('You died, the word was', word)
    else:
        print('You guessed the word', word, '!')

# Run the game
hangman()
