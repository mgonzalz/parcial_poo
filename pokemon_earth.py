
# Source packages.
from weapon_type import WeaponType

from pokemon import Pokemon
class PokemonEarth(Pokemon):
    def __init__(self, ID, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        super().__init__(ID, pokemon_name, weapon_type, health_points, attack_rating, defense_rating)
        if 11<= defense_rating <= 20: #EL INDICE DE DEFENSA DEBE SER MAYOR IGUAL QUE 11 Y MENOR IGUAL QUE 20
            self.defense_rating = defense_rating
        else:
            return False
    def fight_attack(self, pokemon_to_attack):
        self.health_points -= pokemon_to_attack.attack_rating

def main():
    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")                             #TEST 1 SUPERADO
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", WeaponType.HEADBUTT, 100, 8, 15)

    if pokemon_1.get_pokemon_name() == "Diglett":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", WeaponType.HEADBUTT, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", WeaponType.KICK, 97, 8, 15)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonEarth(4, "Diglett", WeaponType.ELBOW, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", WeaponType.PUNCH, 99, 10, 20) #Pokemon(ID, nombre, tipo, vida, ataque, defensa)
    pokemon_6 = PokemonEarth(6, "Diglett", WeaponType.PUNCH, 99, 9, 18)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
