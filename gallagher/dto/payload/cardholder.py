""" Cardholder Update Builder exploration

Example Usage:

    add_card_href = CardTypeRef(href="https://api.example.com/cards/123")
    remove_card_href = HrefMixin(href="https://api.example.com/cards/456")

    card_update_builder = CardholderUpdateBuilder()
        .add_card(add_card_href)
        .remove_card(remove_card_href)
        .build()

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

