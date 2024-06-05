from .models import *

COMBINAISONS = {
    "epees": Sword,
    "arcs": Bow,
    "lances": Spear,
    "casques": Helmet,
    "armures": Armor,
    "pantalons": Pant,
    "bottes": Boots,
    "gants": Gantelet,
    "ceintures": Belt,
    "anneaux": Ring,
    "amulettes": Amulet,
    "sword": Sword,
    "bow": Bow,
    "spear": Spear,
    "helmet": Helmet,
    "armor": Armor,
    "pant": Pant,
    "boots": Boots,
    "gantelet": Gantelet,
    "belt": Belt,
    "ring": Ring,
    "amulet": Amulet
}

def str_to_class(name):
    return COMBINAISONS.get(name, None)