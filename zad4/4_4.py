def rom_dec(n):
    dict = (("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000))
    result=0
    current = 0;
    prev = 0;
    for element in n:
      #  print('elem:'+str(element))
        for pos in dict:
           # print(pos)
            (rom, arb) = pos
            if element == rom:
                current=arb
                #print("prev"+str(prev))
                if prev >= current:
                    result = result + current
                else:
                    result = result + current - 2*prev
                prev = current
    return result

x = input("Liczba rzymska: ")
print(rom_dec(x))

#można również uwzględnić w słowniku IV, IX, XL, XC, CD, CM, a następnie liczyć wartość symbolu następnego i porównywać z bieżącym