with open("input") as f:
    lines = f.readlines()
    lines = [int(line.strip()) for line in lines]
    
def adj(l):
    s = [l[i] < l[i+1] for i in range(len(l)-1)]
    print(sum(s))

adj(lines)