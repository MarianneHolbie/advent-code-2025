# Advent of Code 2025 - Day 5

import re


#####################
#     Part One      #
#####################

def process_file(path='input'):
    """Parse le fichier et retourne les ranges et les nombres."""
    with open(path, 'r') as f:
        content = f.read().split('\n\n')

    ranges = content[0].strip().split('\n')
    numbers = content[1].strip().split('\n')

    return ranges, numbers


def is_in_range(numbers, ranges):
    """Compte combien de nombres sont dans au moins un range."""
    count = 0
    for n in numbers:
        n = int(n)
        for r in ranges:
            start, end = map(int, r.split('-'))
            if start <= n <= end:
                count += 1
                break
    return count


#####################
#     Part Two      #
#####################

def parse_ranges(ranges):
    """Convertit les ranges en liste de tuples triés."""
    tuples = [tuple(map(int, r.split('-'))) for r in ranges]
    return sorted(tuples)


def merge_ranges(sorted_ranges):
    """Fusionne les intervalles qui se chevauchent."""
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_fresh_ids(merged):
    """Compte le total d'IDs dans les intervalles fusionnés."""
    return sum(end - start + 1 for start, end in merged)


#####################
#       Main        #
#####################

if __name__ == '__main__':
    ranges, numbers = process_file('input')

    # Part 1
    print("Part one:", is_in_range(numbers, ranges))

    # Part 2
    sorted_ranges = parse_ranges(ranges)
    merged = merge_ranges(sorted_ranges)
    print("Part two:", count_fresh_ids(merged))