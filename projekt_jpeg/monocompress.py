import numpy as np
from matplotlib import pyplot as plt
import cv2


# podgląd obrazu
def preview(img):
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.show()


# macierz kwantyzacji o współczynniku 10 - można użyć dowolnej innej, w zależności od pożądanego stopnia kompresji
Q10 = np.array([[80, 60, 50, 80, 120, 200, 255, 255],
                [55, 60, 70, 95, 130, 255, 255, 255],
                [70, 65, 80, 120, 200, 255, 255, 255],
                [70, 85, 110, 145, 255, 255, 255, 255],
                [90, 110, 185, 255, 255, 255, 255, 255],
                [120, 175, 255, 255, 255, 255, 255, 255],
                [245, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255]])

# wczytanie kolorowego obrazu do skompresowania
img = cv2.imread("test3.png", 0)
preview(img)

# pobranie wymiarów obrazu
height = len(img)
width = len(img[0])

# funkcja kompresująca
def dctransformer(channel):
    # w algorytmie JPEG dzieli się obraz na bloki 8x8 pikseli i dla przyspieszenia obliczeń odejmuje się wartość średnią z [0-255], czyli 128
    divider = []
    tempJ = 0
    for i in range(8, height + 1, 8):
        tempI = 0
        for j in range(8, width + 1, 8):
            divider.append(channel[tempJ:i, tempI:j] - np.ones((8, 8)) * 128)
            tempI = j
        tempJ = i

    # konieczna jest zmiana typu na float, aby DCT mogło zadziałać
    imf = [np.float32(n) for n in divider]
    dct_result = []
    for part in imf:
        currDCT = cv2.dct(part)
        dct_result.append(currDCT)

    # podzielenie wyniku DCT przez odpowiednie współczynniki macierzy kwantyzacji - stratny etap kompresji
    for block in dct_result:
        for k in range(8):
            for l in range(8):
                block[k, l] = np.around(block[k, l] / Q10[k, l])

    # odwrotna DCT
    cleaner = []
    for n_block in dct_result:
        current = cv2.idct(n_block)
        cleaner.append(current)

    # przepisanie wyniku z listy na tablicę 2D
    x = 0
    xy = []
    for m in range(int(width / 8), len(cleaner) + 1, int(width / 8)):
        xy.append(np.hstack((cleaner[x:m])))
        x = m
    done = np.vstack((xy))
    return done


result=dctransformer(img)

preview(result)