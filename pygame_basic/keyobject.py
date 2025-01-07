import pygame


# 파이게임 초기화
pygame.init()

# 창 크기 설정 
background = pygame.display.set_mode((480, 360))
# 게임 창 이름 설정
pygame.display.set_caption('실행')

# 이동하는 오브젝트 만들기
# 초기 좌표 설정
x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2

# 이동좌표
to_x = 0
to_y = 0

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                to_y = -1
            elif event.key == pygame.K_a:
                to_x = -1
            elif event.key == pygame.K_s:
                to_y = 1
            elif event.key == pygame.K_d:
                to_x = 1

    # 좌표 변경
    x_pos += to_x
    y_pos += to_y

    # 배경색상
    background.fill((0,0,0))
    # 오브젝트 그리기
    pygame.draw.circle(background, (255,255,255), (x_pos,y_pos), 5)
    # 변동사항 반영
    pygame.display.update()

pygame.quit()