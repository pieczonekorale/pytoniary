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

    speed = [10, 0]
    accel = [2, 9.81]
    counter = 0
    scale = 60 #zmienna do zwalniania/przyspieszania, żeby lepiej się dało zaobserwować ruch
    local_speed=[speed[0], speed[1]]

    image = pygame.image.load(r'bg.png')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height())/2
    )
    screen.blit(image, surf_center)
    ball = pygame.image.load(r'szop.png')
    screen.blit(ball, (width / 2, height / 2))
    ball = pygame.transform.scale(ball, (ball.get_width() // 1,
                                         ball.get_height() // 1))

    screen.blit(ball, (width / 2, height / 2))
    ballrect = ball.get_rect(center=(width / 2, 0))

    pygame.display.flip()

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()

        if ballrect.bottom<=height:
            if speed[0]==0 and speed[1]==0:
                counter+=1
                ballrect.centery +=accel[1]*counter/scale
                print(ballrect.centery)

            if speed[0]>0 and speed[1]==0:
                counter=counter+1
                local_speed[1]=accel[1]*counter
                print(local_speed[0])
                print(local_speed[1])
                ballrect.centerx+=local_speed[0]*accel[0]
                ballrect.centery+=local_speed[1]
                print(ballrect.centerx)
                print(ballrect.centery)
                print("____")

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()

    # pygame.time.delay(50)


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()

