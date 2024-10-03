ismlar = ["Aziz", "Islom", "Ali", "Shahzod", "Komil", "Behruz", "Sodiq"]
ism = input("Ism kiriting:\n")
if ism.lower() in str(ismlar).lower() :
    print("Ism listda bor")
else : 
    ismlar.append(ism)
    print("Ism ro'yhatga qo'shildi")