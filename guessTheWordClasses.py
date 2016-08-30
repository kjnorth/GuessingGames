class InputValidation:

    def __init__(self, user_input):
        self._user_input = user_input

    def is_input_str(self):
        if self._user_input.isalpha():
            return True
        else:
            print("That\'s not a letter!")
            return False

    def is_input_only_one_character(self):
        if len(self._user_input) == 1:
            return True
        else:
            print("Please only enter one letter at a time")
            return False

    def get_user_input(self):
        return self._user_input


class CheckInputAgainstGuessWord:
    # inheritance is not the proper technique to use
    #
    def __init__(self, guess_word):
        # InputValidation.__init__(self, user_input)
        self._guess_word = guess_word

    def populate_underscores_and_spaces(self):

        blank_spaces_and_correct_guesses = []

        for i, char in enumerate(self._guess_word):
            global blank_spaces_and_correct_guesses

            if char != " ":
                blank_spaces_and_correct_guesses.insert(i, "_")
            elif char == " ":
                blank_spaces_and_correct_guesses.insert(i, " ")

    def populate_correct_guesses(self):
        global blank_spaces_and_correct_guesses

        for i, char in enumerate(self._guess_word):
            input = InputValidation.get_user_input() # can't call method like this
            if char == input:
                 print("correct character")

    @staticmethod
    def print_blank_spaces_and_correct_guesses():

        for i in blank_spaces_and_correct_guesses:
            print(i, end=" ")
