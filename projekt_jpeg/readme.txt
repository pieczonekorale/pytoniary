Uproszczony algorytm kompresji JPEG.
Osobno wersje do odczytu plików RGB i w skali szarości, a także pliki testowe.

Algorytm JPEG jest kompresją stratną.
Obraz wejściowy zostaje podzielony na mniejsze bloki, na których przeprowadzana jest dyskretna transformata kosinusowa (DCT).
Wyniki podlegają kwantyzacji, czyli dzieleniu przez jakieś odpowiednie wartości. Od doboru tych wartości zależy stopień kompresji i jakość wynikowego obrazu.
Potem wyniki są odczytywane w odpowiedniej kolejności.

Program dla plików w skali szarości jest znacznie prostszy - czytane są tylko pojedyncze wartości pikseli, które następnie są przetwarzane w funkcji kompresującej.
Wersja dla kolorowych obrazów wczytuje plik w postaci macierzy: szerokość x wysokość x 3 wartości kolorów
tutaj istotne było odseparowanie poszczególnych wartości kolorów i przetwarzanie ich osobno - stąd algorytm kompresji zostaje wywołany na każdej z tablic przechowującej kolory.
Wyniki są łączone z powrotem dopiero na końcu.

Program posiada jeszcze kilka mankamentów. Wersja RGB przetwarza tymczasowo tylko kwadratowe pliki, brakuje także przekształcenia składowych RGB na tzw. współrzędne Y, Cb, Cr (jednak ten krok nie jest formalnie obowiązkowy).
Do uruchomienia programu konieczne są biblioteki: numeryczna, opencv, matplotlib