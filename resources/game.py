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

    chooseDoppelganger = pygame.image.load("./images/choose/doppelganger80.png")
    chooseDrunk = pygame.image.load("./images/choose/drunk80.png")
    chooseHunter = pygame.image.load("./images/choose/hunter80.png")
    chooseInsomniac = pygame.image.load("./images/choose/insomniac80.png")
    chooseMason = pygame.image.load("./images/choose/mason80.png")
    chooseMinion = pygame.image.load("./images/choose/minion80.png")
    chooseRobber = pygame.image.load("./images/choose/robber80.png")
    chooseSeer = pygame.image.load("./images/choose/seer80.png")
    chooseTanner = pygame.image.load("./images/choose/tanner80.png")
    chooseTroublemaker = pygame.image.load("./images/choose/troublemaker80.png")
    chooseVillager = pygame.image.load("./images/choose/villager80.png")
    chooseWerewolf = pygame.image.load("./images/choose/werewolf80.png")

    # 음악


    # 캐릭터 배열
    Character = [Villager, Werewolf, Seer, Robber, Troublemaker, Tanner, Drunk, Hunter, Mason, Insomniac, Minion, Doppelganger]
    chooseCharacter = [chooseVillager, chooseWerewolf, chooseSeer, chooseRobber, chooseTroublemaker, chooseTanner, chooseTanner, 
            chooseDrunk, chooseHunter, chooseMason, chooseInsomniac, chooseMinion, chooseDoppelganger]
    myCharacter = random.randrange(0, len(Character))

    while True:
        screen.fill(Color["backgroundColor"])
        if stage == 1:
            if sakiStage != stage:
                sakiStage = stage

            pygame.draw.rect(screen, Color["purple"], [width // 2 + 100, height // 2 - 37, 96, 54])

            txt1 = myCardFontbig.render("몇 명?: " + str(numberOfPlayer) + " 명", True, Color["black"])
            txtObj1 = txt1.get_rect()
            txtObj1.center = (width//2 - 50, height//2 - 10)
            screen.blit(txt1, txtObj1)

            txt2 = myCardFontbig.render("확 인", True, Color["white"])
            txtObj2 = txt2.get_rect()
            txtObj2.center = (width//2 + 148, height//2 - 10)
            screen.blit(txt2, txtObj2)

            pygame.draw.polygon(screen, Color["purple"], [[width//2 - 50, height//2 - 70], [width//2 - 80, height//2 - 40], [width//2 - 20, height//2 - 40]])
            pygame.draw.polygon(screen, Color["purple"], [[width//2 - 50, height//2 + 50], [width//2 - 80, height//2 + 20], [width//2 - 20, height//2 + 20]])

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
                        img = chooseDoppelganger
                    elif tmp <= 3:
                        img = chooseWerewolf
                    elif tmp == 4:
                        img = chooseMinion
                    elif tmp <= 6:
                        img = chooseMason
                    elif tmp == 7:
                        img = chooseSeer
                    elif tmp == 8:
                        img = chooseRobber
                    elif tmp == 9:
                        img = chooseTroublemaker
                    elif tmp == 10:
                        img = chooseDrunk
                    elif tmp == 11:
                        img = chooseInsomniac
                    elif tmp <= 14:
                        img = chooseVillager
                    elif tmp == 15:
                        img = chooseHunter
                    elif tmp == 16:
                        img = chooseTanner
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
