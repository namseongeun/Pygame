import pygame


# 파이게임 초기화
pygame.init()

# 창 크기 설정 
background = pygame.display.set_mode((480, 360))
# 게임 창 이름 설정
pygame.display.set_caption('실행')
# 시간
clock = pygame.time.Clock()
# 커서설정
pygame.mouse.set_cursor(pygame.cursors.broken_x)

# 이동하는 오브젝트 만들기
# 초기 좌표 설정
x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2

# 이동좌표
to_x = 0
to_y = 0

play = True

while play:
    # 1초에 몇 번 while문 실행하는지 설정
    deltaTime = pygame.time.Clock().tick(300)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        # 키 입력
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                to_y = -1
            elif event.key == pygame.K_a:
                to_x = -1
            elif event.key == pygame.K_s:
                to_y = 1
            elif event.key == pygame.K_d:
                to_x = 1

        # 키 입력 해제
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                to_y = 0
            elif event.key == pygame.K_a:
                to_x = 0
            elif event.key == pygame.K_s:
                to_y = 0
            elif event.key == pygame.K_d:
                to_x = 0        

        # 마우스 모션
        if event.type == pygame.MOUSEMOTION:
            # 마우스 이동에 따른 오브젝트 좌표이동
            x_pos, y_pos = pygame.mouse.get_pos()
            pygame.draw.circle(background, (255,255,255), (x_pos,y_pos),5)

        # 마우스 클릭
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 1: 왼쪽, 2: 휠, 3: 오른쪽, 4: 휠업, 5: 휠다운
            
            # 왼쪽 클릭하면 배경을 검정으로 채우기
            if event.button == 1:
                background.fill((0,0,0))

        # 마우스 클릭해제
        if event.type == pygame.MOUSEBUTTONUP:
            pass

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