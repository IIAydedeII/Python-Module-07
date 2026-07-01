#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def verify_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")

    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()

    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())

    print(" fight!")
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    verify_factory(flame_factory)
    print()

    verify_factory(aqua_factory)
    print()

    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
