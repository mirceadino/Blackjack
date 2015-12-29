from player.Personality import Personality


class Dealer(Personality):
    '''
    Class corresponding to dealer's personality for a game of blackjack.
    As long as the competitor's player has a greater, potentially winning hand than the dealer, draw cards.
    '''

    def __init__(self, own_hand, competitor_hand):
        Personality.__init__(self, own_hand, competitor_hand)


    def think(self):
        if self.own_hand.sum() >= self.competitor_hand.sum():
            return "stand"

        return "hit"