import guessTheWordClasses

if __name__ == '__main__':

    guess_word = guessTheWordClasses.CheckInputAgainstGuessWord("Max the cat")
    print("Guess the word!")
    guess_word.populate_underscores_and_spaces()

    while True:
        guess_word.print_underscores_spaces_and_correct_guesses()
        if guess_word.check_if_won():
            break
        else:
            pass
        user_input = input("\nEnter a letter")
        input_validation = guessTheWordClasses.InputValidation(user_input)

        is_str = input_validation.is_input_str()
        if is_str:
            pass
        else:
            continue

        is_only_character = input_validation.is_input_only_one_character()
        if is_only_character:
            pass
        else:
            continue

        guess_word.populate_correct_guesses()
