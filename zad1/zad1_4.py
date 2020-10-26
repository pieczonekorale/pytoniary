x = int(input("szerokosc: "))
y = int(input("wysokosc: "))


print("+" + (" -"*3+" +")*x)
i = y
while i != 0:
    print(("|" + " "*7)*x + "|")
    print("+" + (" -" * 3 + " +") * x)
    i = i-1

