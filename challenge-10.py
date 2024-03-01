#Fibonacci 1 2 3 5 8 13 21 34
print("\t<<< FIBONACCI >>>\t")
print("-"*35)
n = int(input("Masukkan angka : "))
print("-"*35)
data = []
for i in range(n) :
    if (i == 0) :
        data.append(1)
    elif (i == 1) :
        data.append(1)
    else :
        data.append(data[i-1] + data[i-2])
print(data)
print("-"*35)
print("\t<<< FIBONACCI >>>\t")
print("-"*35)
n = int(input("Masukkan angka : "))
print("-"*35)
data = [1 if i <= 1 else data[i-1]+data[i-2] for i in range(n) ]
print(data)