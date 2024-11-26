royxat = ["cobalt", "Malibu", "Thoe", "Gentra"]

while True:
    try:
        a = int(input("Indeksni kiriting (0 dan 3 gacha) = "))
        print("Tanlangan element:", royxat[a])
        break
    except IndexError:
        print("Noto'g'ri indeks (0-3) oralig'idagi bo'lasin")