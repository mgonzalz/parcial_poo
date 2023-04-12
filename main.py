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
            pokemons = Pokemon(int(row[0]), str(row[1]), row[2], int(row[3]), int(row[4]), int(row[5])) #Se les ha establecido todos la clase Pokemon, ya que los pokemons no cumplen las condiciones de las otras clases derivadas.
            lista.append(pokemons)
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
    for i in range(len(list_of_pokemons)):
      print("Pokemon", i+1, ":", list_of_pokemons[i].get_pokemon_name(), "with", list_of_pokemons[i].get_health_points(), "health points")
    pokemon_selected = int(input("Please, select a Pokemon for " + coach_to_ask + ": "))
    print("Put the numer of the Pokemon that you want to select.")
    if pokemon_selected > len(list_of_pokemons):
      raise ValueError("The Pokemon selected is not valid. Please, select a valid Pokemon.")
    else:
      print("The Pokemon selected is: ", list_of_pokemons[pokemon_selected-1].get_pokemon_name())
      return list_of_pokemons[pokemon_selected-1]



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
    
    # Get configuration for Game User 2.
    user2 = input("Please, introduce the name of the Game User 2: ")
    list_pokemons_user2 = get_data_from_user("coach_2_pokemons.csv")

    users = [user1, user2]

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    list_pokemons_user1_copy = list_pokemons_user1.copy() #PROBAR SINO EL copy.deepcopy(lista) con import copy
    list_pokemons_user2_copy = list_pokemons_user2.copy()

    # Choose first pokemons
    pokemon_user1 = get_pokemon_in_a_list_of_pokemons(user1, list_pokemons_user1_copy)
    pokemon_user2 = get_pokemon_in_a_list_of_pokemons(user2, list_pokemons_user2_copy)

    
    # Main loop.
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
