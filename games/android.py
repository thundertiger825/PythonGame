import math

N = int(input())
K = int(input())
i = 0
a = []
h = []
while (i < N):
    x = int(input())
    a.append(x)
    i = i + 1
har = 0
for z in range(N):

    for y in range(z + 1, N):
        h.append(abs(a[z] - a[y]))
        har = har + 1
q = h.sort()
b=[1,2,3,4,5]
s=b
print(s)
