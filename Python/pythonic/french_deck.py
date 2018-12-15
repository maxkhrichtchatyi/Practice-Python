#!/bin/python3
# -*- coding: utf-8 -*-

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks ]

    def __getitem__(self, item):
        return self._cards[item]

    def __len__(self):
        return len(self._cards)
