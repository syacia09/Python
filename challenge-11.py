data = "IgNatIus"
list = []
len = len(data)
for i in range (len) :
    if data[i].isupper() :
        list.append(data[i])
print(f"{list}")