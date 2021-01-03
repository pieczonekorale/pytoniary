import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

tramwaje={}
for elem in data['tramwaje']:
    tram_name = elem['name']
    tramwaje[tram_name]=[]
    t_przystanki=elem['tprzystanki']
    for row in t_przystanki:
        tramwaje[tram_name].append(row['name'])

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

#stworzenie slownika krawedzi na potrzeby alg bellmana-forda
edges = []
for i in adj:
    for elem in adj[i]:
        edges.append([i,elem])

#przechowywanie poprzednikow w celu odzyskania sciezki powrotnej
prev = dict.fromkeys(przystanki)
route = []

#wczytanie poczatku i konca trasy
print("algorytm Bellmana-Forda")
poczatek = input("Przystanek poczatkowy: ")
koniec = input("Przystanek koncowy: ")


def BellmanFord(source):

    dist = dict.fromkeys(przystanki)
    for i in dist:
        dist[i] = 8181
    dist[source] = 0

    for n in range(len(przystanki)-1):
        for edge in edges:
            if dist[edge[0]] != 8181 and dist[edge[0]] + 1 < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + 1
                prev[edge[1]]=edge[0]

    u = koniec
    if prev[u]:
        while u:
            route.append(u)
            u = prev[u]
    route.reverse()
    return route

trasa=BellmanFord(poczatek)
print("trasa przejazdu: ",trasa)

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

