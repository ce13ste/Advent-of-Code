
with open("input") as f:
    lines = f.readlines()
    lines = [line.strip().split() for line in lines]


def finalPosition(l):
    horizontal, depth, aim = 0, 0, 0
    for line in lines:
        if line[0] == 'forward':
            horizontal += int(line[1])
            depth += int(line[1]) * aim
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
    
    return horizontal * depth

print(finalPosition(lines))