from django.db import models
from django.contrib.auth.models import User

class Stats(models.Model):
    hp = models.IntegerField(verbose_name="points de vie")
    mana = models.IntegerField(verbose_name="mana")
    attack = models.IntegerField(verbose_name="attaque")
    defense = models.IntegerField(verbose_name="défense")
    speed = models.IntegerField(verbose_name="vitesse")
    luck = models.IntegerField(verbose_name="chance")

class Stuff(Stats):
    name = models.CharField(max_length=50, verbose_name="nom")
    required_level = models.PositiveIntegerField(verbose_name="niveau requis")
    picture = models.ImageField(upload_to="items/", null=True)
    
    def __str__(self):
        return self.name
    
class Helmet(Stuff):
    class Meta:
        verbose_name = "Casque"
        verbose_name_plural = "Casques"

class Armor(Stuff):
    class Meta:
        verbose_name = "Armure"
        verbose_name_plural = "Armures"

class Pant(Stuff):
    class Meta:
        verbose_name = "Pantalon"
        verbose_name_plural = "Pantalons"

class Boots(Stuff):
    class Meta:
        verbose_name = "Botte"
        verbose_name_plural = "Bottes"

class Gantelet(Stuff):
    class Meta:
        verbose_name = "Gantelet"
        verbose_name_plural = "Gantelets"
        
class Ring(Stuff):
    class Meta:
        verbose_name = "Anneau"
        verbose_name_plural = "Anneaux"
        
class Amulet(Stuff):
    class Meta:
        verbose_name = "Amulette"
        verbose_name_plural = "Amulettes"
        
class Belt(Stuff):
    class Meta:
        verbose_name = "Ceinture"
        verbose_name_plural = "Ceintures"

class Weapon(Stuff):
    pass

class Sword(Weapon):
    class Meta:
        verbose_name = "Épée"
        verbose_name_plural = "Épées"

class Bow(Weapon):
    class Meta:
        verbose_name = "Arc"
        verbose_name_plural = "Arcs"

class Spear(Weapon):
    class Meta:
        verbose_name = "Lance"
        verbose_name_plural = "Lances"

class Race(Stats):
    name = models.CharField(max_length=50, verbose_name="nom")
    icon = models.ImageField(upload_to="icons/races", null=True)
    
    class Meta:
        verbose_name = "Race"
        verbose_name_plural = "Races"
        
    def __str__(self):
        return self.name
    
class Classe(Stats):
    WEAPONS = (
        ('epees', 'Épées'),
        ('arcs', 'Arcs'),
        ('lances', 'Lances'),
    )
    
    name = models.CharField(max_length=50, verbose_name="classe")
    icon = models.ImageField(upload_to="icons/classe", null=True)
    weapon = models.CharField(max_length=30, null=True, choices=WEAPONS)
    
    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"
        
    def __str__(self):
        return self.name

class Character(models.Model):
    user = models.ForeignKey(User, related_name="characters", on_delete=models.CASCADE, verbose_name="utilisateur")
    
    name = models.CharField(max_length=50, verbose_name="nom", null=False)
    classe = models.ForeignKey(Classe, null=False, on_delete=models.CASCADE, verbose_name="classe")
    race = models.ForeignKey(Race, null=False, on_delete=models.CASCADE, verbose_name="race")
    level = models.PositiveIntegerField(verbose_name="niveau", default=0)
    
    weapon = models.ForeignKey(Weapon, null=True, default=None, on_delete=models.SET_NULL, verbose_name="arme")
    helmet = models.ForeignKey(Helmet, null=True, default=None, on_delete=models.SET_NULL, verbose_name="casque")
    armor = models.ForeignKey(Armor, null=True, default=None, on_delete=models.SET_NULL, verbose_name="armure")
    pant = models.ForeignKey(Pant, null=True, default=None, on_delete=models.SET_NULL, verbose_name="pantalon")
    boots = models.ForeignKey(Boots, null=True, default=None, on_delete=models.SET_NULL, verbose_name="bottes")
    left_gantelet = models.ForeignKey(Gantelet, null=True, default=None, on_delete=models.SET_NULL, related_name="left_gantelet", verbose_name="gant gauche")
    right_gantelet = models.ForeignKey(Gantelet, null=True, default=None, on_delete=models.SET_NULL, related_name="right_gantelet", verbose_name="gant droit")
    ring = models.ForeignKey(Ring, null=True, default=None, on_delete=models.SET_NULL, verbose_name="Anneau")
    amulet = models.ForeignKey(Amulet, null=True, default=None, on_delete=models.SET_NULL, verbose_name="Amulette")
    belt = models.ForeignKey(Belt, null=True, default=None, on_delete=models.SET_NULL, verbose_name="Ceinture")
    
    class Meta:
        verbose_name = "Personnage"
        verbose_name_plural = "Personnages"
        
    def __str__(self):
        return f"{self.name}@{self.user.username}"