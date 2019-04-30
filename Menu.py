
class Menu:
    _menu_options = []

    def __init__(self):
        pass

    def create_menu_option(self, option_text, option_func):
        self._menu_options.append({'text': option_text, 'func': option_func})

    def display(self):
        print()
        print('Select an option')

        for idx, option in enumerate(self._menu_options):
            print(' ' + chr(ord('A') + idx) + ') ' + option['text'])

    def handle_input(self):
        choice = input('> ')
        choice = choice.capitalize()
        while len(choice) != 1 or ord(choice) not in range(ord('A'), ord('A') + len(self._menu_options)):
            print('Invalid selection')
            choice = input('> ')

        self._menu_options[ord(choice) - ord('A')]["func"]()
