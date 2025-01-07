import pygame


# 파이게임 초기화
pygame.init()

# 창 크기 설정 
background = pygame.display.set_mode((480, 360))

# 파이게임 실행 여부 flag
play = True

while play:
    # 파이게임 실행 중 받는 모든 이벤트에 대하여...
    for event in pygame.event.get():
        # 종료 이벤트
        if event.type == pygame.QUIT:
            play = False

        # 키보드 입력 이벤트
        if event.type == pygame.KEYDOWN:
            print(event.key)

pygame.quit()