ls = []
i = 0
nol = 0
bir = 1
keyingi = 0
while i < 50 :
    ls.append(keyingi)
    nol = bir
    bir = keyingi
    keyingi = bir + nol
    i += 1
print(f"dastlabki 50 ta fibonchchi sonlari:\n{ls}")