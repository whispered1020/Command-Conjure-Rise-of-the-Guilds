from utils.loader import load_cards
from core.deck import Deck
from core.game import Game

def main():
    cards = load_cards()
    deck1 = Deck(cards[:10])
    deck2 = Deck(cards[:10])

    game = Game(deck1, deck2)
    game.start()

if __name__ == "__main__":
    main()
