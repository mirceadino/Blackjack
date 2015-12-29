from player.Player import Player
from game.Exceptions import BlackjackException


class Autoplayer(Player):
    '''
    Class used for handling an automatic player for a game of blackjack.
    '''

    def __init__(self, name, hand, personality):
        '''
        Constructor for an Autoplayer.
        :param name: string - name of the dealer
        :param hand: Hand - hand corresponding to the autoplayer
        :param personality: Personality - AI personality/strategy of the autoplayer
        '''
        Player.__init__(self, name, hand)
        self.personality = personality


    def proceed(self):
        '''
        Performs the next move of the autoplayer.
        :return: string - name of autoplayer's move
        :raises BlackjackException: if the personality does not returns a valid move
        '''
        move = self.personality.think()

        if move == "hit":
            self.draw()
        elif move == "stand":
            self.stand()
        else:
            raise BlackjackException("Invalid move.")

        return move