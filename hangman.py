import random
import re
import sys


def select_word():
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
    print("SECRET WORD",secret_word)
    return secret_word


def calculate_total_guess(secret_word):

    if len(secret_word) <= 7:
        return len(secret_word)
    else:
        return 8


def display_word(guess_word, correct_guess, incorrect_guess, secret_word):

    for input_letter in correct_guess:
        indicies = [i.start() for i in re.finditer(input_letter, secret_word)]
        for x in indicies:
            guess_word = guess_word[:x] + input_letter + guess_word[x+1:]
    if guess_word == secret_word:
        print(f"THE WORD IS: {guess_word}")
        print("Hurray! YOU WON!")
        want_to_play_again()
    else:
        print(f"\nTHE WORD IS: {guess_word}")
        print(f"Guessed letters are: {correct_guess}")
        print(f"Incorrect guessed letters are: {incorrect_guess}")


def get_user_input(secret_word, total_guesses, correct_guess, incorrect_guess):

    guess_word = ""
    for letter in secret_word:
        if letter == " ":
            guess_word += " "
        else:
            guess_word += "*"

    print("The secret word is:", guess_word)

    while total_guesses > 0:
        while True:
            print(f"You have total {total_guesses}  guesses!")
            input_letter = input("Guess the letter: ")
            input_letter = input_letter.lower()
            if not input_letter.isalpha() or len(input_letter) != 1:
                print("Invalid input. Please enter a single alphabet!")
            else:
                break

        if input_letter in secret_word:
            if input_letter in correct_guess:
                print("Letter already guessed!")
            else:
                correct_guess.append(input_letter)
                print("Correct guess!")
                display_word(guess_word, correct_guess, incorrect_guess, secret_word)

        elif input_letter in incorrect_guess:
            print("Incorrect letter already guessed!")

        elif input_letter not in secret_word:
            total_guesses -= 1
            print("Incorrect guess.")

            if total_guesses == 0:
                print("You Lose!")
                print(f"The word was: {secret_word}")
            else:
                incorrect_guess.append(input_letter)
                display_word(guess_word, correct_guess, incorrect_guess, secret_word)

    want_to_play_again()


def want_to_play_again():
    while True:
        answer = input("\nDo you want to play again? Type YES or NO to exit: ")
        if answer.lower() == "no":
            sys.exit()
        elif answer.lower() == "yes":
            main()


def main():
    print('############################################################################', '\n'
          '####################### Welcome to Hangman #################################', '\n'
          '############################################################################')
    correct_guess = []
    incorrect_guess = []
    secret_word = select_word()
    total_guesses = calculate_total_guess(secret_word)
    get_user_input(secret_word, total_guesses, correct_guess, incorrect_guess)


if __name__ == "__main__":
    main()
