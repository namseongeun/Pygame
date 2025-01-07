import pygame


# 파이게임 초기화
pygame.init()

# 창 크기 설정 
background = pygame.display.set_mode((480, 360))

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()