#Author: Aidan Mellin

import Cards
import random as r

"""
This is gonna be the driver code

Cards against humanity rules:
    -One randomly chosen player begins as the Card Czar and plays a Black Card. The Card Czar reads the question or fill-in-the-blank phrase on the Black Card out loud.
    -Everyone else answers the question or fills in the blank by passing one White Card, face down, to the Card Czar.
    -The Card Czar shuffles all of the answers and shares each card combination with the group. For full effect, the Card Czar should usually re-read the Black Card before presenting each answer.
    -The Card Czar then picks a favorite, and whoever played that answer keeps the Black Card as one Awesome Point.
    -After the round, a new player becomes the Card Czar and everyone draws back up to ten White Cards.

"""

class CAH:
    def __init__(self):
        self.users = []
        self.played_cards = []
        self.blackCard = self.drawBCard()
        self.requiredCards = 1

    def _addUser(self, user):
        self.users.append(Player(user, self.getHand()))

    def drawBCard(self):
        '''
        Draw random black card (if not already used)
        '''
        choice = r.choice(cards.bCards)
        while True:
            if choice not in cards.usedBCards:
                cards.usedBCards.append(choice)
                if choice.count("_") > 1:
                    self.requiredCards = choice.count("_")
                return choice #Return random black card not already created

    def drawWCard(self):
        '''
        Draw a random white card from imported parseCards and add chosen card to the used cards.
        '''
        while True:
            if self.blankCard():
                return "___" #Return a blank card
            choice = r.choice(cards.wCards)
            if choice not in cards.usedWCards:
                cards.usedWCards.append(choice)
                return choice #Return random white card not already created

    '''
    getHand function for each player. This should all be handled server-side, and this should be implemented in my discord bot
    '''
    def getHand(self):
        hand = []
        for i in range(10):
            hand.append(self.drawWCard())
        return hand

    def blankCard(self):
        return r.random() <= .1 #10% chance of getting a blank card

    def playCard(self, user, card):
        self.played_cards.append()

    def endRound():
        pass

    def test(self):
        self._addUser("Test User")
        self.users[0].wonRound()
        self.users[0].czarToggle()

    def printInfo(self):
        print("Black Card: {} (Required Card Count: {})".format(self.blackCard, self.requiredCards))
        for i in self.users:
            print("{}:\n\tCzar? {}\n\tScore: {}\n\tHand: {}".format(i.name, i.isCzar, i.score, i.hand))

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.isCzar = False
        self.score = 0
        self.cardsToAdd = 0
    
    def czarToggle(self):
        self.isCzar = not self.isCzar
    
    def wonRound(self):
        self.score += 1

if __name__ == '__main__':
    cards = Cards.Cards()
    cah = CAH()
    cah.test()
    cah.printInfo()
    print("CAH completed")