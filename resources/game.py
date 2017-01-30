import pygame, sys, socket, threading, time
from pygame.locals import *

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

pygame.display.set_caption('One Night Ultimate Werewolf')

# 색깔
color = { "white":(255,255,255), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "magenta":(255,0,255), "orange":(255,127,0),"pink":(255,192,203),
        "background_color":(255,244,78), "brown":(150,75,0), "cyan":(0,255,255), "indigo":(75,0,130), "purple":(128,0,128), "violet":(143,0,255), "gray":(128,128,128) }

# 폰트
testfont = pygame.font.Font("resources/fonts/NIXGONFONTS M 2.0.ttf", 20)

# 사진

# 음악

while True:
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

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pass
        if event.type == KEYDOWN:
            pass
        if event.type == QUIT:
            pygame.quit()
            sys.exit()