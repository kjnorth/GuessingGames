class InputValidation:
    user_input = ""

    def __init__(self, users_input):
        InputValidation.user_input = users_input

    @staticmethod
    def is_input_str():
        if InputValidation.user_input.isalpha():
            return True
        else:
            print("That\'s not a letter!")
            return False

    @staticmethod
    def is_input_only_one_character():
        if len(InputValidation.user_input) == 1:
            return True
        else:
            print("Please only enter one letter at a time")
            return False


class CheckInputAgainstGuessWord(InputValidation):

    def __init__(self, guess_word):
        self._guess_word = guess_word
        CheckInputAgainstGuessWord.replaced_chars = 0

    underscores_spaces_and_correct_guesses = []

    def populate_underscores_and_spaces(self):
        global underscores_spaces_and_correct_guesses
        underscores_spaces_and_correct_guesses = ["_" if char != " " else " " for char in self._guess_word]

    def populate_correct_guesses(self):
        global underscores_spaces_and_correct_guesses

        u_input = InputValidation.user_input
        correct_guess = [self.good_guess(char, i, underscores_spaces_and_correct_guesses)
                         if char == u_input or char == u_input.upper() or char == u_input.lower()
                                                                          and self.is_already_guessed(char) is False
                         else False
                         for i, char in enumerate(self._guess_word)]

        self.is_correct_guess(correct_guess)

    @staticmethod
    def good_guess(char, i, underscores_spaces_and_correct_guesses):
        underscores_spaces_and_correct_guesses[i] = char
        CheckInputAgainstGuessWord.replaced_chars += 1
        return True

    @staticmethod
    def is_already_guessed(user_char):
        global underscores_spaces_and_correct_guesses
        for letter in underscores_spaces_and_correct_guesses:
            if letter == user_char:
                print("Already guessed...")
                return True
        return False

    def check_if_won(self):
        space_decrement = self.decrement_for_spaces()
        length = len(self._guess_word)

        if CheckInputAgainstGuessWord.replaced_chars == (length - space_decrement):
            print("\nYou got it!")
            return True
        else:
            return False

    def decrement_for_spaces(self):
        space_decrement = 0

        for char in self._guess_word:
            if char == " ":
                space_decrement += 1
        return space_decrement

    @staticmethod
    def is_correct_guess(correct_guess):
        print("Correct guess!") if correct_guess else print("Try again!")

    @staticmethod
    def print_underscores_spaces_and_correct_guesses():

        for i in underscores_spaces_and_correct_guesses:
            print(i, end=" ")
