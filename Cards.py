#Author: Aidan Mellin
# Name: parseCards.py

import random as r

"""
This is gonna be the code part that parses the input of the cards text.
"""

'''
First thing is importing the cards. Next is to just cycle through it and enter white cards into one dict and black cards into another.

Going to use list and keep track of already used indeces.
'''

class Cards:
    def __init__(self):
        self.bCards = []
        self.wCards = []

        #Separate lists so that these can be cleared for easy game restart
        self.usedBCards = []
        self.usedWCards = []

        #Actually parse the text file
        self.parseCards()

    def parseCards(self, fn="cards-plain.txt", delimeter="---"):
        """Parse cards from text file

        Args:
            fn (str, optional): [name of text file starting with white cards, when switching to black cards has a line of '---']. Defaults to "cards-plain.txt".
        """
        black_cards = False
        with open(fn,"r") as f:
            #Read for the delimeter so that custom cards can be added
            for line in f:
                line = line.strip()
                if delimeter in line:
                    black_cards = True
                if black_cards:
                    if delimeter not in line:
                        self._addBCard(line)
                else:
                    self._addWCard(line)
    
    #Separate methods in case I want to change this up later.

    def _addBCard(self, card):
        """Add b card to list

        Args:
            card ([str]): [black card to be added]
        """
        self.bCards.append(card)

    def _addWCard(self, card):
        """Add white card to list

        Args:
            card ([str]): [White card to be added]
        """
        self.wCards.append(card)

    def _useBCard(self, card):
        """Use a black card

        Args:
            card ([str]): [black card to be added to used list]
        """
        self.usedBCards.append(card)

    def _useWCard(self, card):
        """Use a white card

        Args:
            card ([str]): [white card to be used]
        """
        self.usedWCards.append(card)

    #Might implement vote remove card function later


if __name__ == '__main__':
    cards = Cards()
    print("Random White Card:\n{}\nRandom Black Card:\n{}".format(r.choice(cards.wCards), r.choice(cards.bCards)))