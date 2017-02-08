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
Color = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
         "magenta": (255, 0, 255), "orange": (255, 127, 0), "pink": (255, 192, 203),
         "backgroundColor": (255, 244, 78), "brown": (150, 75, 0), "cyan": (0, 255, 255), "indigo": (75, 0, 130),
         "purple": (128, 0, 128), "violet": (143, 0, 255), "gray": (128, 128, 128)}

# 폰트
myCardFont = pygame.font.Font("./fonts/NIXGONFONTS M 2.0.ttf", 20)
myCardFontbig = pygame.font.Font("./fonts/NIXGONFONTS M 2.0.ttf", 40)

# 사진
Doppelganger = pygame.image.load("./images/doppelganger.png")
Drunk = pygame.image.load("./images/drunk.png")
Hunter = pygame.image.load("./images/hunter.png")
Insomniac = pygame.image.load("./images/insomniac.png")
Mason = pygame.image.load("./images/mason.png")
Minion = pygame.image.load("./images/minion.png")
Robber = pygame.image.load("./images/robber.png")
Seer = pygame.image.load("./images/seer.png")
Tanner = pygame.image.load("./images/tanner.png")
Troublemaker = pygame.image.load("./images/troublemaker.png")
Villager = pygame.image.load("./images/villager.png")
Werewolf = pygame.image.load("./images/werewolf.png")

# 음악


# 캐릭터 배열
Character = [Doppelganger, Drunk, Hunter, Insomniac, Mason, Minion, Robber, Seer, Tanner, Troublemaker, Villager, Werewolf]
myCharacter = random.randrange(0, 12)

while True:
    screen.fill(Color["backgroundColor"])
    if stage == 1:
        if sakistage != stage:
            sakistage = stage

        pygame.draw.rect(screen, Color["purple"], [width // 2 + 150, height // 2 - 27, 96, 54])

        txt1 = myCardFontbig.render("몇 명?: " + str(numberofplayer) + " 명", True, Color["black"])
        txtObj1 = txt1.get_rect()
        txtObj1.center = (width // 2, height // 2)
        screen.blit(txt1, txtObj1)

        txt2 = myCardFontbig.render("확 인", True, Color["white"])
        txtObj2 = txt2.get_rect()
        txtObj2.center = (width // 2 + 198, height // 2)
        screen.blit(txt2, txtObj2)

        pygame.draw.polygon(screen, Color["purple"], [[width // 2, height // 2 - 60], [width // 2 - 30, height // 2 - 30], [width // 2 + 30, height // 2 - 30]])
        pygame.draw.polygon(screen, Color["purple"], [[width // 2, height // 2 + 60], [width // 2 - 30, height // 2 + 30], [width // 2 + 30, height // 2 + 30]])

    elif stage == 2:
        if sakistage != stage:
            sakistage = stage
        # 내 카드
        # pygame.draw.rect(screen, Color["white"], (50, 60, 200, 300)) # 나중에 이미지로 바꾸어야 됨
        screen.blit(Character[myCharacter], (50, 60))
        # 내 카드 글씨
        myCardText = myCardFont.render("내 카드", True, Color["black"])
        myCardTextObj = myCardText.get_rect()
        myCardTextObj.center = (150, 30)
        screen.blit(myCardText, myCardTextObj)

        # 채팅창
        pygame.draw.rect(screen, Color["white"], (50, 420, 200, 250))

        # 설명판
        pygame.draw.rect(screen, Color["white"], (335, 420, 630, 250))

        # 순서표
        pygame.draw.rect(screen, Color["white"], (1040, 420, 200, 250))

        # 카드 3장 # 나중에 이미지로 바꿔야 됨
        for i in range(3):
            pygame.draw.rect(screen, Color["white"], (50 + 200 + 75 + 90 * i, 60 + 105, 60, 90))

        # 플레이어 카드
        for i in range(5):
            for j in range(2):
                pygame.draw.rect(screen, Color["white"], (50 + 200 + 390 + 120 * i, 60 + 5 + 170 * j, 80, 120))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if stage == 1:
                if abs(pos[0] - width // 2) <= 30 and abs(pos[1] - height // 2 + 30) <= 30:
                    if numberofplayer < 10:
                        numberofplayer += 1
                if abs(pos[0] - width // 2) <= 30 and abs(pos[1] - height // 2 - 30) <= 30:
                    if numberofplayer > 3:
                        numberofplayer -= 1
                if abs(pos[0] - width // 2 - 198) <= 48 and abs(pos[1] - height // 2) <= 27:
                    stage = 2
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == KEYDOWN:
            pass
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
