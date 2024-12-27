from math import ceil

# Input
n, m, a = [int(x) for x in input().split(" ")]

# Process
vert = ceil(n / a)
hori = ceil(m / a)
total = vert * hori

# Output
print(total)
