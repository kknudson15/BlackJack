from Deck import *
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    def isBust(self):
        return self.value >21
    def stand(self):
        stand =  input('Do you want to stay?')
        if stand == 'yes':
            return True
        else:
            return False
    def hand_value(self):
        return self.value()
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
