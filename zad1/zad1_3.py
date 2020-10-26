n = int(input("dlugosc linijki: "))

ruler = "|" + (" ."*3+" |")*n
if n <= 9:
    numbers = "0" + "".join(" "*7 + str(i) for i in range(1,n+1,1))

elif n<=99:
    numbers = "0" + "".join(" "*7 + str(i) for i in range(1,10,1)) +"".join(" "*6 +str(j) for j in range(10, n+1, 1))

else:
    numbers = "0" + "".join(" " * 7 + str(i) for i in range(1, 10, 1)) + "".join(
        " " * 6 + str(j) for j in range(10, 100, 1)) + "".join(" "*5 + str(k) for k in range (100,n+1,1))

print(ruler)
print(numbers)
