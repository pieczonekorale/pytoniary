tramwaje = {1 : ["p1", "p2", "p3"], 2 : ["p3", "p4"], 3 : ["p2", "p5", "p6"], 4 : ["p6", "p7"], 5: ["p7", "p8", "p9", "p10"]}
result = {}
#stworzenie listy przystankow
temp = list(tramwaje.values())
przystanki = []
for l in temp:
    for i in l:
        przystanki.append(i)
przystanki = list(dict.fromkeys(przystanki))
print("przystanki: ", przystanki)

#stworzenie listy sasiedztwa
adj = dict.fromkeys(przystanki)
for x in adj:
    adj[x] = []

for stop_list in temp:

    for num, sp_stop in enumerate(stop_list, start=0):
        if num+1<len(stop_list):
            adj[sp_stop].append(stop_list[num+1])
            adj[stop_list[num+1]].append(sp_stop)

#przechowywanie poprzednikow w celu odzyskania sciezki powrotnej
prev = dict.fromkeys(przystanki)

#wczytanie poczatku i konca trasy
print("algorytm Dijkstry")
poczatek = input("Przystanek poczatkowy: ")
koniec = input("Przystanek koncowy: ")


def minV(dist, visited):
    min = 8181
    for v in przystanki:

        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_stop = v

    return min_stop

def dijkstra(source):

    #slownik na przechowywanie zapamietywan przegladania
    visited = dict.fromkeys(przystanki)
    for j in visited:
        visited[j] = False

    #slownik na przechowywanie odleglosci
    dist = dict.fromkeys(przystanki)
    for i in dist:
        dist[i]=8181

    #odleglosc zadanego punktu startowego
    dist[source]=0
    route = []
    for i in przystanki:
        u = minV(dist, visited)
        visited[u] = True

        if u == koniec:
            if prev[u]:
                while u:
                    route.append(u)
                    u=prev[u]
            route.reverse()
            return route

        else:
            for v in przystanki:
                templ=adj[u]
                if visited[v] == False and dist[v] > dist[u] + 1 and v in templ:
                    dist[v] = dist[u] + 1
                    prev[v]=u

trasa = dijkstra(poczatek)
print("trasa przejazdu: ", trasa)

def tram_search(route, poczatek, final_stop):
    done = False
    trasa=route
    zero_stop=poczatek
    prev_stop = zero_stop
    while not done:
        delet = []
        for tram0 in tramwaje:
            if zero_stop in tramwaje[tram0] and final_stop in tramwaje[tram0]:
                result[tram0] = trasa
                done = True
        if not done:
            delet = []
            counter = {}
            new_route=[]
            for current_tram in tramwaje:
                if zero_stop in tramwaje[current_tram]:
                    counter[current_tram]=0
                    #szukanie tramwaju, ktory zawiera na pewno 1 przystanek i najwiecej kolejnych
                    for elem in trasa:
                        if elem in tramwaje[current_tram]:
                            counter[current_tram]+=1
            best_tram = max(counter, key=counter.get)
            result[best_tram]=[]
            new_route = trasa
            for i in range (counter[best_tram]-1):
                result[best_tram].append(new_route.pop(0))
            trasa=new_route
            zero_stop=trasa[0]
            result[best_tram].append(zero_stop)



tram_search(trasa,poczatek,koniec)

print(result)
