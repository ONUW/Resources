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
    pygame.draw.rect(screen, color["white"], (50, 60, 200, 300))

    # 글씨 1
    mycardtext = testfont.render("내 카드", True, color["black"])
    mycardtextobj = mycardtext.get_rect()
    mycardtextobj.center = (150, 30)
    screen.blit(mycardtext, mycardtextobj)
    pygame.display.flip()

