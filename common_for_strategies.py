from math import sqrt
from random import randint

from objects import Predator, Victim


def get_distance(objectA, objectB):
    """Returns the distance between two simulation
        objects
    Parameters:
        objectA, objectB (object): The objects to calculate
            distance between
    """
    return sqrt((objectA.x - objectB.x)**2 + (objectA.y - objectB.y)**2)


def move_victim_random(victim, predator):
    x_move = 0
    y_move = 0
    if randint(0, 99) < 30:
        x_move = randint(-victim.velocity, victim.velocity)
        y_move = randint(-victim.velocity, victim.velocity)
    if sqrt((victim.x + x_move - predator.x)**2 + (victim.y + y_move - predator.y)**2) > victim.visibility_area:
        victim.x += x_move
        victim.y += y_move

def move_animal_from_another(animalA, animalB):
    """Moves animalA away from animalB
        not making steps greater than animal.velocity by each
        of the axes
    Parameters:
        animalA (object): The animal, which runs away
        animalB (object): The animal, which animalA runs away from
    """
    def get_new_coordinate(animalA_coordinate, animalB_coordinate, \
            animalA_velocity):
        if animalA_coordinate == animalB_coordinate:
            return animalA_coordinate
        elif animalA_coordinate > animalB_coordinate:
            return animalA_coordinate + animalA_velocity
        else:
            return animalA_coordinate - animalA_velocity
    
    animalA.x = get_new_coordinate(animalA.x, animalB.x, \
            animalA.velocity)
    animalA.y = get_new_coordinate(animalA.y, animalB.y, \
            animalA.velocity)


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