import pygame, sys

pygame.init()

def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption('Gra')
    icon = pygame.image.load(r'icon.jpg')
    pygame.display.set_icon(icon)

   # pygame.mixer.music.load(r'C:\Users\witol\Documents\UJ\PYTHON\GAME\music.mp3')
    #pygame.mixer.music.play(-1)

    size = width, height = 1400, 800
    screen = pygame.display.set_mode(size)

    speed = [0, 0]
    accel = [0.1, 0.1]
    prev = ""
    counter = 0

    image = pygame.image.load(r'bg.png')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height()) / 2
    )
    screen.blit(image, surf_center)
    ball = pygame.image.load(r'szop.png')
    screen.blit(ball, (width / 2, height / 2))
    ballrect = ball.get_rect(center=(width / 2, height / 2))

    pygame.display.flip()

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()


        if keys[pygame.K_UP]:
          #  ballrect.centery-=5
            counter = counter +1
            if (prev=="up"):
               # speed[0]=speed[0]+(accel[0]*counter)

                speed[1]=speed[1]+(accel[1]*counter)
                ballrect.centery -= int(speed[1])
            else:
                speed[0]=0
                speed[1]=0
                counter=0
            prev="up"

        elif keys[pygame.K_DOWN]:
            counter = counter + 1
            if (prev == "down"):
                # speed[0]=speed[0]+(accel[0]*counter)

                speed[1] = speed[1] + (accel[1] * counter)
                ballrect.centery += speed[1]
            else:
                counter = 0
                speed[0]=0
                speed[1]=0
            prev="down"

        elif keys[pygame.K_LEFT]:
            counter = counter + 1
            if (prev == "left"):
                speed[0]=speed[0]+(accel[0]*counter)

                ballrect.centerx -= int(speed[0])
            else:
                counter = 0
                speed[0]=0
                speed[1]=0
            prev="left"

        elif keys[pygame.K_RIGHT]:

            counter = counter + 1
            if (prev == "right"):
                speed[0]=speed[0]+(accel[0]*counter)

                ballrect.centerx += int(speed[0])
            else:
                counter = 0
                speed[0]=0
                speed[1]=0
            prev="right"

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()

    # pygame.time.delay(50)


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
