import random
import re

def main():
    words = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after',
             'again', 'against', 'agreement', 'air', 'all', 'almost', 'among', 'amount', 'amusement', 'and', 'angle',
             'angry', 'animal', 'answer', 'ant']
    word = random.choice(words)
    print('Welcome to Hangman')
    guess_word = word.replace(word, len(word) * '*')
    print("The word is:", guess_word)
    correct_guess = []

    def total_guess(word):
        if len(word) <= 7:
            return len(word)
        else:
            return 8

    def display_word(guess_word, correct_guess):

        for input_letter in correct_guess:

            indicies = [i.start() for i in re.finditer(input_letter, word)]
            for x in indicies:
                guess_word = guess_word[:x] + input_letter + guess_word[x+1:]
        if guess_word == word:
            print("THE WORD IS:", guess_word)
            print("Hurray! YOU WON!")
            exit()
        else:
            print("\n""THE WORD IS:", guess_word)


    def check_inputletter(word, total_guesses, correct_guess):

        while total_guesses > 0:
            input_letter = input("Guess the letter: ")

            if input_letter in word:
                if input_letter in correct_guess:
                    print("Letter already guessed")
                else:
                    correct_guess.append(input_letter)
                    print("Correct guess!")
                    # print("correct guess", correct_guess)
                    display_word(guess_word, correct_guess)

            elif input_letter not in word:
                total_guesses = total_guesses - 1
                print(f'Incorrect guess. You have total {total_guesses} left')
                display_word(guess_word, correct_guess)
        print("You Lose!")
    total_guesses = total_guess(word)
    print('total_guesses: ', total_guesses)

    check_inputletter(word, total_guesses, correct_guess)


main()
