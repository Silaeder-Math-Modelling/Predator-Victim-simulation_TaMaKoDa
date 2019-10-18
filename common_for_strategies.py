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