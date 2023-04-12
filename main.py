import csv
from pokemon import Pokemon
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity
from pokemon_water import PokemonWater
# Source packages.

def get_data_from_user(name_file):
    """
    Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """
    lista = []
    with open(name_file, newline='') as File:
        reader = csv.reader(File)
        for row in reader: # CONVERTIR EN CLASES
            pokemons = Pokemon(int(row[0]), str(row[1]), row[2], int(row[3]), int(row[4]), int(row[5]))
            lista.append(pokemons)
    for pokemon in lista:
       if pokemon.get_pokemon_name == 'Pikachu': #ELECTRICITY
          pokemon = PokemonElectricity(pokemon.get_id, pokemon.get_name, pokemon.get_type, pokemon.get_health_points, pokemon.get_attack_points, pokemon.get_defense_points)
       elif pokemon.get_pokemon_name == 'Pidgey': #AIR
          pokemon = PokemonAir(pokemon.get_id, pokemon.get_name, pokemon.get_type, pokemon.get_health_points, pokemon.get_attack_points, pokemon.get_defense_points)
       elif pokemon.get_pokemon_name == 'Diglett': #EARTH
          pokemon = PokemonEarth(pokemon.get_id, pokemon.get_name, pokemon.get_type, pokemon.get_health_points, pokemon.get_attack_points, pokemon.get_defense_points)
       elif pokemon.get_pokemon_name == 'Squirtle': #WATER
          pokemon = PokemonWater(pokemon.get_id, pokemon.get_name, pokemon.get_type, pokemon.get_health_points, pokemon.get_attack_points, pokemon.get_defense_points)
       else:
          pass
    return lista




def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """
    primer_pokemon = list_of_pokemons[0]
    segundo_pokemon = list_of_pokemons[1]
    tercer_pokemon = list_of_pokemons[2]
    for i in range(3):
        print("Pokemon", i+1, ":", list_of_pokemons[i].get_pokemon_name(), "with", list_of_pokemons[i].get_health_points(), "health points")
    return list_of_pokemons, primer_pokemon, segundo_pokemon, tercer_pokemon





def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """
    for i in range(len(list_of_pokemons)):
        if list_of_pokemons[i].is_alive():
            return True
    return False

def coach(list_pokemons, user):
  choice = input("Player "+  user + " choose your pokemon: ")
  for i in range(len(list_pokemons)):
    if choice == list_pokemons[i].get_pokemon_name():
      pokemon_user = list_pokemons[i]
      return pokemon_user
    else:
      raise ValueError("You have not chosen a valid pokemon")


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

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

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    user1 = input("Please, introduce the name of the Game User 1: ")
    list_pokemons_user1 = get_data_from_user("coach_1_pokemons.csv")
    get_pokemon_in_a_list_of_pokemons(user1, list_pokemons_user1)

    # Get configuration for Game User 2.
    user2 = input("Please, introduce the name of the Game User 2: ")
    list_pokemons_user2 = get_data_from_user("coach_2_pokemons.csv")
    get_pokemon_in_a_list_of_pokemons(user2, list_pokemons_user2)

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    list_pokemons_user1_copy = list_pokemons_user1.copy()
    list_pokemons_user2_copy = list_pokemons_user2.copy()

    # Choose first pokemons
    pokemon_user_1 = coach(list_pokemons_user1_copy, user1)
    pokemon_user_2 = coach(list_pokemons_user2_copy, user2)

    # Main loop.
    if not coach_is_undefeated(list_pokemons_user1_copy) and not coach_is_undefeated(list_pokemons_user2_copy):
      pokemon_user_1.attack_rating(pokemon_user_2)
      pokemon_user_2.attack_rating(pokemon_user_1)
      if pokemon_user_1.is_alive == False:
        list_pokemons_user1_copy.remove(pokemon_user_1)
        user1 = coach(list_pokemons_user1_copy, user1)
      if pokemon_user_2.is_alive ==False:
        list_pokemons_user2_copy.remove(pokemon_user_2)
        user2 = coach(list_pokemons_user2_copy, user2)
      if not coach_is_undefeated(list_pokemons_user1_copy):
        print("The winner is", user2)
      if not coach_is_undefeated(list_pokemons_user2_copy):
        print("The winner is", user1)


    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    for i in range(len(list_pokemons_user1)):
        print("Pokemon", i+1, ":", list_pokemons_user1[i].get_pokemon_name(), "with", list_pokemons_user1[i].get_health_points(), "health points")


    print("Game User 2:")
    for i in range(len(list_pokemons_user2)):
        print("Pokemon", i+1, ":", list_pokemons_user2[i].get_pokemon_name(), "with", list_pokemons_user2[i].get_health_points(), "health points")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
