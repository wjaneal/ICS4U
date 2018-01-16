import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((50,25),0,32)
pygame.display.set_caption("Hello, world!")
background = pygame.image.load('blue.png').convert()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #接收到鼠标按下事件后更换背景
            background = pygame.image.load('yellow.png').convert()
