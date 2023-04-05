import pygame
from pygame.locals import *
from random import randrange

pygame.init()

# SOM 
pygame.mixer.music.set_volume(0.3)
music_theme = pygame.mixer.music.load('music_theme.mp3')
pygame.mixer.music.play(-1)
eat_fruit = pygame.mixer.Sound('food.wav')
eat_fruit.set_volume(0.4)
game_over_sound = False
game_over_sound = pygame.mixer.Sound('game_over_sound.wav')
game_over_sound.set_volume(0.5)

# LINHAS
cell_size = 25
num_cells = 10

# TELA
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 48)


# VARIÁVEIS
bg_color = (34, 139, 34)
line_color = (144, 238, 144)
line_width = 2 
x = screen_width / 2
y = screen_height / 2
x_fruit = randrange(25, 775, 25) 
y_fruit = randrange(25, 575, 25)
speed = 10
x_control = speed
y_control = 0
points = 0
game_over = False

# DESENHAR LINHAS
def draw_grid():
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, line_color, (x, 0), (x, screen_height), line_width)

    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, line_color, (0, y), (screen_width, y), line_width)
        
body = []
initial_size = 1

# CORPO DA COBRA
def snake_body(body):
    for XeY in body:
        pygame.draw.rect(screen, (255, 255, 255), (XeY[0], XeY[1], 25, 25))
    
# RESTARTA O JOGO
def restart_game():
    global points, initial_size, x, y, body, head, x_fruit, y_fruit, game_over
    points = 0
    initial_size = 5
    x = screen_width / 2
    y = screen_height / 2
    body = []
    head = []
    x_fruit = randrange(25, 775, 25) 
    y_fruit = randrange(25, 575, 25)
    game_over = False
    
    
# EVENTOS DO JOGO
while True:
    clock.tick(30)
    screen.fill(bg_color)
    draw_grid()
    font = pygame.font.SysFont("arial.ttf", 40, bold = True)
    message = f'Points: {points}'
    text = font.render(message, True, (0,0,0))
    screen.blit(text,(660, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
                        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = - speed
                    y_control = 0
            if event.key == K_d:
                if x_control == - speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = - speed
            if event.key == K_s:
                if y_control == - speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed
            if event.key == K_LEFT:
                if x_control == speed:
                    pass
                else:
                    x_control = - speed
                    y_control = 0
            if event.key == K_RIGHT:
                if x_control == - speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_UP:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = - speed
            if event.key == K_DOWN:
                if y_control == - speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed
        
    x = x + x_control
    y = y + y_control
        
    
    snake = pygame.draw.rect(screen, (255, 255, 255), (x, y, 25, 25))
    fruit = pygame.draw.rect(screen, (255, 0, 0), (x_fruit, y_fruit, 25, 25))
        
    head = []
    head.append(x)
    head.append(y)
    
    body.append(head)
    
# GAME OVER
    if body.count(head) > 1 or  x < 0 or x + cell_size > screen_width or y < 0 or y + cell_size > screen_height:
        font = pygame.font.Font("8bit_in.ttf", 30)
        message = "Pressione Espaço para Jogar Novamente"
        text = font.render(message,True,(255,255,255))
        game_over_bg = pygame.image.load("game_over.png")
        game_over = True
        while game_over:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                         restart_game()
            screen.blit(text,(140, 250))
            screen.blit(game_over_bg, (270, 100))
            pygame.display.update()
    
    if len(body) > initial_size:
        del body[0]
        
    snake_body(body)
    
# CRESCENDO 
    if snake.colliderect(fruit):
        eat_fruit.play()
        x_fruit = randrange(25, 750, 25) 
        y_fruit = randrange(25, 550, 25)
        initial_size = initial_size + 3
        points = points + 1
        
    pygame.display.flip()
