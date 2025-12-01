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