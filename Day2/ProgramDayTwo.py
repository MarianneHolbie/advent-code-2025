# Advent of Code 2025 - Day2

#####################
#     Part One      #
#####################
import re




def parse_ranges_regex(line: str):
    """Avec regex : trouve toutes les paires 'N-N' et retourne (ranges, max_value)."""
    matches = re.findall(r'(\d+)-(\d+)', line)
    ranges = [(int(a), int(b)) for a, b in matches]
    max_value = max((b for _, b in ranges), default=None)
    return ranges, max_value


def generate_all_invalid_ids(max_val):
    invalid = []
    k = 1  # longueur du préfixe
    while True:
        min_p = 1 if k == 1 else 10 ** (k - 1)  # pas de zéro en tête
        max_p = 10 ** k - 1
        for p in range(min_p, max_p + 1):
            num = int(str(p) + str(p))  # ou p * 10**k + p
            if num > max_val:
                return invalid
            invalid.append(num)
        k += 1

def process_file(path='input'):
    invalid_ID = 0
    with open(path, 'r') as f:
        line = f.readline()

        ranges, max_value = parse_ranges_regex(line)

        all_invalid_ids = generate_all_invalid_ids(max_value)

    total = 0
    for start, end in ranges:
        for invalid_id in all_invalid_ids:
            if start <= invalid_id <= end:
                total += invalid_id

    return total



#####################
#     Part Two      #
#####################


def parse_ranges_regex(line: str):
    """Avec regex : trouve toutes les paires 'N-N' et retourne (ranges, max_value)."""
    matches = re.findall(r'(\d+)-(\d+)', line)
    ranges = [(int(a), int(b)) for a, b in matches]
    max_value = max((b for _, b in ranges), default=None)
    return ranges, max_value


def generate_new_all_invalid_ids(max_val):
    invalid = set()
    k_max = len(str(max_val)) // 2

    for k in range(1, k_max + 1):
        min_p = 1 if k == 1 else 10 ** (k - 1)
        max_p = 10 ** k - 1

        for p in range(min_p, max_p + 1):
            r = 2
            p_string = str(p)
            while int((p_string * r)) <= max_val:
                invalid.add(int(p_string * r))
                r += 1
    return invalid


def process_file_part2(path='input'):
    with open(path, 'r') as f:
        line = f.readline()

        ranges, max_value = parse_ranges_regex(line)

        all_invalid_ids = generate_new_all_invalid_ids(max_value)

    total = 0
    for start, end in ranges:
        for invalid_id in all_invalid_ids:
            if start <= invalid_id <= end:
                total += invalid_id

    return total


if __name__ == '__main__':
    print(process_file('input'))
    print(process_file_part2('input'))