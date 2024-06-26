import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("music player")

musics = [r"C:\Users\abdia\PycharmProjects\pp2\lab7\hello.mp3", r"C:\Users\abdia\PycharmProjects\pp2\lab7\letali.mp3", r"C:\Users\abdia\PycharmProjects\pp2\lab7\coldplay.mp3"]

pygame.mixer.music.load(musics[0])
pygame.mixer.music.play()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

now = 0
def queue(music):
    global now
    if music == True:
        now += 1
        if now >= len(musics):
            now = 0
        pygame.mixer.music.load(musics[now])
        pygame.mixer.music.play()
    else:
        now -= 1
        if now < 0:
            now = len(musics) - 1
    pygame.mixer.music.load(musics[now])
    pygame.mixer.music.play()


run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == SONG_END:
            print('The Song Ended!')

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pygame.mixer.music.unpause()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            music =  True
            queue(music)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            music = False
            queue(music)

    screen.fill((225, 225, 225))
    font = pygame.font.Font(None, 50)
    text1 = font.render('1.Adele - Hello', True, (0, 0, 0))
    text2 = font.render('2.Ulukmanapo - Letali', True, (0, 0, 0))
    text3 = font.render('3.Coldplay - A sky full of stars', True, (0, 0, 0))
    text4 = font.render('          ^       ', True, (240, 0, 255))
    text5 = font.render('   <  ____  >', True, (240, 0, 255))
    screen.blit(text1, [70, 100])
    screen.blit(text2, [70, 140])
    screen.blit(text3, [70, 180])
    screen.blit(text4, [100, 220])
    screen.blit(text5, [100, 240])
    pygame.display.flip()

pygame.quit()