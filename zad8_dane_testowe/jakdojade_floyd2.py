tramwaje = {1 : ["p1", "p2", "p3"], 2 : ["p3", "p4"], 3 : ["p2", "p5", "p6"], 4 : ["p6", "p7"], 5: ["p7", "p8", "p9", "p10"]}
result = {}
#stworzenie listy przystankow
temp = list(tramwaje.values())

przystanki = []
for l in temp:
    for i in l:
        przystanki.append(i)
przystanki = list(dict.fromkeys(przystanki))
print("przystanki: ",przystanki)

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
next = {}
route=[]

#lista krawedzi
edges = []
for i in adj:
    for elem in adj[i]:
        edges.append((i,elem))

#wczytanie poczatku i konca trasy
poczatek = input("Przystanek poczatkowy: ")
koniec = input("Przystanek koncowy: ")


def floydWarshall():

    size=len(przystanki)
    dist = {}
    for edge in edges:
        dist[edge]=2137

    for v1 in przystanki:
        for v2 in przystanki:
            dist[(v1,v2)]=2137
        dist[(v1,v1)]=0
        next[(v1,v1)]=v1
    for edge in edges:
        dist[edge]=1
        next[edge]=edge[1]

    for k in przystanki:
        for i in przystanki:
            for j in przystanki:
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
                    next[(i, j)] = next[(i, k)]


    print(dist[(poczatek, koniec)])
    path=[]
    u = poczatek
    v = koniec
    path.append(u)
    while u != v:
        u = next[(u,v)]
        path.append(u)
    print("sciezka: ",path)
    return path

trasa = floydWarshall()

def tram_search(route, poczatek, final_stop):
    done = False
    trasa=route
    zero_stop=poczatek
    prev_stop = zero_stop
    while not done:
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
