list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']
text = []
other = []
for i in list1:
    if type(i) == str:
        text.append(i)
    else:
        other.append(i)
text.sort()
other.sort(reverse=True)
print(f"TEXT = {text} \nOTHER = {other}")
