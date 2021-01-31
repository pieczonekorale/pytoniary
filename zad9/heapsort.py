import sortgen


def heap_maker (data, n, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != root:
        data[root], data[largest] = data[largest], data[root]
        heap_maker(data, n, largest)



def heapsort(data, n):

    for i in range (int(n/2)-1, -1, -1):
        heap_maker(data, n, int(i))

    for i in range(n-1, -1, -1):
        data[0], data[i] = data[i], data[0]
        heap_maker(data, i, 0)


n=10
data = sortgen.gen_random(n)
print(data)
heapsort(data, n)
print(data)




'''
Heapsort, czyli sortowanie kopcowe, to algorytm sortowania bazującym na strukturze kopca.
Jest sortowaniem niestabilnym, jego złożoność czasowa to O(n log n). 
Algorytm korzysta z kopca binarnego - buduje kopiec na podstawie danych z otrzymanego zbioru wejściowego, 
w taki sposób, żeby relacja rodzic-dziecko, wynikająca z własności kopca, została zachowana. Własnością kopca jest to, iż korzeniem jest zawsze największy element.
Właściwe sortowanie polega na usuwaniu elementu z korzenia i przebudowaniu kopca, aby ponownie w korzeniu otrzymać najwyższą wartość. Powtarza się czynność do wyczerpania elementów.

'''