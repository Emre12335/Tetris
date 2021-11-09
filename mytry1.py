# Taslak
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


def draw_main():
    a = pygame.surface.Surface((300, 600))
    a.fill("gray")
    a_r = a.get_rect(center=(400, 400))
    screen.blit(a, a_r)


def draw_horizontal_lines():
    x1 = 250
    x2 = 549
    y = 100
    while y < 700:
        pygame.draw.line(screen, "red", (x1, y), (x2, y))
        y += 600 / 21


def draw_vertical_lines():
    y1 = 100
    y2 = 699
    x = 250
    while x < 550:
        pygame.draw.line(screen, "red", (x, y1), (x, y2))
        x += 300 / 11


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_main()
    draw_vertical_lines()
    draw_horizontal_lines()
    pygame.display.update()
    clock.tick(60)
