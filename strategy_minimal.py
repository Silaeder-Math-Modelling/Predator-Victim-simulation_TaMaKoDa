from random import randint

from objects import * # Predator, Victim, ...
# (так, как в предыдущей строчке, писать довольно некрасиво,
# но нам придется так делать, чтобы main мог импортировать
# из нас всё, что объявлено в objects)

# Не забывайте, что вы можете еще объявлять тут какие-нить
# локальные функции чисто для себя или даже выносить
# некоторые функции, которые могут пригодиться нескольким
# стратегиям, в отдельный файл

def world_iteration(objects, ...):
    """Performs one iteration of the world's life
    Parameters:
        object (dict): {object_type (`type`): objects_of_this_type (`list`)}
            A dict from objects' type to the list of the objects of this type
        ...
    """
    # Обратите внимание: ключами словаря objects не являются
    # строки! Ключами словаря objects являются типы. То есть
    # сами слова Predator, Victim. Теоретически я знаю
    # ситуацию, в которой такой ход нам бы пригодился,
    # но я очень сомневаюсь, что мы доведем задачу до состояния,
    # когда нам понадобится использовать это, так что
    # просто считайте, что это для красоты. Имхо, это
    # выглядит эстетично

    # Там, где троеточие в аргументах выше, передаются какие-то детали
    # процесса, который мы моделируем, например, размеры карты.
    # В этом примере далее считаем, что там были переданы
    # max_map_x и max_map_y как границы карты

    predators = objects[Predator]
    assert(len(predators) == 1) # Мы ведь считаем, что хищник 1?
    predator = predators[0]

    victims = objects[Victim]

    # Просто для примера как-нибудь подвинем хищника
    predator.x += 0.4
    predator.y += 0.4
    if predator.x > max_map_x:
        predator.x = max_map_x
    if predator.y > max_map_y:
        predator.y = max_map_y

    # Ну и жертв тоже как-нить там
    for victim in victims:
        victim.x -= 1.2
        victim.y += 0.1
        if victim.x < 0:
            victim.x = 0
        if victim.y > max_map_y:
            victim.y = max_map_y

    # Не забудем убить всех тех, кто попался волку, да?
    victims = [victim for victim in victims \
        if ((victim.x != predator.x) or (victim.y != predator.y))]
    # Если не понимаете синтаксис конструкции выше, то тоже
    # погуглите, что такое generator expressions в питоне

    # А еще на жертв напала чума (только почему-то после
    # того, как на них напал хищник...) и выкосила чутка:
    victims = [victim for victim in victims \
        if (randint(1, 50) != 1)]

# ОБРАТИТЕ ВНИМАНИЕ!!! В этом файле со стратегией объявлена функция,
# которая выполняет ОДИН шаг в мире, а не цикл шагов. Это очень
# важно для некоторых ситуаций, например, для рисования графики:
# цикл должен быть в главном файле, который исполняет стратегию,
# тогда он сможет делать что-нибудь еще на шагах мира, например
# выполнять отрисовку, делать паузы и т. д.
