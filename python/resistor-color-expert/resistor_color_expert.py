def resistor_label(colors):
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    tolerance_codes = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }
    # helper to format numbers without unnecessary trailing .0
    def _fmt(n):
        return "{:g}".format(n)
    if len(colors) == 1:
        return f"{color_codes[colors[0]]} ohms"
    elif len(colors) == 4:
        first_digit = color_codes[colors[0]]
        second_digit = color_codes[colors[1]]
        multiplier = 10 ** color_codes[colors[2]]
        tolerance = tolerance_codes[colors[3]]
        
        value = (first_digit * 10 + second_digit) * multiplier

        if value >= 1_000_000_000:
            return f"{_fmt(value / 1_000_000_000)} gigaohms ±{tolerance}%"
        elif value >= 1_000_000:
            return f"{_fmt(value / 1_000_000)} megaohms ±{tolerance}%"
        elif value >= 1_000:
            return f"{_fmt(value / 1_000)} kiloohms ±{tolerance}%"
        else:
            return f"{_fmt(value)} ohms ±{tolerance}%"
    else:
        first_digit = color_codes[colors[0]]
        second_digit = color_codes[colors[1]]
        third_digit = color_codes[colors[2]]
        multiplier = 10 ** color_codes[colors[3]]
        tolerance = tolerance_codes[colors[4]]

        value = (first_digit * 100 + second_digit * 10 + third_digit) * multiplier

        if value >= 1_000_000_000:
            return f"{_fmt(value / 1_000_000_000)} gigaohms ±{tolerance}%"
        elif value >= 1_000_000:
            return f"{_fmt(value / 1_000_000)} megaohms ±{tolerance}%"
        elif value >= 1_000:
            return f"{_fmt(value / 1_000)} kiloohms ±{tolerance}%"
        else:
            return f"{_fmt(value)} ohms ±{tolerance}%"
        