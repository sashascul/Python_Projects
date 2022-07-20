L = []
with open("youscore.txt", "r") as f:
    for line in f:
        L.append(line)

L.sort(reverse=True)

sor = ["0", "0", "0", "0", "0"]

for i in range(len(L)):
    sor[i] = L[i]

