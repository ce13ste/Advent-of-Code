
with open("input") as f:
    lines = f.readlines()
    lines = [line.strip().split() for line in lines]


def finalPosition(l):
    horizontal, depth = 0, 0
    for line in lines:
        if line[0] == 'forward':
            horizontal += int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])
    
    return horizontal * depth

print(finalPosition(lines))