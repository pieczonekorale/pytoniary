def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True;
            else:
                return False;
        else:
            return True
    else:
        return False


n = int(input("Ktory rok sprawdzic: "))
if n<1900 and n>100000:
    print("podaj rok z zakresu 1900-10000")

print(leap_year(n))