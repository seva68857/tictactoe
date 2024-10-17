import pygame

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
pos = []
current_player = 1
winner = 0
game_over = False
line_width = 6
game_state = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
font = pygame.font.SysFont(None, 40)
again_rect = pygame.Rect(SCREEN_WIDTH//2 - 80, SCREEN_HEIGHT//2 + 53, 160, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TiaTacToe')

def draw_grid():
    bg = (255, 200, 255)
    grid = (0, 0, 0)
    screen.fill(bg)
    for i in range(1, 3):
        pygame.draw.line(screen, grid, (0, i*(SCREEN_HEIGHT//3)), (SCREEN_WIDTH, i*(SCREEN_HEIGHT//3)), line_width)
        pygame.draw.line(screen, grid, (i*(SCREEN_WIDTH//3), 0), (i*(SCREEN_WIDTH//3), SCREEN_HEIGHT), line_width)

def draw_markers():
    x_pos = 0
    for x in game_state:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, (0, 255, 0), (x_pos*SCREEN_WIDTH//3 + 15, y_pos*SCREEN_HEIGHT//3 + 15), (x_pos*SCREEN_WIDTH//3 + 85, y_pos*SCREEN_HEIGHT//3 + 85), line_width)
                pygame.draw.line(screen, (0, 255, 0), (x_pos*SCREEN_WIDTH//3 + 15, y_pos*SCREEN_HEIGHT//3 + 85), (x_pos*SCREEN_WIDTH//3 + 85, y_pos*SCREEN_HEIGHT//3 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, (255, 0, 0), (x_pos*SCREEN_WIDTH//3 + 50, y_pos*SCREEN_HEIGHT//3 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in game_state:
        if sum(x) == 3: #check coloumns
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if game_state[0][y_pos] + game_state[1][y_pos] + game_state[2][y_pos] == 3: #check rows
            winner = 1
            game_over = True
        if game_state[0][y_pos] + game_state[1][y_pos] + game_state[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    #check cross
    if game_state[0][0] + game_state[1][1] + game_state[2][2] == 3 or game_state[0][2] + game_state[1][1] + game_state[2][0] == 3:
            winner = 1
            game_over = True
    if game_state[0][0] + game_state[1][1] + game_state[2][2] == -3 or game_state[0][2] + game_state[1][1] + game_state[2][0] == -3:
            winner = 2
            game_over = True
    
    #check draw
    if not game_over and (0 not in game_state[0]) and (0 not in game_state[1]) and (0 not in game_state[2]):
        game_over = True
        winner = 3

def draw_winner(winner):
    win_text = f'Player {winner} wins!' if winner != 3 else 'Draw!'
    win_img = font.render(win_text, True, (255, 100, 255))
    pygame.draw.rect(screen, (150, 50, 150), (35, 117, 230, 65))
    screen.blit(win_img, (SCREEN_WIDTH//2 - win_img.get_width()//2, SCREEN_HEIGHT//2 - win_img.get_height()//2))

    again_text = 'Play again'
    again_img = font.render(again_text, True, (255, 100, 255))
    pygame.draw.rect(screen, (150, 50, 150), again_rect)
    screen.blit(again_img, (SCREEN_WIDTH//2 - again_img.get_width()//2, SCREEN_HEIGHT//2 - again_img.get_height()//2 + 80))

run = True
while run:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #print(pos)
                mouse_x = pos[0]
                mouse_y = pos[1]
                if game_state[mouse_x // (SCREEN_WIDTH // 3)][mouse_y // (SCREEN_HEIGHT // 3)] == 0:
                    game_state[mouse_x // (SCREEN_WIDTH // 3)][mouse_y // (SCREEN_HEIGHT // 3)] = current_player
                    current_player *= -1
                    check_winner()

    if game_over:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                current_player = 1
                winner = 0
                game_over = False
                pos = []
                game_state = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]

    pygame.display.update()


pygame.quit()