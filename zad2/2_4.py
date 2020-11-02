x = int(input("x= "))
y = int(input("y= "))
z = int(input("z= "))
n = int(input("n= "))

big_list=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+k+j != n:
                list=[]
                list.append(i)
                list.append(j)
                list.append(k)
                print(list)
                big_list.append(list)
print(big_list)
