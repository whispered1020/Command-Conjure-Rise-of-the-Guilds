import random
from core.card import Card

class Deck:
    """Representa um deck de cartas."""
    def __init__(self, cards_data):
        self.cards = [Card(c) for c in cards_data]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

    def __len__(self):
        return len(self.cards)
