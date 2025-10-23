class Card:
    """Classe base para qualquer carta."""
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.type = data.get("type")
        self.subtype = data.get("subtype", [])
        self.level = data.get("level", 0)
        self.attribute = data.get("attribute", "")
        self.race = data.get("race", "")
        self.atk = data.get("atk", 0)
        self.def_ = data.get("def", 0)
        self.effect = data.get("effect", "")
        self.archetype = data.get("archetype", "")

    def __str__(self):
        return f"{self.name} (ATK {self.atk} / DEF {self.def_})"
