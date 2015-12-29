
class Hand():
    '''
    Class used for handling a hand of blackjack.
    '''

    def __init__(self, deck):
        '''
        Constructor for a Hand.
        :param deck: Deck - deck of cards to be used
        '''
        self.hand = [] # hand = cards composing the hand
        self.deck = deck


    def __iter__(self):
        return iter(self.hand)


    def __str__(self):
        return str(self.hand)


    def reset(self):
        '''
        Reinitializes the hand.
        '''
        self.hand[:] = []


    def draw(self):
        '''
        Draws the card from the top of the deck.
        :raises BlackjackException: if all cards have been popped and no cards are left in the stack
        '''
        card = self.deck.draw()
        self.hand.append(card)


    def sum(self):
        '''
        Sums up the values of the cards in a favorable way to the player.
        If the hand has aces, they are evaluated in such manner that the sum is closest to 21, without exceeding it.
        :return: int - sum of the cards
        '''
        not_aces = 0
        aces = 0
        best_sum = 0

        for card in self.hand:
            if card.value == 11: aces += 1
            else: not_aces += card.value

        best_sum = not_aces + aces

        for ones in range(aces):
            sum = not_aces + ones * 1 + (aces - ones) * 11
            if sum <= 21 and best_sum < sum:
                best_sum = sum

        return best_sum


    def blackjack(self):
        '''
        Checks if the hand is a blackjack.
        :return: True - hand is a blackjack, False otherwise
        '''
        return (self.sum() == 21)


    def loss(self):
        '''
        Checks if the hand is a loss.
        :return: True - hand is a loss, False otherwise
        '''
        return (self.sum() > 21)


    def end(self):
        '''
        Checks if the hand is out of the game i.e. it's a loss.
        :return: True - hand is out of the game, False otherwise
        '''
        return self.loss()


    def in_game(self):
        '''
        Checks if the hand is playable and still in the game i.e. it is not a loss yet.
        :return: True - hand is playable, False otherwise
        '''
        return not self.end()