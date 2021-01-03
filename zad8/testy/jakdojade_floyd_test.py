import json
import time
import random
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

tramwaje={}
for elem in data['tramwaje']:
    tram_name = elem['name']
    tramwaje[tram_name]=[]
    t_przystanki=elem['tprzystanki']
    for row in t_przystanki:
        tramwaje[tram_name].append(row['name'])


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

def floydWarshall(source, destination):
    poczatek=source
    koniec=destination
    next = {}
    route = []

    # lista krawedzi
    edges = []
    for i in adj:
        for elem in adj[i]:
            edges.append((i, elem))
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

test_set = []
for i in range(10):
    test_set.append(random.choice(przystanki))
print('SET TESTOWY:', test_set)

t = time.process_time()
for x in test_set:
    poczatek = x
    koniec = 'Urzędnicza'
    if poczatek != koniec:
        print("licze: ", poczatek, koniec)
        print(floydWarshall(poczatek,koniec))

elapsed_time = time.process_time() - t
print(elapsed_time)