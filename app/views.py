from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from .forms import *
from .utils import str_to_class
from .models import *
import json

class Index(View):
    def get(self, request):
        characters = Character.objects.all().order_by('-id')
        if len(characters) > 4:
            characters = characters[:4]
        return render(request, "index.html",{
            "characters": characters,
            "nb_characters": len(characters),
        })

class UserRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app_index')
        
        form = RegisterForm()
        return render(request, 'user/register.html', {
            'form': form,
        })
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("app_index")
        
        return render(request, "user/register.html", {
            'form': form
        })

class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('app_index')
    
class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app_index')
        
        form = UserLoginForm()
        return render(request, 'user/login.html', {
            "form": form
        })
        
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request, "user/login.html", {
                    "form": form,
                    "errors": form.errors
                })
            
            login(request, user)
            return redirect('app_index')
        
        return render(request, "user/login.html", {
            "form": form,
        })
        
class Encyclopedie(View):
    def get(self, request, type):
        class_type = str_to_class(type)
        if class_type is None:
            return render(request, "encyclopedie/error.html", {
                "type": type,
            })
            
        data = class_type.objects.all()
        return render(request, "encyclopedie/liste.html", {
            "type": type,
            "data": data
        })
        
class FilterEncyclopedie(View):
    def post(self, request):
        data = request.body.decode()
        data_json = json.loads(data)
        
        query_class = str_to_class(data_json.get("type"))
        query_set = query_class.objects.all()
        
        search_fields = data_json.get('data')
        
        if search_fields.get("name") != "":
            query_set = query_set.filter(name__iexact=search_fields.get("name"))
            
        if search_fields.get("min_required_level") != "" and search_fields.get('max_required_level'):
            min_required_level = int(search_fields.get("min_required_level"))
            max_required_level = int(search_fields.get("max_required_level"))
            query_set = query_set.filter(required_level__range=(min_required_level, max_required_level))
        
        if search_fields.get("min_hp") != "" and search_fields.get("max_hp"):
            min_hp = int(search_fields.get("min_hp"))
            max_hp = int(search_fields.get("max_hp"))
            query_set = query_set.filter(hp__range=(min_hp, max_hp))
            
        if search_fields.get("min_mana") != "" and search_fields.get("max_mana"):
            min_mana = int(search_fields.get("min_mana"))
            max_mana = int(search_fields.get("max_mana"))
            query_set = query_set.filter(mana__range=(min_mana, max_mana))
            
        if search_fields.get("min_attack") != "" and search_fields.get("max_attack"):
            min_attack = int(search_fields.get("min_attack"))
            max_attack = int(search_fields.get("max_attack"))
            query_set = query_set.filter(attack__range=(min_attack, max_attack))
            
        if search_fields.get("min_defense") != "" and search_fields.get("max_defense"):
            min_defense = int(search_fields.get("min_defense"))
            max_defense = int(search_fields.get("max_defense"))
            query_set = query_set.filter(defense__range=(min_defense, max_defense))
            
        if search_fields.get("min_speed") != "" and search_fields.get("max_speed"):
            min_speed = int(search_fields.get("min_speed"))
            max_speed = int(search_fields.get("max_speed"))
            query_set = query_set.filter(speed__range=(min_speed, max_speed))
            
        if search_fields.get("min_luck") != "" and search_fields.get("max_luck"):
            min_luck = int(search_fields.get("min_luck"))
            max_luck = int(search_fields.get("max_luck"))
            query_set = query_set.filter(luck__range=(min_luck, max_luck))
            
        items = []
        for each in query_set:
            items.append({
                "name": each.name,
                "required_level": each.required_level,
                "hp": each.hp,
                "mana": each.mana,
                "attack": each.attack,
                "defense": each.defense,
                "speed": each.speed,
                "luck": each.luck,
                "picture": each.picture.url,
            })
        
        return JsonResponse({
            "message": "ok",
            "items": items
        })
        
