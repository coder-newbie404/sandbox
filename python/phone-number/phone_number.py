class PhoneNumber:
    def __init__(self, number):
        self.number = self._clean_number(number)
        self.area_code = self.number[0:3]

    def _clean_number(self, number):
        for i in number:
            if i.isalpha():
                raise ValueError("letters not permitted")
            if i in ('@', '!', '#', '$', '%', '^', '&', '*'):
                raise ValueError("punctuations not permitted")
        digits = ''.join(filter(str.isdigit, number))
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
            if digits[0] == '1':
                digits = digits[1:]
            else:
                raise ValueError("11 digits must start with 1")

        # Validate area code (first digit) and exchange code (fourth digit)
        if digits[0] == '0':
            raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
            raise ValueError("area code cannot start with one")
        if digits[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
            raise ValueError("exchange code cannot start with one")
        return digits

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}"
