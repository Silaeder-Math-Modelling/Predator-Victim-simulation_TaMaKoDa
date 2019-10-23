from math import sqrt

def get_nearest_victim(predator, victims):
    """Returns a victim nearest to the predator
    Parameters:
        predator (Predator): The predator
        victims (list[Victim]): The list of victims
    Returns:
        victim: The nearest victim
    """
    ans = victims[0]
    for victim in victims:
        distance = lambda a, b: sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
        if distance(predator, victim) < distance(predator, ans):
            ans = victim
    return ans

def move_predator_to_victim(predator, victim):
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

def clear_killed_victims(victims, predator):
    """Returns an array of victims which are not under the predator
    Parameters:
        victims (list[Victim]): The list of victims to be filtered
        predator (Predator): The predator
    Returns:
        list[Victim]: Alive victims
    """
    return [victim for victim in victims if victim.x != predator.x or \
        victim.y != predator.y]

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