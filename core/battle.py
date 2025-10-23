def attack(monster1, monster2):
    """
    Resolve o combate entre dois monstros.
    Retorna um dicionário com o resultado.
    """
    result = {"winner": None, "damage": 0, "details": ""}

    if monster1.atk > monster2.atk:
        result["winner"] = monster1.name
        result["damage"] = monster1.atk - monster2.atk
        result["details"] = f"{monster2.name} is destroyed."
    elif monster1.atk < monster2.atk:
        result["winner"] = monster2.name
        result["damage"] = monster2.atk - monster1.atk
        result["details"] = f"{monster1.name} is destroyed."
    else:
        result["winner"] = "Draw"
        result["details"] = "Both monsters are destroyed."

    return result
