class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # check if all char in input is number 
        cleaned = self.card_num.replace(" ", "")
        for i in cleaned:
            if not (i.isdigit()):
                return False
        if len(cleaned) < 2:
            return False
        # Check if all characters are digits
        if not cleaned.isdigit():
            return False
        # Apply Luhn algorithm
        total = 0
        for i, digit in enumerate(reversed(cleaned)):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0