#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""
from weapon_type import WeaponType

# Source packages.

class Pokemon():
    """Python class to implement a basic version of a Pokemon of the game.
    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """
    # ATRIBUTOS
    def __init__(self, ID, pokemon_name, weapon_type, health_points, atttack_rating, defense_rating):
        self.ID = int(ID)
        self.pokemon_name = str(pokemon_name)
        self.weapon_type = weapon_type #Puñetazo, Patada, Codazo, Cabezazo. CLASE WEAPON_TYPE
        self.health_points = int(health_points) # 1 - 100
        self.attack_rating = int(atttack_rating) # 1 - 10
        self.defense_rating = int(defense_rating) # 1 - 10
    # METODOS GETTERS Y SETTERS
    def get_pokemon_name(self): # Los metodos getters permiten acceder a los atributos de una clase de forma controlada. ACCEDER SIN MODIFICAR.
        return self.pokemon_name
    def get_weapon_type(self):
        return self.weapon_type
    def get_health_points(self):
        return self.health_points
    def get_attack_rating(self):
        return self.attack_rating
    def get_defense_rating(self):
        return self.defense_rating
    def set_pokemon_name(self, pokemon_name): #Los metodos setters permiten modificar los atributos de una clase de forma controlada. MODIFICAR DESDE FUERA DE LA CLASE
        self.pokemon_name = pokemon_name
    def set_weapon_type(self, weapon_type):
        self.weapon_type = weapon_type
    def set_health_points(self, health_points):
        self.health_points = health_points
    def set_attack_rating(self, attack_rating):
        self.attack_rating = attack_rating
    def set_defense_rating(self, defense_rating):
        self.defense_rating = defense_rating
    # METODO IS_ALIVE
    def is_alive(self):
        if self.health_points > 0:
            return True
        else:
            return False

    # METODO FIGHT_DEFENSE
    def fight_defense(self, damage):
        self.health_points = self.health_points - damage + self.defense_rating
        if self.health_points <= 0:
            return False
        else:
            return True


    # METODO FIGHT_ATTACK
    def fight_attack(self, pokemon_to_attack):
        self.health_points -= pokemon_to_attack.fight_defense(self.attack_rating)
        if self.health_points <= 0:
            return False
        else:
            return True

    # METODO STR
    def __str__(self):  #Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100
        return "Pokemon ID " + str(self.ID) + " with name " + self.pokemon_name + " has as weapon " + self.weapon_type.name + " and health " + str(self.health_points)




def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")                                         #TEST 1 SUPERADO
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
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
    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")
    




    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")          #TEST 2, FUNCION PERO NO PASA EL TEST
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)
    
    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))




    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")                             #TEST 3 SUPERADO
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")



    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")              #TEST 4 SUPERADO
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")               #TEST 5 SUPERADO
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

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
