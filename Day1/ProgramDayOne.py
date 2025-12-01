#####################
#     Part One      #
#####################


position = 50
pointing_zero = 0

with open('input.txt') as f:
    line = f.readline()

    while line:
        line = line.strip()
        if not line:
            line = f.readline()
            continue

        number = ''.join(ch for ch in line if ch.isdigit())
        if line[0] == 'R' :
            position = (position + int(number)) % 100
            if position == 0:
                pointing_zero += 1
        else :
            position = (position - int(number)) % 100

            if position == 0:
                pointing_zero += 1

        line = f.readline()

print(pointing_zero)


#####################
#     Part Two      #
#####################

position = 50
full_pointing_zero = 0

with open('input.txt') as f:
    line = f.readline()

    while line:
        line = line.strip()
        if not line:
            line = f.readline()
            continue

        number = ''.join(ch for ch in line if ch.isdigit())
        if line[0] == 'R' :
            new_position = (position + int(number)) % 100
            # first click zero
            k0 = (100 -(position % 100)) % 100
            if k0 == 0:
                k0 = 100
            if k0 <= int(number):
                count_passe = 1 + (int(number) - k0) // 100
                full_pointing_zero += count_passe

        else :
            new_position = (position - int(number)) % 100

            # first click zero
            k0 = position % 100
            if k0 == 0:
                k0 = 100
            if k0 <= int(number):
                count_passe = 1 + (int(number) - k0) // 100
                full_pointing_zero += count_passe

        position = new_position
        line = f.readline()

print(full_pointing_zero)