# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    if category == "YACHT":
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0
    elif category == "ONES":
        return dice.count(1) * 1
    elif category == "TWOS":
        return dice.count(2) * 2
    elif category == "THREES":
        return dice.count(3) * 3
    elif category == "FOURS":
        return dice.count(4) * 4
    elif category == "FIVES":
        return dice.count(5) * 5
    elif category == "SIXES":
        return dice.count(6) * 6
    elif category == "FULL_HOUSE":
        unique_values = set(dice)
        if len(unique_values) == 2:
            first, second = unique_values
            if (dice.count(first) == 2 and dice.count(second) == 3) or (dice.count(first) == 3 and dice.count(second) == 2):
                return sum(dice)
        return 0
    elif category == "FOUR_OF_A_KIND":
        for value in set(dice):
            if dice.count(value) >= 4:
                return value * 4
        return 0
    elif category == "LITTLE_STRAIGHT":
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    elif category == "BIG_STRAIGHT":
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    elif category == "CHOICE":
        return sum(dice)
    else:
        return 0