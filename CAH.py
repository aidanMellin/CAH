#Author: Aidan Mellin

import importCards
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
        self.users = [] #List of users
        self.czar = '' #Current czar for round (votes on which card wins)
        self.voteAvailable = False #I don't think this is necessary
        self.blackCard = self.drawBCard()
        self.requiredCards = 1

        self.played_cards = {}

    def _addUser(self, user): #Add a user to the game
        user = Player(user, self.getHand())
        self.users.append(user)

    def getUserIndex(self, user):
        '''
        Return int of the user index of the user designated
        '''
        return self.users.index(user)

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
        user = self.users[userIdx]
        if not user == self.czar:
            card = user.hand[idx]
            if card == "___": #White card instance
                card = self.useBlankCard()
                user.hand[userIdx] = card #Replace blank card with inputted text
            self.played_cards.update({card : user})
            user.hand.remove(card)
            if len(self.played_cards) == len(self.users) - 1:
                self.voteAvailable = True
                return self.showplayed_cards()

            return False

    def showplayed_cards(self):
        lineBreak = "------------------------"
        strReturn = "\n\t===Which Card Wins?===\nPrompt:\t{}\n{}\n".format(self.blackCard, lineBreak)

        for count, value in enumerate(self.played_cards):
            strReturn += '{}.\t{}\n{}\n'.format(count + 1, value, lineBreak) 

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

        self.czar = r.choice(self.users)
        self.users[self.users.index(self.czar)].czarToggle()
        self.users[self.users.index(self.czar)].played = True

        return "New Czar is {}".format(self.czar.name)

    def winner(self, user):
        if not user.isCzar:
            user.wonRound()
            self.endRound()
            strReturn = "{} wins!\n".format(user.name)
            strReturn += self.getScoreboard()
            strReturn += self.endRound()
            return strReturn
        else:
            return self.winner(self.played_cards.get(value) for count, value in enumerate(self.played_cards)[int(input("Invalid selection. Enter winning card number: ")) - 1])

    def endRound(self):
        for i in self.users:
            for j in range(i.cardsToAdd):
                i.hand.append(self.drawWCard())
            i.played = False
        self.blackCard = self.drawBCard()
        self.voteAvailable = False
        self.played_cards.clear()
        return self.getNewCzar()


    def printInfo(self):
        strRtn = "Black Card: {} (Required Card Count: {})\nCzar: {}".format(self.blackCard, self.requiredCards, self.czar.name)
        for i in self.users:
            strRtn += "{}:\n\tCzar? {}\n\tScore: {}\n\tHand: {}".format(i.name, i.isCzar, i.score, i.hand)
        strRtn += "\n"
        return strRtn

    def test(self):
        self._addUser("Test User 1")
        self._addUser("Test User 2")
        self._addUser("Test User 3")

        while True:
            play_cards = []

            print("This round's prompt: {}".format(self.blackCard))
            print("There are {} blank spots".format(self.blackCard.count("_")))

            self.users[0].wonRound()
            self.users[0].wonRound()
            self.users[1].wonRound()
            
            self.getNewCzar()
            # print(self.printInfo())
            print(self.showHand(2))

            play_cards.append([0,1])
            play_cards.append([1,1])
            play_cards.append([2, int(input("Enter card number to play: "))-1])

            for i in play_cards:
                card = self.playCard(i[0], i[1])
                print("{}".format(card) if not card == None and not card  == False else '')

            vote = int(input("Enter winning card number: ")) - 1
            while True:
                try:
                    print("\n{}".format(self.winner([self.played_cards.get(value) for count, value in enumerate(self.played_cards)][vote])))
                    break
                except Exception as e:
                    vote = int(input("Invalid selection. Enter winning card number: ")) - 1
            print("\n")

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
    cards = importCards.Cards()
    cah = CAH()
    cah.test()