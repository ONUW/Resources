import pygame, sys, socket, threading, time, random
from pygame.locals import *

def main():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    sakiStage = 0
    stage = 1
    numberOfPlayer = 5
    whoPlayNow = 0

    pygame.display.set_caption('One Night Ultimate Werewolf')

    # 색깔
    Color = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
         "magenta": (255, 0, 255), "orange": (255, 127, 0), "pink": (255, 192, 203),
         "backgroundColor": (255, 244, 78), "brown": (150, 75, 0), "cyan": (0, 255, 255), "indigo": (75, 0, 130),
         "purple": (128, 0, 128), "violet": (143, 0, 255), "gray": (128, 128, 128)}

    # 폰트
    myCardFont = pygame.font.Font("NIXGONFONTS M 2.0.ttf", 20)
    myCardFontbig = pygame.font.Font("NIXGONFONTS M 2.0.ttf", 40)

    # 사진
    Doppelganger = pygame.image.load("doppelganger.png")
    Drunk = pygame.image.load("drunk.png")
    Hunter = pygame.image.load("hunter.png")
    Insomniac = pygame.image.load("insomniac.png")
    Mason = pygame.image.load("mason.png")
    Minion = pygame.image.load("minion.png")
    Robber = pygame.image.load("robber.png")
    Seer = pygame.image.load("seer.png")
    Tanner = pygame.image.load("tanner.png")
    Troublemaker = pygame.image.load("troublemaker.png")
    Villager = pygame.image.load("villager.png")
    Werewolf = pygame.image.load("werewolf.png")

    choose_Doppelganger = pygame.image.load("doppelganger80.png")
    choose_Drunk = pygame.image.load("drunk80.png")
    choose_Hunter = pygame.image.load("hunter80.png")
    choose_Insomniac = pygame.image.load("insomniac80.png")
    choose_Mason = pygame.image.load("mason80.png")
    choose_Minion = pygame.image.load("minion80.png")
    choose_Robber = pygame.image.load("robber80.png")
    choose_Seer = pygame.image.load("seer80.png")
    choose_Tanner = pygame.image.load("tanner80.png")
    choose_Troublemaker = pygame.image.load("troublemaker80.png")
    choose_Villager = pygame.image.load("villager80.png")
    choose_Werewolf = pygame.image.load("werewolf80.png")

    # 음악


    # 캐릭터 배열
    Character = [Villager, Werewolf, Seer, Robber, Troublemaker, Tanner, Drunk, Hunter, Mason, Insomniac, Minion, Doppelganger]
    myCharacter = random.randrange(0, len(Character))

    while True:
        screen.fill(Color["backgroundColor"])
        if stage == 1:
            if sakiStage != stage:
                sakiStage = stage

            pygame.draw.rect(screen, Color["purple"], [width // 2 + 100, height // 2 - 37, 96, 54])

            txt1 = myCardFontbig.render("몇 명?: " + str(numberOfPlayer) + " 명", True, Color["black"])
            txtObj1 = txt1.get_rect()
            txtObj1.center = (width // 2 - 50, height // 2 - 10)
            screen.blit(txt1, txtObj1)

            txt2 = myCardFontbig.render("확 인", True, Color["white"])
            txtObj2 = txt2.get_rect()
            txtObj2.center = (width // 2 + 148, height // 2 - 10)
            screen.blit(txt2, txtObj2)

            pygame.draw.polygon(screen, Color["purple"], [[width // 2 - 50, height // 2 - 70], [width // 2 - 80, height // 2 - 40], [width // 2 - 20, height // 2 - 40]])
            pygame.draw.polygon(screen, Color["purple"], [[width // 2 - 50, height // 2 + 50], [width // 2 - 80, height // 2 + 20], [width // 2 - 20, height // 2 + 20]])

        # 잠에서 깨어나는 순서로 넣을게 (One Night 앱 참조)
        elif stage == 2:
            if sakiStage != stage:
                sakiStage = stage
            for i in range(4):
                for j in range(4):
                    pygame.draw.rect(screen, Color["white"], (width // 2 - 200 + 90 * i, height // 2 - 270 + 130 * j, 80, 120))
                    tmp = i + 4*j + 1
                    img = 0
                    if tmp == 1:
                        img = choose_Doppelganger
                    elif tmp <= 3:
                        img = choose_Werewolf
                    elif tmp == 4:
                        img = choose_Minion
                    elif tmp <= 6:
                        img = choose_Mason
                    elif tmp == 7:
                        img = choose_Seer
                    elif tmp == 8:
                        img = choose_Robber
                    elif tmp == 9:
                        img = choose_Troublemaker
                    elif tmp == 10:
                        img = choose_Drunk
                    elif tmp == 11:
                        img = choose_Insomniac
                    elif tmp <= 14:
                        img = choose_Villager
                    elif tmp == 15:
                        img = choose_Hunter
                    elif tmp == 16:
                        img = choose_Tanner
                    screen.blit(img, (width // 2 - 200 + 90 * i, height // 2 - 270 + 130 * j))

        elif stage == 3:
            if sakiStage != stage:
                sakiStage = stage
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
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if stage == 1:
                    if abs(pos[0] - (width // 2 - 50)) <= 30 and abs(pos[1] - (height // 2 - 55)) <= 15:
                        if numberOfPlayer < 10:
                            numberOfPlayer += 1
                    if abs(pos[0] - (width // 2 - 50)) <= 30 and abs(pos[1] - (height // 2 + 35)) <= 15:
                        if numberOfPlayer > 3:
                            numberOfPlayer -= 1
                    if abs(pos[0] - (width // 2 + 148)) <= 48 and abs(pos[1] - (height // 2 - 10)) <= 27:
                        stage = 2
            if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
            if event.type == KEYDOWN:
                pass
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()
