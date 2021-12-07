import pygame

TILESIZE = 32
BOARD_POS = (10, 10)

def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*8, TILESIZE*8))
    dark = False
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('black' if dark else 'white'), rect)
            dark = not dark
        dark = not dark
    return board_surf

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)
    return board

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILESIZE) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None

def main():
    screen = pygame.display.set_mode((640, 480))
    board = create_board()
    board_surf = create_board_surf()
    clock = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return

        piece, x, y = get_square_under_mouse(board)

        screen.fill(pygame.Color('grey'))
        screen.blit(board_surf, BOARD_POS)

        if x != None:
            rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()