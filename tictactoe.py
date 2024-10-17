import pygame

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
pos = []
current_player = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TiaTacToe')

def draw_grid():
    line_width = 6
    bg = (255, 200, 255)
    grid = (0, 0, 0)
    screen.fill(bg)
    for i in range(1, 3):
        pygame.draw.line(screen, grid, (0, i*(SCREEN_HEIGHT//3)), (SCREEN_WIDTH, i*(SCREEN_HEIGHT//3)), line_width)
        pygame.draw.line(screen, grid, (i*(SCREEN_WIDTH//3), 0), (i*(SCREEN_WIDTH//3), SCREEN_HEIGHT), line_width)

run = True
while run:

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    pygame.display.update()


pygame.quit()