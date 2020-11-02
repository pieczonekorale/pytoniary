def char_frequency(str1):
    slownik = {}
    for i in str1:
        keys = slownik.keys()
        if i in keys:
            slownik[i] += 1
        else:
            slownik[i] = 1
    return slownik


tekst = "Przykladowy tekst. Milego dnia i smacznej kawusi."
print(tekst)

for char in '-.,\n':
    tekst=tekst.replace(char,' ')
    tekst = tekst.lower()

word_list = tekst.split()
size = len(word_list)
print("Liczba slow w tekscie: "+str(size))

napis = ''
for i in word_list:
    napis = napis+i

list2 = list(napis)

print("liczba liter w tekscie: " + str(len(list2)))
print("liczba wystapien poszczegolnych liter: "+'\n'+str(char_frequency(napis)))

