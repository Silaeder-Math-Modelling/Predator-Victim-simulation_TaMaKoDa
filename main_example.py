from strategy_advanced import *
# Обратите внимание: мы не импортируем ничего из objects,
# потому что все и так импортировано в файл со стратгией,
# и, возможно, там были произведены модификации (замена
# дополнительного инициализатора)


def main():
    objects = {Predator: [], Victim: []}
    objects[Predator].append(
        Predator(parent_intializer_kwargs={'age': 7},
            additional_initializer_kwargs={'max_velocity_when_not_hungry': 2})
        )
    for i in range(100):
        objects[Victim].append(Victim())

    while len(objects[Victim] > 10):
        world_iteration(objects)


if __name__ == "__main__":
    main()
