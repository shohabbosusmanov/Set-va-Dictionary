ls = list(map(int, input("list elementlarini probel bilan kiriting\n").split()))
matn = input("matn kiriting:\n")
for i in range(len(ls)) :
    ls[i] = matn + str(ls[i])
print(ls)