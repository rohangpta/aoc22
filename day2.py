data = open("input2.txt", "r").read().split("\n")
base = {"X": 1, "A": 1, "B": 2, "Y": 2, "Z": 3, "C": 3}


def get_losing(c):
    return ((c + 1) % 3) + 1


def solve1(other_, me_) -> int:
    other = base[other_]
    me = base[me_]
    return me + (3 if me == other else (6 if other == get_losing(me) else 0))


def solve2(other, me) -> int:
    if me == "X":
        return get_losing(base[other])
    elif me == "Z":
        return get_losing(get_losing(base[other])) + 6
    return base[other] + 3


for i, func in enumerate([solve1, solve2]):
    print(
        f"Soln to part {i + 1} is {sum(map(lambda line: func(*line.split()) if line else 0, data))}"
    )
