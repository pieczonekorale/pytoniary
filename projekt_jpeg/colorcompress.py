import numpy as np
from matplotlib import pyplot as plt
import cv2

#podgląd obrazu
def preview(img):
    plt.figure(figsize=(10,10))
    plt.axis("off")
    plt.imshow(img)
    plt.show()

#macierz kwantyzacji o współczynniku 10 - można użyć dowolnej innej, w zależności od pożądanego stopnia kompresji
Q10 = np.array([[80,60,50,80,120,200,255,255],
                [55,60,70,95,130,255,255,255],
                [70,65,80,120,200,255,255,255],
                [70,85,110,145,255,255,255,255],
                [90,110,185,255,255,255,255,255],
                [120,175,255,255,255,255,255,255],
                [245,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255]])

#wczytanie kolorowego obrazu do skompresowania
img = cv2.imread("imgtest.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
preview(img)

#pobranie wymiarów obrazu
height  = len(img) 
width = len(img[0]) 

#deklaracja tablic na każdy kanał koloru
RED = np.ones((width, height), np.int16)
GREEN = np.ones((width, height), np.int16)
BLUE = np.ones((width, height), np.int16)

#przepisanie wartości kolorów z pobranego obrazu do odpowiednich tablic
for i in range(0, height):
    for j in range(0, width):

        RED[i, j] = img[i,j,0]
        GREEN[i, j] = img[i, j, 1]
        BLUE[i, j] = img[i, j, 2]


#funkcja kompresująca
def dctransformer(channel):
    #w algorytmie JPEG dzieli się obraz na bloki 8x8 pikseli i dla przyspieszenia obliczeń odejmuje się wartość średnią z [0-255], czyli 128
    divider = []
    tempJ = 0 
    for i in range(8, height + 1, 8):
        tempI = 0 
        for j in range(8, width + 1, 8):
            divider.append(channel[tempJ:i, tempI:j] - np.ones((8, 8)) * 128)  
            tempI = j
        tempJ = i

    #konieczna jest zmiana typu na float, aby DCT mogło zadziałać
    float_img = [np.float32(n) for n in divider]
    dct_result = []
    for block_dv in float_img:
        current = cv2.dct(block_dv)
        dct_result.append(current)

    #podzielenie wyniku DCT przez odpowiednie współczynniki macierzy kwantyzacji - stratny etap kompresji
    for block in dct_result:
        for k in range(8):
            for l in range(8):
                block[k, l] = np.around(block[k, l] / Q10[k, l])


    #odwrotna DCT
    cleaner = []
    for n_block in dct_result:
        current = cv2.idct(n_block)
        cleaner.append(current)
        
    #przepisanie wyniku z listy na tablicę 2D
    x = 0
    xy = []
    for m in range(int(width / 8), len(cleaner) + 1, int(width / 8)):
        xy.append(np.hstack((cleaner[x:m])))
        x = m
    done = np.vstack((xy))
    return done


#przeprowadzenie kompresji na każdym z kanałów
lumin=dctransformer(RED)
blueval=dctransformer(GREEN)
redval=dctransformer(BLUE)

#zebranie oddzielnych tablic w wynikowy obraz
result = np.ones((width, height, 3))
for i in range(0, height, 1):
    for j in range(0, width, 1):
        result[i,j,0]=lumin[i,j]
        result[i, j, 1] = blueval[i, j]
        result[i, j, 2] = redval[i, j]


preview(result)
