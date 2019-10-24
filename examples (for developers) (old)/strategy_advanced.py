from random import randint

from objects import * # Animal, Predator, Victim, ...

# Не забывайте, что вы можете еще объявлять тут какие-нить
# локальные функции чисто для себя или даже выносить
# некоторые функции, которые могут пригодиться многим
# стратегиям, в отдельный файл. Например, мб надо
# вынести туда функцию, которая находит ближайшую к
# хищнику жертву?

def animal_init(self, max_age=10):
    self.age = randint(0, max_age)

def predator_init(self, max_velocity_when_not_hungry):
    self.max_velocity_when_not_hungry = \
        max_velocity_when_not_hungry

def victim_init(self):
    self.stupidity = randint(0, 1000)

# Мы описали функции доп. инициализации выше. Теперь надо
# привязать их к классам из objects:
Animal.animal_additional_init = animal_init
Predator.predator_additional_init = predator_init
Victim.victim_additional_init = victim_init

def world_iteration(objects, ...):
    """Performs one iteration of the world's life
    Parameters:
        object (`dict`): {object_type (`type`): objects_of_this_type (`list`)}
            A dict from object type to the list of objects of this type
        ...
    """
    # Там, где троеточие в аргументах, передаются какие-то детали
    # процесса, который мы моделируем, например, размеры карты.
    # В этом примере далее считаем, что там были переданы
    # max_map_x и max_map_y как границы карты
    predators = objects[predators]
    not_predators = [obj for obj_type, obj in objects.items() \
        if issubclass(obj_type, Animal) and (obj_type is not Predator)]
    # 1. Если вы не понимаете про dict.items(),
    # тоже стоит погуглить. Про issubclass можно погуглить, а
    # можно догодаться
    # 2. Вот, почему ключи objects - это не строки, а типы.
    # Все-таки это файл с advanced стратегией
    # и я не удержался тут не рассказать. Смотрите, в этом примере
    # нам все равно, какие типы в принципе объявлены и существуют
    # в файле objects. Мы можем при помощи конструкции выше
    # собрать в принципе всех животных, которые не хищники.
    # Ну скажите, клево, а?

    pass # Ну, тут, понятно, делаем какие-нибудь операции
    # Если хотите, можете еще возвращать какую-то инфу, но
    # сомневаюсь, что это понадобится
