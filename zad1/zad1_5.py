x = [1, 2, 3, 5666, 3, 4, 6, 3, 4, 6]
y = [2, 4, 8, 19, 5666, 3, 3]

print("Sekwencja 1: ", x)
print("Sekwencja 2: ", y)

set_x = set(x)
set_y = set(y)

print("Wszystkie elementy bez powtórzeń:",list(set_x.union(set_y)))
print("Czesc wspolna zbiorow: ",list(set_x.intersection(set_y)))
