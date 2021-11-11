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
        self.czar = ''
        self.voteAvailable = False
        self.played_cards = []
        self.blackCard = self.drawBCard()
        self.requiredCards = 1

    def _addUser(self, user):
        self.users.append(Player(user, self.getHand()))
        self.played_cards.append(None)

    def drawBCard(self):
        '''
        Draw random black card (if not already used)
        '''
        choice = r.choice(cards.bCards)
        while True:
            if choice not in cards.usedBCards:
                cards.usedBCards.append(choice)
                if choice.count("_") >= 1:
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

    def getHand(self):
        """Get hand for one user

        Returns:
            [string []]: [List of white cards in player's hand]
        """        
        hand = []
        for i in range(10):
            hand.append(self.drawWCard())
        return hand

    def blankCard(self):
        """[determines if card drawn is a blank card]

        Returns:
            [bool]: [if random num between 0 < x < 1 was <= .1]
        """        
        return r.random() <= .1 #10% chance of getting a blank card

    def showHand(self, userIdx):
        """Return a stringified version of the indicated player's hand

        Args:
            userIdx ([int]): [index of player in self.users]
        """    
        lineBreak = "------------------------"
        returnStr = "Your hand:\n"
        for i in range(len(self.users[userIdx].hand)):
            returnStr += "{}.\t{}\n{}\n".format(i+1, self.users[userIdx].hand[i], lineBreak)
        return returnStr

    def useBlankCard(self):
        return input("Enter Text for Blank Card: ")

    def playCard(self, userIdx, idx):
        """Play a card if user playing card isn't czar and hasn't already played

        Args:
            userIdx ([int]): [index position of the user]
            idx ([int]): [index of the card the user is playing]
        """
        # idx -= 1   
        user = self.users[userIdx]
        if not user == self.czar and not user.played:
            card = user.hand[idx]
            if card == "___":
                card = self.useBlankCard()
                user.hand[userIdx] = card
            self.played_cards[userIdx] = card
            user.played = True
            user.cardsToAdd += 1
            user.hand.remove(card)

            if self.played_cards.count(None) <= 1:
                self.voteAvailable = True
                return self.showPlayedCards()

    def showPlayedCards(self):
        lineBreak = "------------------------"
        strReturn = "Prompt:\t{}\n{}\n".format(self.blackCard, lineBreak)
        i = 0
        while i < len(self.played_cards)-1:
            if self.played_cards[i] is not None and self.played_cards[i] != "":
                strReturn += '{}.\t{}\n{}\n'.format(i+1, self.played_cards[i], lineBreak) 
                i += 1

        return strReturn

    def getScoreboard(self):
        scores = [[i.name, i.score] for i in self.users]

        scoresSorted = quickSort(scores, 0, len(scores)-1)
        strReturn = "Scores:\n"
        for i in scoresSorted:
            strReturn += "{}\t{}\n".format(i[0], i[1])
        
        return strReturn

    def getNewCzar(self):
        if not self.czar == "":
            self.users[self.users.index(self.czar)].czarToggle()
            self.users[self.users.index(self.czar)].played = False

        self.czar = r.choice(self.users)
        self.users[self.users.index(self.czar)].czarToggle()
        self.users[self.users.index(self.czar)].played = True
        self.played_cards[self.users.index(self.czar)] = "I am Czar. I shan't play"

        return "New Czar is {}".format(self.czar)

    def winner(self, userIdx):
        userIdx -= 1
        self.users[userIdx].wonRound()
        self.endRound()
        strReturn = "{} wins!\n".format(self.users[userIdx].name)
        strReturn += self.getScoreboard()
        self.endRound()
        return strReturn

    def endRound(self):
        for i in self.users:
            for j in range(i.cardsToAdd):
                i.hand.append(self.drawWCard())
            i.played = False
        self.voteAvailable = False
        for i in range(len(self.played_cards)):
            self.played_cards[i] = None
        self.getNewCzar()
        

    def printInfo(self):
        print("Black Card: {} (Required Card Count: {})\nCzar: {}".format(self.blackCard, self.requiredCards, self.czar.name))
        for i in self.users:
            print("{}:\n\tCzar? {}\n\tScore: {}\n\tHand: {}".format(i.name, i.isCzar, i.score, i.hand))
        print("\n")

    def test(self):
        self._addUser("Test User 1")
        self._addUser("Test User 2")
        self._addUser("Test User 3")

        self.users[0].wonRound()
        self.users[0].wonRound()
        self.users[1].wonRound()
        
        self.getNewCzar()
        # self.printInfo()
        self.playCard(0, 1)
        self.playCard(1, 1)
        print(self.playCard(2, 1))

        print(self.winner(1))
        self.endRound()

        print(self.showHand(0))


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.isCzar = False
        self.score = 0
        self.cardsToAdd = 0
        self.played = False
    
    def czarToggle(self):
        self.isCzar = not self.isCzar
    
    def wonRound(self):
        self.score += 1

#--------Quick sort scores----------------
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high][1] #array is [[name, score],[name, score]]

    for j in range(low, high):
        if arr[j][1] >= pivot: # >= inverses the list so it counts down (helpful for scoreboard quicksort)
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

    return arr

if __name__ == '__main__':
    cards = Cards.Cards()
    cah = CAH()
    cah.test()