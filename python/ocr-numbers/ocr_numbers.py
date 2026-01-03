def convert(input_grid):
    if not input_grid or len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    digit_map = {
        (" _ ",
         "| |",
         "|_|",
         "   "): '0',
        ("   ",
         "  |",
         "  |",
         "   "): '1',
        (" _ ",
         " _|",
         "|_ ",
         "   "): '2',
        (" _ ",
         " _|",
         " _|",
         "   "): '3',
        ("   ",
         "|_|",
         "  |",
         "   "): '4',
        (" _ ",
         "|_ ",
         " _|",
         "   "): '5',
        (" _ ",
         "|_ ",
         "|_|",
         "   "): '6',
        (" _ ",
         "  |",
         "  |",
         "   "): '7',
        (" _ ",
         "|_|",
         "|_|",
         "   "): '8',
        (" _ ",
         "|_|",
         " _|",
         "   "): '9',
    }

    rows = len(input_grid)
    cols = len(input_grid[0])
    result = []

    for row_start in range(0, rows, 4):
        line_digits = []
        for col_start in range(0, cols, 3):
            digit_representation = tuple(
                input_grid[row_start + r][col_start:col_start + 3] for r in range(4)
            )
            line_digits.append(digit_map.get(digit_representation, '?'))
        result.append(''.join(line_digits))

    return ','.join(result)