class CreatePlayer(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('app_index')
        
        return render(request, "player/create.html", {
            "races": Race.objects.all(),
            "classes": Classe.objects.all(),
            "equipements": ["helmet", "armor", "pant", "boots", "gantelet", "belt", "ring", "amulet"],
            "display_equipement": {
                "helmet": "un casque",
                "armor": "une armure",
                "pant": "un pantalon",
                "boots": "des bottes",
                "gantelet": "un gant",
                "belt": "une ceinture",
                "ring": "un anneau",
                "amulet": "une amulette",
                "weapon": "une arme",
            }
        })
        
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({
                "error": ""
            })
        data = request.body.decode()
        data_json = json.loads(data)
        
        if data_json.get("name") is None:
            return JsonResponse({
                "success": False,
                "reason": "name"
            })
            
        if data_json.get("race") is None:
            return JsonResponse({
                "success": False,
                "reason": "race"
            })
            
        if data_json.get("classe") is None:
            return JsonResponse({
                "success": False,
                "reason": "classe"
            })
            
        try:
            character = Character.objects.get(user=request.user, name=data_json.get("name"))
            return JsonResponse({
                "success": False,
                "reason": "name taken"
            })
        except Character.DoesNotExist:
            pass
        
        name = data_json.get("name")
        if data_json.get("level") is None:
            level = 0
        else:
            level = data_json.get("level")
            
        try:
            classe = Classe.objects.get(name=data_json.get("classe"))
        except Classe.DoesNotExist:
            return JsonResponse({
                "success": False,
                "reason": "classe not exists"
            })
            
        try:
            race = Race.objects.get(name=data_json.get("race"))
        except Race.DoesNotExist:
            return JsonResponse({
                "success": False,
                "reason": "race not exists"
            })
            
        try:
            weapon = Weapon.objects.get(id=data_json.get("weapon"))
        except Weapon.DoesNotExist:
            weapon = None
            
        try:
            helmet = Helmet.objects.get(id=data_json.get("helmet"))
        except Helmet.DoesNotExist:
            helmet = None
            
        try:
            armor = Armor.objects.get(id=data_json.get("armor"))
        except Armor.DoesNotExist:
            armor = None
            
        try:
            pant = Pant.objects.get(id=data_json.get("pant"))
        except Pant.DoesNotExist:
            pant = None
            
        try:
            boots = Boots.objects.get(id=data_json.get("boots"))
        except Boots.DoesNotExist:
            boots = None
            
        try:
            left_gantelet = Gantelet.objects.get(id=data_json.get("left_gantelet"))
        except Gantelet.DoesNotExist:
            left_gantelet = None
            
        try:
            right_gantelet = Gantelet.objects.get(id=data_json.get("right_gantelet"))
        except Gantelet.DoesNotExist:
            right_gantelet = None
            
        try:
            ring = Ring.objects.get(id=data_json.get("ring"))
        except Ring.DoesNotExist:
            ring = None
            
        try:
            amulet = Amulet.objects.get(id=data_json.get("amulet"))
        except Amulet.DoesNotExist:
            amulet = None
            
        try:
            belt = Belt.objects.get(id=data_json.get("belt"))
        except Belt.DoesNotExist:
            belt = None
        
        Character.objects.create(
            user = request.user,
            name = name,
            classe = classe,
            race = race,
            level = level,
            weapon = weapon,
            helmet = helmet,
            armor = armor,
            pant = pant,
            boots = boots,
            left_gantelet = left_gantelet,
            right_gantelet = right_gantelet,
            ring = ring,
            amulet = amulet,
            belt = belt
        )
        
        return JsonResponse({
            "success": True
        })
        
class Equipements(View):
    def get(self, request, type_e):
        query_class = str_to_class(type_e)
        query_set = query_class.objects.all()
        
        items = []
        for each in query_set:
            items.append({
                "id": each.id,
                "name": each.name,
                "name_id": each.name.replace(" ", "_"),
                "required_level": each.required_level,
                "hp": each.hp,
                "mana": each.mana,
                "attack": each.attack,
                "defense": each.defense,
                "speed": each.speed,
                "luck": each.luck,
                "picture": each.picture.url,
            })
            
        if type_e in ["epees", "arcs", "lances"]:
            type_e = "weapon"
        
        return JsonResponse({
            "message": "ok",
            "type": type_e,
            "items": items
        })
        
class ListPlayer(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("app_index")
        
        characters = Character.objects.filter(user=request.user).order_by('-id')
        
        return render(request, "player/list.html", {
            "characters": characters
        })
        
class DeletePlayer(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect("app_index")
        
        try:
            character = Character.objects.get(id=id, user=request.user)
            character.delete()
        except Character.DoesNotExist:
            pass
        
        return redirect("app_player_list")
    
class UpdatePlayer(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('app_index')
        
        try:
            character = Character.objects.get(id=id, user=request.user)
        except Character.DoesNotExist:
            return redirect("app_player_list")
        
        return render(request, "player/update.html", {
            "character": character,
            "races": Race.objects.all(),
            "classes": Classe.objects.all(),
            "equipements": ["helmet", "armor", "pant", "boots", "gantelet", "belt", "ring", "amulet"],
            "display_equipement": {
                "helmet": "un casque",
                "armor": "une armure",
                "pant": "un pantalon",
                "boots": "des bottes",
                "gantelet": "un gant",
                "belt": "une ceinture",
                "ring": "un anneau",
                "amulet": "une amulette",
                "weapon": "une arme",
            }
        })
        
    def post(self, request, id):
        if not request.user.is_authenticated:
            return JsonResponse({
                "error": ""
            })
            
        try:
            character = Character.objects.get(user=request.user, id=id)
        except Character.DoesNotExist:
            return JsonResponse({
                "success": False,
            })
            
        data = request.body.decode()
        data_json = json.loads(data)
        
        if data_json.get("name") is None:
            return JsonResponse({
                "success": False,
                "reason": "name"
            })
            
        if data_json.get("race") is None:
            return JsonResponse({
                "success": False,
                "reason": "race"
            })
            
        if data_json.get("classe") is None:
            return JsonResponse({
                "success": False,
                "reason": "classe"
            })
            
        try:
            character_check = Character.objects.get(user=request.user, name=data_json.get("name"))
            if character_check != character:
                return JsonResponse({
                    "success": False,
                    "reason": "name taken"
                })
        except Character.DoesNotExist:
            pass
        
        character.name = data_json.get("name")
        if data_json.get("level") is None:
            character.level = 0
        else:
            character.level = data_json.get("level")
            
        try:
            character.classe = Classe.objects.get(name=data_json.get("classe"))
        except Classe.DoesNotExist:
            return JsonResponse({
                "success": False,
                "reason": "classe not exists"
            })
            
        try:
            character.race = Race.objects.get(name=data_json.get("race"))
        except Race.DoesNotExist:
            return JsonResponse({
                "success": False,
                "reason": "race not exists"
            })
            
        try:
            character.weapon = Weapon.objects.get(id=data_json.get("weapon"))
        except Weapon.DoesNotExist:
            character.weapon = None
            
        try:
            character.helmet = Helmet.objects.get(id=data_json.get("helmet"))
        except Helmet.DoesNotExist:
            character.helmet = None
            
        try:
            character.armor = Armor.objects.get(id=data_json.get("armor"))
        except Armor.DoesNotExist:
            character.armor = None
            
        try:
            character.pant = Pant.objects.get(id=data_json.get("pant"))
        except Pant.DoesNotExist:
            character.pant = None
            
        try:
            character.boots = Boots.objects.get(id=data_json.get("boots"))
        except Boots.DoesNotExist:
            character.boots = None
            
        try:
            character.left_gantelet = Gantelet.objects.get(id=data_json.get("left_gantelet"))
        except Gantelet.DoesNotExist:
            character.left_gantelet = None
            
        try:
            character.right_gantelet = Gantelet.objects.get(id=data_json.get("right_gantelet"))
        except Gantelet.DoesNotExist:
            character.right_gantelet = None
            
        try:
            character.ring = Ring.objects.get(id=data_json.get("ring"))
        except Ring.DoesNotExist:
            character.ring = None
            
        try:
            character.amulet = Amulet.objects.get(id=data_json.get("amulet"))
        except Amulet.DoesNotExist:
            character.amulet = None
            
        try:
            character.belt = Belt.objects.get(id=data_json.get("belt"))
        except Belt.DoesNotExist:
            character.belt = None
            
        character.save()
        
        return JsonResponse({
            "success": True
        })
        
class ForgotPassword(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("app_index")
        
        form = ForgotPasswordForm()
        return render(request, "user/forgot_password.html", {
            "form": form
        })
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect("app_index")
        
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            print(email)
                
        return render(request, "user/forgot_password.html", {
            "form": form
        })