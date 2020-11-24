import pygame
from random import randint

pygame.init()

# kolory
BLUE = (0, 0, 255)
BIALY = (255, 255, 255)

bestscore=0
currentscore=0

class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 700:
           self.rect.x = 700



class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(4, 8), randint(-8, 8)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -1.2*self.velocity[0]
        self.velocity[1] = -1.2*self.velocity[1]



# definiujemy rozmiary i otwieramy nowe okno
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietkaA = Rakietka(BIALY, 100, 10)
rakietkaA.rect.x = 350
rakietkaA.rect.y = 590


pileczka = Pilka(BIALY,10,10)
pileczka.rect.x = randint(0,800)
pileczka.rect.y = 0

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie obu rakietek i piłeczki do listy
all_sprites_list.add(rakietkaA)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
scoreA = 0
game_over = False

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False


    if not game_over:
        # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rakietkaA.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            rakietkaA.moveRight(5)


        # aktualizacja listy duszków
        all_sprites_list.update()

        # sprawdzenie czy piłeczka nie uderza w którąś ścianę
        # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
        if pileczka.rect.x>=800:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.x<=0:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.y<0:
            pileczka.velocity[1] = -pileczka.velocity[1]

        # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
        if pygame.sprite.collide_mask(pileczka, rakietkaA):
            pileczka.bounce()
            scoreA+=1
            if(scoreA>bestscore):
                bestscore=scoreA

    #game over init
    if pileczka.rect.y>590 and not pygame.sprite.collide_mask(pileczka, rakietkaA):
        currentscore = scoreA
        game_over=True

        #restart gry
        if event.type == pygame.MOUSEBUTTONUP:
            pileczka.rect.x = randint(0, 800)
            pileczka.rect.y = 0
            scoreA = 0
            pileczka.velocity[0] = randint(4, 8)
            pileczka.velocity[1] = randint(-8, 8)
            game_over = False


    # RYSOWANIE
    screen.fill(BLUE)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 70)
    text = font.render(str(scoreA), 1, BIALY)
    screen.blit(text, (400,10))


    if game_over:

        font = pygame.font.Font(None, 70)
        text = font.render(str(bestscore) + "- najlepszy wynik", 1, BIALY)
        screen.blit(text, (100, 280))
        text = font.render(str(currentscore) + "- twoj wynik", 1, BIALY)
        screen.blit(text, (100, 350))
        font = pygame.font.Font(None, 20)
        text = font.render("wcisnij PRAWY PRZYCISK MYSZY aby zaczac", 1, BIALY)
        screen.blit(text, (5, 5))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()