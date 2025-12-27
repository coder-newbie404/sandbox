def say(number):
    if not (0 <= number <= 999_999_999_999):
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    def one(num):
        switcher = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }
        return switcher.get(num)

    def two_less_20(num):
        switcher = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        return switcher.get(num)

    def ten(num):
        switcher = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        }
        return switcher.get(num)
    
    def helper(num):
        if num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        elif num < 100:
            tenner = num // 10
            rest = num % 10
            return ten(tenner) + ('' if rest == 0 else '-' + one(rest))
        elif num < 1000:
            hundrer = num // 100
            rest = num % 100
            return helper(hundrer) + ' hundred' + ('' if rest == 0 else ' ' + helper(rest))
        elif num < 1_000_000:
            thousander = num // 1000
            rest = num % 1000
            return helper(thousander) + ' thousand' + ('' if rest == 0 else ' ' + helper(rest))
        elif num < 1_000_000_000:
            millioner = num // 1_000_000
            rest = num % 1_000_000
            return helper(millioner) + ' million' + ('' if rest == 0 else ' ' + helper(rest))
        else:
            milliarder = num // 1_000_000_000
            rest = num % 1_000_000_000
            return helper(milliarder) + ' billion' + ('' if rest == 0 else ' ' + helper(rest))
        
    return helper(number)


