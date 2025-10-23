import json

def load_cards(path="data/cards.json"):
    """Carrega o arquivo JSON de cartas e retorna uma lista de dicionários."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
