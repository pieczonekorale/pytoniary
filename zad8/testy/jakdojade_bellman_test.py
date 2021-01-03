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

#stworzenie slownika krawedzi na potrzeby alg bellmana-forda
edges = []
for i in adj:
    for elem in adj[i]:
        edges.append([i,elem])

#przechowywanie poprzednikow w celu odzyskania sciezki powrotnej
prev = dict.fromkeys(przystanki)

#wczytanie poczatku i konca trasy
print("algorytm Bellmana-Forda")
#poczatek = input("Przystanek poczatkowy: ")
#koniec = input("Przystanek koncowy: ")


def BellmanFord(source, destination):


    dist = dict.fromkeys(przystanki)
    route = []
    result = {}
    prev = dict.fromkeys(przystanki)

    for i in dist:
        dist[i] = 8181
    dist[source] = 0

    for n in range(len(przystanki)-1):
        for edge in edges:
            if dist[edge[0]] != 8181 and dist[edge[0]] + 1 < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + 1
                prev[edge[1]]=edge[0]

    u = destination
    if prev[u]:
        while u:
            route.append(u)
            u = prev[u]
    route.reverse()
    return route


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
        print(BellmanFord(poczatek,koniec))

elapsed_time = time.process_time() - t
print(elapsed_time)