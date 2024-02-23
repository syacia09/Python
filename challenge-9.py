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