class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def print_cards(self):
        print(self.name + '\'s cards:')
        for c in self.cards:
            print(c)
