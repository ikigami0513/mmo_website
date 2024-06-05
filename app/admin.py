from django.contrib import admin
from .models import *

admin.site.site_title = "Characters Builder"
admin.site.site_header = "Characters Builder"

class StuffAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "required_level", "picture"]}),
        ("Stats", {"fields": ["hp", "mana", "attack", "defense", "speed", "luck"]})
    )

@admin.register(Helmet)
class HelmetAdmin(StuffAdmin):
    pass

@admin.register(Armor)
class ArmorAdmin(StuffAdmin):
    pass

@admin.register(Pant)
class PantAdmin(StuffAdmin):
    pass

@admin.register(Boots)
class BootsAdmin(StuffAdmin):
    pass

@admin.register(Gantelet)
class GanteletAdmin(StuffAdmin):
    pass

@admin.register(Ring)
class RingAdmin(StuffAdmin):
    pass

@admin.register(Amulet)
class AmuletAdmin(StuffAdmin):
    pass

@admin.register(Belt)
class BeltAdmin(StuffAdmin):
    pass

@admin.register(Sword)
class SwordAdmin(StuffAdmin):
    pass

@admin.register(Bow)
class BowAdmin(StuffAdmin):
    pass

@admin.register(Spear)
class SpearAdmin(StuffAdmin):
    pass

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "icon"]}),
        ("Stats", {"fields": ["hp", "mana", "attack", "defense", "speed", "luck"]})
    )

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "icon", "weapon"]}),
        ("Stats", {"fields": ["hp", "mana", "attack", "defense", "speed", "luck"]})
    )

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["user",]}),
        ("Informations", {"fields": ["name", "classe", "race", "level"]}),
        ("Équipements", {"fields": ["weapon", "helmet", "armor", "pant", "boots", "left_gantelet", "right_gantelet", "ring", "amulet", "belt"]})
    )