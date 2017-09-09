""" Pythonic : consistency
    - dunder method (magic method)
"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):

    ranks = [str(n) for n in range(2, 11)]  + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
     
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    # dunder method(magic method)
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


base_card = Card('7', 'spades')
print(base_card)

deck = FrenchDeck()
print(len(deck))
print(deck[6])
print(deck[-1])

print(choice(deck))
print(deck[:3])
print(deck[12::13])

for card in deck[12::13]:
    print(card)

for card in reversed(deck[12::13]):
    print(card)

print(Card('Q', 'hearts') in deck)
print(Card('Q', 'beasts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(str(card.rank))
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

