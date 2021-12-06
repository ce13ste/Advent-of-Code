
with open("input") as f:
    lines = [x for x in f.read().split()]

lines2 = lines.copy()
index = 0
while len(lines) > 1:
    one = 0 
    zero = 0
    ones = []
    zeroes = []
    for i in range(len(lines)):
        if lines[i][index] == '0':
            zero += 1
            zeroes.append(lines[i])
        else:
            one += 1
            ones.append(lines[i])
    if zero > one:
        lines = zeroes
    else:
        lines = ones
    index += 1
oxygen_rating = int(lines[0],2)

lines = lines2
index = 0
while len(lines) > 1:
    one = 0 
    zero = 0
    ones = []
    zeroes = []
    for i in range(len(lines)):
        if lines[i][index] == '0':
            zero += 1
            zeroes.append(lines[i])
        else:
            one += 1
            ones.append(lines[i])
    if zero > one:
        lines = ones
    else:
        lines = zeroes
    index += 1
co2_rating = int(lines[0],2)

print(oxygen_rating * co2_rating)

