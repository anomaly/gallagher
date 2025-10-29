""" Cardholder Update Builder exploration

"""
from ..ref.card import CardTypeRef

from pydantic import BaseModel, URL

class CardholderUpdateBuilder:

    def __init__(self):
        self.cards = []

    def add_card(self, card: CardTypeRef):
        self.cards.append(card)

    def remove_card(self, href: URL):
        pass
