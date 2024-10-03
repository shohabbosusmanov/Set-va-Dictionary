ls = []
for i in range(4) :
    n = list(map(int, input(f"{i + 1} - list elementlarini probel bilan kiriting\n").split()))
    ls.append(n)
s = 0
index = 0
for j in range(4) :
    if sum(ls[j]) > s :
        s = sum(ls[j])
        index = j
print(ls[index])