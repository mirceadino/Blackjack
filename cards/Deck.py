from random import shuffle
from cards.Card import Card
from game.Exceptions import BlackjackException


class Deck():
    '''
    Class used for handling a deck of cards.
    '''

    def __init__(self):
        '''
        Constructor for a Deck.
        '''
        self.pack = [] # pack = all cards of the deck
        self.stack = [] # stack = remaining cards of the deck, face down
        self.popped = [] # popped = cards that were drawn
        self.__generate()


    def __generate(self):
        for i, suit in  [(0, "clubs"), (1, "diams"), (2, "hearts"), (3, "spades")]:
            if i in [0, 3]: color="black"
            else: color="red"

            for number in range(2, 11):
                name = str(number) + " " + suit
                value = number
                url = "{0}{1}.png".format(i, number)
                text = "{0}<font color={1}>&{2};</font>".format(number, color, suit)
                card = Card(name, value, url, text, color)

                self.pack.append(card)

            for number in ['J', 'Q', 'K']:
                name = str(number) + " " + suit
                value = 10
                url = "{0}{1}.png".format(i, number)
                text = "{0}<font color={1}>&{2};</font>".format(number, color, suit)
                card = Card(name, value, url, text, color)

                self.pack.append(card)

            for number in ['A']:
                name = str(number) + " " + suit
                value = 11
                url = "{0}{1}.png".format(i, number)
                text = "{0}<font color={1}>&{2};</font>".format(number, color, suit)
                card = Card(name, value, url, text, color)

                self.pack.append(card)


    def shuffle(self):
        '''
        Puts all the pack in the game and shuffles it.
        '''
        self.stack[:] = self.pack
        self.popped[:] = []
        self.reshuffle()


    def reshuffle(self):
        '''
        Shuffles the stack.
        '''
        shuffle(self.stack)


    def draw(self):
        '''
        Draws a card from the stack.
        :return: Card - the card from the top of the stack is popped
        :raises BlackjackException: if all cards have been popped and no cards are left in the stack
        '''
        if len(self.stack) == 0:
            raise BlackjackException("No cards left.")

        return self.stack.pop()