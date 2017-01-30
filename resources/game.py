import pygame, sys, socket, threading, time
from pygame.locals import *

pygame.init()
size = width, height = 1280,720
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
    pygame.draw.rect(screen, color["white"], (50, 60, 200, 300))

    # 글씨 1
    mycardtext = testfont.render("내 카드", True, color["black"])
    mycardtextobj = mycardtext.get_rect()
    mycardtextobj.center = (150, 30)
    screen.blit(mycardtext, mycardtextobj)

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
            pyame.quit()
            sys.exit()

