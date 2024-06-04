import pygame, sys
#tạo hàm cho trò chơi
def draw_floor():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))
def create_pipe():
    new_pipe = pipe_surface.get_rect( midtop = (216,384))
    return new_pipe
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -= 5
        return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
#tạo biến cho trò chơi
gravity = 0.25
bird_movement = 0
# chèn back
bg = pygame.image.load('FileGame/FileGame/assets/background-night.png')
bg = pygame.transform.scale2x(bg)
# chèn sàn
floor = pygame.image.load('FileGame/FileGame/assets/floor.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0 
# tạo chim 
bird = pygame.image.load('FileGame/FileGame/assets/yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384))
#tạo ống
pipe_surface = pygame.image.load('FileGame/FileGame/assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
#tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -11
        if event.type == spawnpipe:
            pipe_list.append(create_pipe())

        
    screen.blit(bg,(0,0))
    #chim
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird,bird_rect)
    #ống
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    #sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos < -432:
        floor_x_pos=0
       
    screen.blit(floor,(floor_x_pos,600))
    pygame.display.update()
    clock.tick(120)