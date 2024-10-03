n = int(input("n sonini kiriting:\n"))
tub = []
i = 0
m = n + 1
while i < 5 :
    s = 0
    for j in range(2, m) :
        if m % j == 0 :
            s = 1
            break
    if s == 0:
        tub.append(m)
        i += 1
    m += 1
print("n sonidan keyingi 5 ta tub son:", tub)