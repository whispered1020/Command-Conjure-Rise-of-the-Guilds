from core.battle import attack

class Game:
    """Controla o fluxo básico de uma batalha simples."""
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.lp1 = 4000
        self.lp2 = 4000

    def start(self):
        print("=== CardSim Battle Start ===")
        c1 = self.deck1.draw()
        c2 = self.deck2.draw()

        print(f"Player 1 summons {c1}")
        print(f"Player 2 summons {c2}")

        result = attack(c1, c2)
        print(f"Result: {result['details']}")

        if result["winner"] == c1.name:
            self.lp2 -= result["damage"]
        elif result["winner"] == c2.name:
            self.lp1 -= result["damage"]

        print(f"LP1: {self.lp1} | LP2: {self.lp2}")
