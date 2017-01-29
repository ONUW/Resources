import pygame, sys
from pygame.locals import *

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('One Night Ultimate Werewolf')

# 색깔
color = {"white":(255,255,255), "black":(0,0,0), "background_color":(255,244,78)}

# 폰트
testfont = pygame.font.Font("resources/fonts/NIXGONFONTS M 2.0.ttf", 20)

# 사진

# 음악

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color["background_color"])

    # 내 카드
    pygame.draw.rect(screen, color["white"], (50, 60, 200, 300)) # 나중에 이미지로 바꾸어야 됨
    # 내 카드 글씨
    mycardtext = testfont.render("내 카드", True, color["black"])
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