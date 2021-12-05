
# with open("input") as f:
#     lines = f.readlines()
#     lines = [line.rstrip() for line in lines]


# def gamma_bin(i):
#     zeroes = 0
#     ones = 0
#     for num in lines:
#         if num[i] == 0:
#             zeroes += 1
#         else: 
#             ones += 1
#     if zeroes > ones:
#         return '0'
#     else:
#         return '1'

# def epsilon_bin(gamma_bin):


# def binTodec(n):
#     return int(n,2)

# gamma = int(gamma_bin, 2)

# print(gamma_bin(lines))
with open('input') as f:
    lines = [line for line in f.read().split()]

gamma = ""
epsilon = ""

for i in range(len(lines[0])):
    zeroes = 0
    ones = 0
    for j in range(len(lines)):
        if lines[j][i] == '0':
            zeroes += 1
        else: ones += 1
    if zeroes > ones:
        gamma += '0'
        epsilon += '1'
    else: 
        gamma += '1'
        epsilon += '0'


g = int(gamma, 2)
e = int(epsilon, 2)

print(g * e)