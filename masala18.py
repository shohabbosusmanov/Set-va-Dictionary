numbers = (12, 35, 22, 49, 50, 47, 43, 67, 98, 12, 97, 31, 45, 63, 83, 38, 24)
toq = []
juft = []
for i in numbers :
    if i % 2 == 0 :
        juft.append(i)
    else :
        toq.append(i)
print(f"juft: {tuple(juft)} \ntoq: {tuple(toq)}")