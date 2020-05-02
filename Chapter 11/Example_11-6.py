from random import shuffle
from frenchdeck import FrenchDeck

deck = FrenchDeck()


def set_card(deck, position, card):
    deck._cards[position] = card


FrenchDeck.__setitem__ = set_card
shuffle(deck)
deck[:5]
