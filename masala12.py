ls = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
s = list(ls.pop())
s[-1] = 100
s = tuple(s)
ls.append(s)
print(ls)