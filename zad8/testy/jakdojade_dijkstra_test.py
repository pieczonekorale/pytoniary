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

#wczytanie poczatku i konca trasy
print("algorytm Dijkstry")

def minV(dist, visited):
    min = 8181
    for v in przystanki:

        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_stop = v

    return min_stop

def dijkstra(source, destination):
    koniec = destination
    prev = dict.fromkeys(przystanki)

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


test_set = []
for i in range(100):
    test_set.append(random.choice(przystanki))
print('SET TESTOWY:', test_set)

t = time.process_time()
for x in test_set:
    poczatek = x
    koniec = 'Urzędnicza'
    if poczatek != koniec:
        print("licze: ", poczatek, koniec)
        print(dijkstra(poczatek,koniec))

elapsed_time = time.process_time() - t
print(elapsed_time)