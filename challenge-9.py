print("<<<\t\tLatihan 1\t\t>>>")
print("Berikut akan tampil list dengan kondisi : ")
print("1. Range(1, 100)")
print("2. Value/Item : genap (i >= 10 dan i <= 20)")
print("3. Value/Item : ganjil (i >= 90 dan i <= 100)/n")
print()
list_num = []
for i in range(100) :
    i += 1
    if (i % 2 == 0) :
        if (i >= 10 and i <= 20) : 
            list_num.append(i)
    else :
        if (i >= 90 and i <= 100) :
            list_num.append(i)
print(f"{list_num}")
print()
print("<<<\t\tLatihan 2\t\t>>>")
list = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
list2 = list[2:3] + list[0:1] + list[3:7] + list[1:2]
print(f"{list2}")
print()
print("<<<\t\tLatihan 3\t\t>>>")
data = "IgNatIus"
list = []
len = len(data)
for i in range (len) :
    if data[i].isupper() :
        list.append(data[i])
print(f"{list}")