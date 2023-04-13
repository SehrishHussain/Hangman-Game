import random
import re
import sys


def select_word():       # pick a random word or phrase the below lists

    words = ['cat', 'dog', 'book', 'sun', 'rain', 'tree', 'mountain', 'ocean', 'moon', 'star',
             'beach', 'bird', 'cloud', 'coffee', 'computer', 'flower', 'friend', 'guitar', 'home', 'music',
             'phone', 'pizza', 'river', 'smile', 'snow', 'song', 'water', 'wine', 'world',
             'angel', 'apple', 'banana', 'butterfly', 'cake', 'camera', 'candle', 'dragon', 'elephant', 'fire',
             'heart', 'horse', 'ice', 'key', 'light', 'love', 'magic', 'mirror', 'peace', 'sky']
    phrases = ['love hurts sometimes more',
               'cats purr dogs bark',
               'rain falls plants grow',
               'life is tough survive it',
               'time flies memories last',
               'dreams come true occasionally',
               'money talks wealth whispers',
               'silence is golden sometimes',
               'mind over matter',
               'hope springs eternal',
               'actions speak louder',
               'all for one one for all',
               'less is more sometimes',
               'what goes around comes',
               'knowledge is power truly',
               'beauty is in simplicity',
               'truth is stranger than',
               'curiosity killed the cat',
               'live and learn hopefully',
               'actions speak louder always']

    combined_list = words + phrases
    random.shuffle(combined_list)
    secret_word = random.choice(combined_list)
    print ("SECRET WORD", secret_word)
    return secret_word


def calculate_total_guess(secret_word):

    if len(secret_word) <= 7:
        return len(secret_word)
    else:
        return 8                # returns number of guesses equals len(secret_word) or 8 for longer words/phrases


def get_user_input(secret_word, total_guesses, correct_guess, incorrect_guess):

    guess_word = ""                 # guess_word is the display word the user sees e.g s*a*e
    for letter in secret_word:
        if letter == " ":           # replacing spaces in secret_word with spaces in guess_word
            guess_word += " "
        else:
            guess_word += "*"       # replacing alphabets with **

    print("The secret word is:", guess_word)

    while total_guesses > 0:
        while True:
            print(f"You have total {total_guesses}  guesses!")
            input_letter = input("Guess the letter: ")  # get the user input
            input_letter = input_letter.lower()
            if not input_letter.isalpha() or len(input_letter) != 1:    # input validation
                print("Invalid input. Please enter a single alphabet!")
            else:
                break

        if input_letter in secret_word:     # checks on input letter
            if input_letter in correct_guess:       # check if input letter is already guessed
                print("Letter already guessed!")
            else:
                correct_guess.append(input_letter)      # store input letter in correct_guess list
                print("Correct guess!")
                display_word(guess_word, correct_guess, incorrect_guess, secret_word)   # display word

        elif input_letter in incorrect_guess:           # check if input letter is incorrect and is already guessed
            print("Incorrect letter already guessed!")

        elif input_letter not in secret_word:           # check if input_letter is incorrect
            total_guesses -= 1                          # decrement total_guesses
            print("Incorrect guess.")

            if total_guesses == 0:
                print("You Lose!")
                print(f"The word was: {secret_word}")
            else:
                incorrect_guess.append(input_letter)     # append input_letter in incorrect_guess list
                display_word(guess_word, correct_guess, incorrect_guess, secret_word)   # display incorrect list



    want_to_play_again()


def display_word(guess_word, correct_guess, incorrect_guess, secret_word):

    for input_letter in correct_guess:      # replacing * in guess_word with correct alphabet in respective index
        indicies = [i.start() for i in re.finditer(input_letter, secret_word)]
        for x in indicies:
            guess_word = guess_word[:x] + input_letter + guess_word[x+1:]
    if guess_word == secret_word:           # once user guesses all the letters and display fn is called, it checks if all the letters are guessed. Thus user wins.
        print(f"THE WORD IS: {guess_word}")
        print("Hurray! YOU WON!")
        want_to_play_again()
    else:
        print(f"\nTHE WORD IS: {guess_word}")   # else the guess_word and list of correct/incorrect letters are shown to user
        print(f"Guessed letters are: {correct_guess}")
        print(f"Incorrect guessed letters are: {incorrect_guess}")


def want_to_play_again():
    while True:
        answer = input("\nDo you want to play again? Type YES or NO to exit: ")
        if answer.upper() == "NO":
            sys.exit()
        elif answer.upper() == "YES":
            main()


def main():
    print('############################################################################', '\n'
          '####################### Welcome to Hangman #################################', '\n'
          '############################################################################')
    correct_guess = []          # initialized empty lists
    incorrect_guess = []
    secret_word = select_word()     # secret_word is chosen
    total_guesses = calculate_total_guess(secret_word)      # total guesses calculated
    get_user_input(secret_word, total_guesses, correct_guess, incorrect_guess)  # call for user input


if __name__ == "__main__":
    main()
