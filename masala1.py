a, b = map(int, input("a va b sonlarini kiriting: \n").split())
ls = []
for a in range(a, b):
    if a % 2 == 0:
        ls.append(a)
print(ls)
