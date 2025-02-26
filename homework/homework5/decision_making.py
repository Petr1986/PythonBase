import random


def decision_making(money: bool, drinker: bool, gave: bool, misser: bool) -> str:
    if not all(isinstance(arg, bool) for arg in (money, drinker, gave, misser)):
        raise TypeError("must be bool")
    if not money:
        return "you have no money"
    if drinker:
        return "he is a drinker"
    if not gave:
        return "he doesn't pay his debts"
    if misser:
        return "you are misser"
    else:
        return "you can land"


if __name__ == "__main__":

    money1 = random.choice([True, False])
    drinker1 = random.choice([True, False])
    gave1 = random.choice([True, False])
    misser1 = random.choice([True, False])

    result = decision_making(money1, drinker1, gave1, misser1)

    print(
        f" If money {money1}, drinker {drinker1}, gave {gave1}, misser {misser1}",
        result,
        sep="\n",
    )
