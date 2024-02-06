x = int(input("Masukkan nilai x : "))
y = int(input("Masukkan nilai y : "))

if (x > 0 and y > 0) :
    print("Titik tersebut berada di kuadran 1")
elif (x < 0 and y > 0) :
    print("Titik tersebut berada di kuadran 2")
elif (x < 0 and y < 0) :
    print("Titik tersebut berada di kuadran 3")
elif (x > 0 and y < 0):
    print("Titik tersebut berada di kuadran 4")
elif (x == 0 and y == 0) :
    print("Titik tersebut berada di Titik Pusat")
elif (x == 0) :
    print("Titik tersebut berada di sumbu Y")
elif (y == 0) :
    print("Titik tersebut berada di sumbu X")
