#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    healing_base = healing_factory.create_base()
    healing_evolved = healing_factory.create_evolved()

    print(" base:")
    print(healing_base.describe())
    print(healing_base.attack())
    print(healing_base.heal())

    print(" evolved:")
    print(healing_evolved.describe())
    print(healing_evolved.attack())
    print(healing_evolved.heal())
    print()

    print("Testing Creature with tranform capability")
    transform_base = transform_factory.create_base()
    transform_evolved = transform_factory.create_evolved()

    print(" base:")
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())

    print(" evolved:")
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(transform_evolved.transform())
    print(transform_evolved.attack())
    print(transform_evolved.revert())


if __name__ == "__main__":
    main()
