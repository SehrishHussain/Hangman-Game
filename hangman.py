import random
import re

def main():
    words = ['able', 'abo ut', 'acco unt']
    secret_word = random.choice(words)
    print('Welcome to Hangman')

    correct_guess = []

    def calculate_total_guess(word):
        if len(word) <= 7:
            return len(word)
        else:
            return 8

    def display_word(guess_word, correct_guess):

        for input_letter in correct_guess:

            indicies = [i.start() for i in re.finditer(input_letter, secret_word)]
            for x in indicies:
                guess_word = guess_word[:x] + input_letter + guess_word[x+1:]
        if guess_word == secret_word:
            print("THE WORD IS:", guess_word)
            print("Hurray! YOU WON!")
            exit()
        else:
            print("\n""THE WORD IS:", guess_word)


    def get_user_input(secret_word, total_guesses, correct_guess):
        # guess_word = secret_word.replace(secret_word, len(secret_word) * '*')
        guess_word = ""
        for letter in secret_word:
            if letter == " ":
                guess_word += " "
            else:
                guess_word += "*"
        print("The secret word is:", guess_word)

        while total_guesses > 0:
            input_letter = input("Guess the letter: ")

            if input_letter in secret_word:
                if input_letter in correct_guess:
                    print("Letter already guessed")
                    print("Guessed letters are: ", correct_guess, '\n')
                else:
                    correct_guess.append(input_letter)
                    print("Correct guess!")
                    print("Guessed letters are: ", correct_guess)
                    display_word(guess_word, correct_guess)

            elif input_letter not in secret_word:
                total_guesses = total_guesses - 1
                print(f'Incorrect guess. You have total {total_guesses} left')
                display_word(guess_word, correct_guess)
        print("You Lose!")
    total_guesses = calculate_total_guess(secret_word)
    print('total_guesses: ', total_guesses)

    get_user_input(secret_word, total_guesses, correct_guess)


main()
