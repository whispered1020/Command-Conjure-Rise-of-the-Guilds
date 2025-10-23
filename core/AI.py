import random

class SimpleAI:
    """IA simples que escolhe a carta de maior ATK."""
    def choose_card(self, deck):
        if not deck.cards:
            return None
        return max(deck.cards, key=lambda c: c.atk)
