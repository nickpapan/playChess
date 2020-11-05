
import pygame as p
import GameState

width = height = 512
dimensions = 8
square_size = height // dimensions
MAX_FPS = 15
images = {}




def load_images():

    peaces = ['bB', 'bK', 'bN', 'bP', 'bR', 'wB', 'wK', 'wP', 'wQ', 'wR']
    peac = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
    for peace in peac:
        images[peace] = p.transform.scale(p.image.load("images/" + peace + ".png"), (square_size, square_size))


def chess_b_gi():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameState.GameState()  # TODO ???????????????


    load_images()
    draw_game_state(screen, gs)
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board) # TODO ?????????




def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(dimensions):
        for c in range(dimensions):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*square_size, r*square_size, square_size, square_size ))

def draw_pieces( screen, board):
    for r in range(dimensions):
        for c in range(dimensions):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c*square_size, r*square_size, square_size, square_size))


chess_b_gi()
