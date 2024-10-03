ls = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
for i in range(len(ls) - 1, -1, -1) :
    if len(ls[i]) < 1 :
        del ls[i]

print(ls)