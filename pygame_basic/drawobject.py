import pygame


pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('play')

# 화면 중앙 위치 변수화하기
x= background.get_size()[0]//2
y= background.get_size()[1]//2

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    background.fill((255, 255, 255))

    # 선그리기
    # pygame.draw.line(화면, 색, 시작위치, 끝위치, 선굴기=기본1)
    pygame.draw.line(background, (0,0,0), (x,0), (x, y*2))
    pygame.draw.line(background, (0,0,0), (0,y), (x*2, y))

    # 반복문을 사용해서 격자 그리기
    for i in range(0, 480, 30): 
        pygame.draw.line(background, (0,0,0), (i,0), (i,360))
    for j in range(0, 360, 30):
        pygame.draw.line(background, (0,0,0), (0,j), (480,j))

    # 원 그리기
    # pygame.draw.circle(화면, 색, 중심좌표, 반지름 , 선굵기)
    # pygame.draw.circle(background, (0,255,0), (x,y), 50)
    pygame.draw.circle(background, (0,255,0), (x,y), 50, 5)


    # 사각형 그리기
    # pygame.draw.rect(화면, 색, 위치와 크기(좌상단 좌표와 가로세로 길이), 선굵기)
    # pygame.draw.rect(background, (0,0,255), (x-50,y-25,100,50))
    pygame.draw.rect(background, (0,0,255), (x-50,y-25,100,50), 5)

    # 타원 그리기
    # pygame.draw.ellipse()

    # 다각형 그리기
    # pygame.draw.polygon()


    pygame.display.update()

pygame.quit()