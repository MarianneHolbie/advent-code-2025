# Advent of Code 2025 - Day3

#####################
#     Part One      #
#####################

def find_max_number(line: str):
    """Trouve le plus grand nombre à 2 chiffres dans la ligne en respectant l'ordre."""
    len_line = len(line)
    max_value = 0
    for i in range(len_line - 1):
        n = int(line[i])

        if n > max_value:
            max_value = n
            i_max_value = i
    return i_max_value, max_value

def find_max_right(line: str, i_max_value: int):
    """Trouve le chiffre le plus grand à droite du max."""
    len_line = len(line)
    max_r_value = 0

    for i in range(i_max_value + 1, len_line):
        m = int(line[i])
        if m > max_r_value:
            max_r_value = m
    return max_r_value

def process_file(path='input'):
    total = 0
    with open(path, 'r') as f:
        while line := f.readline():
            line = line.strip()


            i_max_value, left_value = find_max_number(line)
            right_value = find_max_right(line, i_max_value)
            concat_value = int(str(left_value) + str(right_value))
            total += int(concat_value)

        return total


#####################
#     Part Two      #
#####################

def find_max_twelve_number(line: str, start, end):
    """Trouve le plus grand nombre à 12 chiffres dans la ligne en respectant l'ordre."""
    len_line = len(line)
    max_chiffre = 0
    max_value = 0
    for i in range (start, end + 1 ):
        n = int(line[i])

        if n > max_value:
            max_value = n
            i_max_value = i
    return i_max_value, max_value



def process_file_part2(path='input'):
    total = 0
    concat_value = ''

    with open(path, 'r') as f:
        while line := f.readline():
            line = line.strip()
            restant = 12

            if len(line) == 12:
                total += int(line)
                continue

            start = 0

            for i in range (1, 13):
                end = len(line) - restant
                j, max_val = find_max_twelve_number(line, start, end)
                start = j + 1
                restant -= 1
                concat_value += str(max_val)
            total += int(concat_value)
            concat_value = ''

        return total




if __name__ == '__main__':
    print(process_file('input'))
    print(process_file_part2('input'))


