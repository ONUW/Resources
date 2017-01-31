import pygame, sys, socket, threading, time, random
from pygame.locals import *

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

sakistage = 0
stage = 1
numberofplayer = 5

pygame.display.set_caption('One Night Ultimate Werewolf')

# 색깔
color = { "white":(255,255,255), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "magenta":(255,0,255), "orange":(255,127,0),"pink":(255,192,203),
        "background_color":(255,244,78), "brown":(150,75,0), "cyan":(0,255,255), "indigo":(75,0,130), "purple":(128,0,128), "violet":(143,0,255), "gray":(128,128,128) }

# 폰트
mycardfont = pygame.font.Font("./fonts/NIXGONFONTS M 2.0.ttf", 20)
mycardfontbig = pygame.font.Font("./fonts/NIXGONFONTS M 2.0.ttf", 40)

# 사진
doppelganger = pygame.image.load("./images/doppelganger.png")
drunk = pygame.image.load("./images/drunk.png")
hunter = pygame.image.load("./images/hunter.png")
insomniac = pygame.image.load("./images/insomniac.png")
mason = pygame.image.load("./images/mason.png")
minion = pygame.image.load("./images/minion.png")
robber = pygame.image.load("./images/robber.png")
seer = pygame.image.load("./images/seer.png")
tanner = pygame.image.load("./images/tanner.png")
troublemaker = pygame.image.load("./images/troublemaker.png")
villager = pygame.image.load("./images/villager.png")
werewolf = pygame.image.load("./images/werewolf.png")

# 음악


# 캐릭터 배열
character = [doppelganger, drunk, hunter, insomniac, mason, minion, robber, seer, tanner, troublemaker, villager, werewolf]

while True:
    screen.fill(color["background_color"])
    if stage == 1:
        if sakistage != stage:
            sakistage = stage
        
        pygame.draw.rect(screen, color["purple"], [width//2+150,height//2-27,96,54])

        txt1 = mycardfontbig.render("몇 명?: "+str(numberofplayer)+" 명", True, color["black"])
        txtobj1 = txt1.get_rect()
        txtobj1.center = (width//2,height//2)
        screen.blit(txt1,txtobj1)

        txt2 = mycardfontbig.render("확 인",True,color["white"])
        txtobj2 = txt2.get_rect()
        txtobj2.center = (width//2+198,height//2)
        screen.blit(txt2,txtobj2)

        pygame.draw.polygon(screen, color["purple"], [ [width//2,height//2-60], [width//2-30,height//2-30], [width//2+30,height//2-30] ])
        pygame.draw.polygon(screen, color["purple"], [ [width//2,height//2+60], [width//2-30,height//2+30], [width//2+30,height//2+30] ])

    elif stage == 2:
        if sakistage != stage:
            sakistage = stage
        # 내 카드
        # pygame.draw.rect(screen, color["white"], (50, 60, 200, 300)) # 나중에 이미지로 바꾸어야 됨
        screen.blit(character[random.randrange(0,12)], (50, 60))
        # 내 카드 글씨
        mycardtext = mycardfont.render("내 카드", True, color["black"])
        mycardtextobj = mycardtext.get_rect()
        mycardtextobj.center = (150, 30)
        screen.blit(mycardtext, mycardtextobj)

        # 채팅창
        pygame.draw.rect(screen, color["white"], (50, 420, 200, 250))
    
        # 설명판
        pygame.draw.rect(screen, color["white"], (335, 420, 630, 250))

        # 순서표
        pygame.draw.rect(screen, color["white"], (1040, 420, 200, 250))

        # 카드 3장 # 나중에 이미지로 바꿔야 됨
        for i in range(3):
            pygame.draw.rect(screen, color["white"], (50+200+75+90*i, 60+105, 60, 90))

        # 플레이어 카드
        for i in range(5):
            for j in range(2):
                pygame.draw.rect(screen, color["white"], (50+200+390+120*i, 60+5+170*j, 80, 120))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if stage == 1:
                if abs(pos[0]-width//2) <= 30 and abs(pos[1]-height//2+30) <= 30:
                    if numberofplayer < 10:
                        numberofplayer += 1
                if abs(pos[0]-width//2) <= 30 and abs(pos[1]-height//2-30) <= 30:
                    if numberofplayer > 3:
                        numberofplayer -= 1
                if abs(pos[0]-width//2-198) <= 48 and abs(pos[1]-height//2) <= 27:
                    stage = 2
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == KEYDOWN:
            pass
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
