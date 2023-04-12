import random
import re
import sys


def main():
    words = ['able', 'abo ut', 'o unt']
    secret_word = random.choice(words)
    print('############################################################################', '\n'
          '#######################Welcome to Hangman###################################', '\n'
          '############################################################################')

    correct_guess = []
    incorrect_guess = []

    def calculate_total_guess(secret_word):
        if len(secret_word) <= 7:
            return len(secret_word)
        else:
            return 8

    def display_word(guess_word, correct_guess, incorrect_guess):

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
            print("Guessed letters are: ", correct_guess)
            print("Incorrect guessed letters are: ", incorrect_guess)

    def get_user_input(secret_word, total_guesses):

        guess_word = ""
        for letter in secret_word:
            if letter == " ":
                guess_word += " "
            else:
                guess_word += "*"
        print("The secret word is:", guess_word)

        while total_guesses > 0:
            print(f'You have total {total_guesses}  guesses!')
            input_letter = input("Guess the letter: ")

            if input_letter in secret_word:
                if input_letter in correct_guess:
                    print("Letter already guessed!")
                else:
                    correct_guess.append(input_letter)
                    print("Correct guess!")
                    display_word(guess_word, correct_guess, incorrect_guess)
            elif input_letter in incorrect_guess:
                print("Incorrect letter already guessed!")
            elif input_letter not in secret_word:
                total_guesses = total_guesses - 1
                print("Incorrect guess.")
                
                if total_guesses == 0:
                    print("You Lose!")
                    print("The word was: ", secret_word, '\n')
                else:
                    incorrect_guess.append(input_letter)
                    display_word(guess_word, correct_guess, incorrect_guess)



        while True:
            answer = input("Do you want to play again? Type YES or NO to exit: ")
            if answer.lower() == "no":
                sys.exit()
            elif answer.lower() == "yes":
                main()
    total_guesses = calculate_total_guess(secret_word)
    print('total_guesses: ', total_guesses)

    get_user_input(secret_word, total_guesses)


main()
