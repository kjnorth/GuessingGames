import guessTheWordClasses

if __name__ == '__main__':

    guess_word = guessTheWordClasses.CheckInputAgainstGuessWord("Juan Carlos")
    print("Guess the word!")

    while True:
        guess_word.populate_underscores_and_spaces()
        guess_word.print_blank_spaces_and_correct_guesses()
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