
class Card:
    '''
    Class used for handling information about a card.
    '''

    def __init__(self, name, value, url, text, color):
        '''
        Constructor for a Card.
        :param name: string - name of the card
        :param value: int - value of the card
        :param url: string - url for image representation of the card
        :param text: string - text for HTML representation of the card
        :param color: string - color of the card
        '''
        self.name = name
        self.value = value
        self.url = url
        self.text = text
        self.color = color


    def __repr__(self):
        return self.name


    def __str__(self):
        return self.name