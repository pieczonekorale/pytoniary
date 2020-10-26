n = int(input("Startowa liczba gwiazdek: "))

if n % 2 == 0:
    print("liczba parzysta!! ")

else:
    print('\n'.join((' ' * int((n - i) / 2) + '*' * i for i in range(n, 0, -2))))


