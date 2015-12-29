from game.Exceptions import BlackjackException


class Player():
    '''
    Class used for handling a player of blackjack.
    '''

    def __init__(self, name, hand):
        '''
        Constructor for a Player.
        :param name: string - name of the player
        :param hand: Hand - hand corresponding to the player
        '''
        self.name = name
        self.hand = hand
        self.standing = False


    def draw(self):
        '''
        Draws a card from the top of the deck and adds it to player's hand.
        :raises BlackjackException: if player is standing, won or lost the hand
        '''
        if self.is_standing():
            raise BlackjackException("{0} is standing.".format(self.name))

        if self.is_loser():
            raise BlackjackException("{0} lost.".format(self.name))

        self.hand.draw()


    def stand(self):
        '''
        Stands the hand and cedes the turn to another player.
        :raises BlackjackException: if player is standing, won or lost the hand
        '''
        if self.is_standing():
            raise BlackjackException("{0} is already standing.".format(self.name))

        if self.is_loser():
            raise BlackjackException("{0} lost.".format(self.name))

        self.standing = True


    def is_standing(self):
        '''
        Checks if the player is standing his turn.
        :return: True - player is standing, False - otherwise
        '''
        return self.standing


    def is_loser(self):
        '''
        Checks if the player has a losing hand.
        :return: True - player lost, False - otherwise
        '''
        return self.hand.loss()


    def is_in_game(self):
        '''
        Checks if the player is still allowed to draw cards.
        :return: True - player is still in game, False - otherwise
        '''
        return not (self.is_standing() or self.hand.in_game())