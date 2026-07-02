#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    StrategyError,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(len(opponents), "opponents involved")

    for i, (factory_1, strategy_1) in enumerate(opponents):
        for factory_2, strategy_2 in opponents[i + 1:]:
            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()

            print()
            print("* Battle *")
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")

            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
            except StrategyError as e:
                print("Battle error, aborting tournament:", e)
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    battle([(flame, normal), (healing, defensive)])
    print()

    print("Tournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([(flame, aggressive), (healing, defensive)])
    print()

    print("Tournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
