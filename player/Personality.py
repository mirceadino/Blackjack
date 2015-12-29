
class Personality():
    '''
    Interface used for handling a personality for AI of a player in a blackjack game.
    '''

    def __init__(self, own_hand, competitor_hand):
        '''
        Constructor for a Personality.
        :param own_hand: Hand - hand of the player with the assigned personality
        :param competitor_hand: - hand of the competitor
        '''
        self.own_hand = own_hand
        self.competitor_hand = competitor_hand


    def think(self):
        '''
        Thinks of the next move.
        :return: "hit" - if the player wants to draw a card, "stand" - if he wants to stand
        '''
        pass