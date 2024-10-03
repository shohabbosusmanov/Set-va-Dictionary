ls = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
ls.sort(key=lambda x: x[1], reverse=True)
print(ls)