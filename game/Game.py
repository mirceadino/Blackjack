from cards.Deck import Deck
from cards.Hand import Hand
from player.Player import Player
from player.Autoplayer import Autoplayer
from player.Dealer import Dealer
from game.Exceptions import BlackjackException


class Game():
    '''
    Class used for handling a game of blackjack between two players, one of which is a dealer.
    '''

    def __init__(self):
        '''
        Constructor for a Game.
        '''
        self.deck = Deck()
        self.deck.shuffle()

        player_hand = Hand(self.deck)
        dealer_hand = Hand(self.deck)
        dealer = Dealer(dealer_hand, player_hand)

        self.player = Player("Player", player_hand)
        self.dealer = Autoplayer("Dealer", dealer_hand, dealer)

        self.player.draw()
        self.dealer.draw()
        self.player.draw()

        self.dealer_turn = False

        self.player_wins = 0
        self.dealer_wins = 0
        self.added_to_scoreboard = False


    def reset(self):
        '''
        Reinitializes the game.
        '''
        if not self.is_end() and not self.added_to_scoreboard:
            self.dealer_wins += 1

        self.deck.shuffle()

        player_hand = Hand(self.deck)
        dealer_hand = Hand(self.deck)
        dealer = Dealer(dealer_hand, player_hand)

        self.player = Player("Player", player_hand)
        self.dealer = Autoplayer("Dealer", dealer_hand, dealer)

        self.player.draw()
        self.dealer.draw()
        self.player.draw()

        self.dealer_turn = False
        self.added_to_scoreboard = False


    def hit(self):
        '''
        Draws a card for the first player.
        :raises BlackjackException: if game came to a conclusion or if it's not player's turn
        '''
        if self.is_end():
            raise BlackjackException("Game ended.")

        if self.dealer_turn:
            raise BlackjackException("Not player\'s turn.")

        self.player.draw()


    def stand(self):
        '''
        Stands first player's turn and passes the turn to the dealer.
        :raises BlackjackException: if game came to a conclusion or if it's not player's turn, if player's already standing
        '''
        if self.is_end():
            raise BlackjackException("Game ended.")

        if self.dealer_turn:
            raise BlackjackException("You\'re already standing.")

        self.player.stand()
        self.dealer_turn = True


    def deal(self):
        '''
        Lets the dealer to take a decision to play.
        :raises BlackjackException: if game came to a conclusion or if it's not dealer's turn
        '''
        if self.is_end():
            raise BlackjackException("Game ended.")

        if not self.dealer_turn:
            raise BlackjackException("Not dealer\'s turn.")

        move = self.dealer.proceed()
        return move


    def is_end(self):
        '''
        Checks if the game came to a conclusion.
        :return: True - game reached a conclusion, False - otherwise
        '''
        if self.player.is_loser():
            if not self.added_to_scoreboard:
                self.dealer_wins += 1
            self.added_to_scoreboard = True
            return True

        if self.player.is_standing() and self.dealer.is_loser():
            if not self.added_to_scoreboard:
                self.player_wins += 1
            self.added_to_scoreboard = True
            return True

        if self.player.is_standing() and self.dealer.is_standing():
            if not self.added_to_scoreboard:
                if self.player.hand.sum() > self.dealer.hand.sum():
                    self.player_wins += 1
                else:
                    self.dealer_wins += 1
            self.added_to_scoreboard = True
            return True

        return False