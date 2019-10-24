from random import randint

# Have to do the following to let main file
# import all the required objects from me
from objects import *
from common_for_strategies import predator_move, \
    normalize_coordinates_to_field_size

def world_iteration(objects, max_field_x, max_field_y):
    """Performs one iteration of the world's life
    Parameters:
        object (dict): {object_type (`type`): objects_of_this_type (`list`)}
            A dict from objects' type to the list of the objects of this type
        max_field_x, max_field_y (int): the field size
    """
    predators = objects[Predator]
    if len(predators) != 1:
        raise ValueError("There must be exactly one predator")
    predator = predators[0]

    victims = objects[Victim]
    if len(victims) == 0:
        raise ValueError("There must be at least one victim")

    for victim in victims:
        victim.x += randint(-victim.velocity, victim.velocity)
        victim.y += randint(-victim.velocity, victim.velocity)

    normalize_coordinates_to_field_size(
        [predator] + [victim for victim in victims], (max_field_x, max_field_y)
        )

    objects[Victim] = victims
    objects[Predator] = [predator]

    objects = predator_move(objects)

    return objects