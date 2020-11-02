x = int(input("liczba do zamiany= "))

liczba_binarna = bin(x)

print(liczba_binarna)


search = list(liczba_binarna)
del search[0]
del search[0]

str_num=""
print(search)
for i in search:
    str_num = str_num+i

print(str_num)

controller = str_num.split("1")
controller = list(filter(None, controller))
#print(controller)

if search[0]== '0':
    del controller[0]
if search[len(search)-1]== '0':
    del controller[len(controller)-1]
print(controller)

if controller:

    max_break=1
    print("liczba przerw: "+str(len(controller)))
    for i in controller:
        if len(i)>max_break:
            max_break=len(i)
    print("najdluzsza przerwa: "+str(max_break))


else:
    print("brak przerw")
