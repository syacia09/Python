i = 0
count = 20
space = int (1/2 * count)
while True :
    if i == 20 :
        break
    elif i % 2 :
        print(" "*space, "+"*i)
        space -= 1
    i += 1

i = 17
count = 20
space = 1
while True :
    if i == 0 :
        break
    elif i % 2 :
        space += 1
        print(" "*space, "+"*i)
    i -= 1

i = 1
count = 20
space = 16
while True :
    if i == 10 :
        break
    else :
        print("+"*i, " "*space, "+"*i)
        space -= 2
    i += 1
print("+"*20)
print("+"*20)

i = 9
count = 20
space = 0
while True :
    if i == 0 :
        break
    else :
        print("+"*i, " "*space, "+"*i)
        space +=2
    i -= 1