from math import sqrt

from objects import Predator, Victim


def get_distance(a, b):
    """Returns the distance between two simulation
        objects
    Parameters:
        a, b (object): The objects to calculate
            distance between
    """
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def move_animal_from_another(animal_A, animal_B):
    """Moves animal_A away from animal_B
        not making steps greater than animal.velocity by each
        of the axes
    Parameters:
        animal_A (object): The animal, who run away
        animal_B (object): The animal, that animal_A run away from
    """
    def get_new_coordinate(animalA_coordinate, animalB_coordinate, \
            animalA_velocity, distance_AB):
        if animalA_coordinate - animalB_coordinate == 0:
            return animalA_coordinate
        elif animalA_coordinate > animalB_coordinate:
            return animalA_coordinate + animalA_velocity
        else:
            return animalA_coordinate - animalA_velocity
    
    if get_distance(animal_A, animal_B) < animal_A.visibility_area:
        animal_A.x = get_new_coordinate(animal_A.x, animal_B.x, \
                animal_A.velocity, get_distance(animal_A, animal_B))
        animal_A.y = get_new_coordinate(animal_A.y, animal_B.y, \
                animal_A.velocity, get_distance(animal_A, animal_B))


def _get_nearest_victim(predator, victims):
    """Returns a victim nearest to the predator
    Parameters:
        predator (Predator): The predator
        victims (list[Victim]): The list of victims
    Returns:
        victim: The nearest victim
    """
    ans = victims[0]
    for victim in victims:
        if get_distance(predator, victim) < \
                get_distance(predator, ans):
            ans = victim
    return ans

def _move_predator_to_victim(predator, victim):
    """Moves the given predator to the given victim,
        not making steps greater than predator.velocity by each
        of the axes
    Parameters:
        predator (Predator) - the predator to be moved
        victim (Victim) - the victim to be moved to
    """
    def get_new_coordinate(predator_coordinate, victim_coordinate, \
            predator_velocity):
        if(abs(predator_coordinate - victim_coordinate) <= predator_velocity):
            return victim_coordinate
        elif victim_coordinate < predator_coordinate:
            return predator_coordinate - predator_velocity
        elif victim_coordinate > predator_coordinate:
            return predator_coordinate + predator_velocity

    predator.x = get_new_coordinate(predator.x, victim.x, predator.velocity)
    predator.y = get_new_coordinate(predator.y, victim.y, predator.velocity)

def _clear_killed_victims(victims, predator):
    """Returns an array of victims which are not under the predator
    Parameters:
        victims (list[Victim]): The list of victims to be filtered
        predator (Predator): The predator
    Returns:
        tuple(list[Victim], int): Alive victims and number of killed victims
    """
    ans = [victim for victim in victims if victim.x != predator.x or \
        victim.y != predator.y]
    return (ans, len(victims) - len(ans))

def predator_move(objects): # Is common for all strategies (by the problem condition)
    """Simulates the predator move in a certain simulation iteration
    Parameters:
        objects (dict{type: list[objects_of_this_type]}): The simulation objects
    Returns:
        dict{type: list[objects_of_this_type]}: The simulation objects after
            the predator's move
    """
    predator = objects[Predator][0]
    victims = objects[Victim]

    if predator.ready_to_run_in != 0:
        predator.ready_to_run_in -= 1
    else:
        _move_predator_to_victim(predator, \
            _get_nearest_victim(predator, victims))
    victims, n_of_killed = _clear_killed_victims(victims, predator)
    predator.ready_to_run_in += predator.victim_eating_time * n_of_killed
    objects[Victim] = victims

    return objects


def normalize_coordinates_to_field_size(animals, field_size):
    """Moves animals which are out of the field bounds back to it
    Parameters:
        animals (list): List of `Animal` or `Animal`-inheritanced
            objects to be moved back to the field
        field_size (tuple(int, int)): The field size
    """
    for animal in animals:
        if animal.x < 0:
            animal.x = 0
        elif animal.x >= field_size[0]:
            animal.x = field_size[0] - 1
        if animal.y < 0:
            animal.y = 0
        elif animal.y >= field_size[1]:
            animal.y = field_size[1] - 1