import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
screen.fill("#301D50")


class block(pygame.sprite.Sprite):
    def __init__(self, color="red", index_x=0, index_y=0):
        super().__init__()
        self.image = pygame.surface.Surface((300 / 10, 600 / 20))
        self.image.fill(color)
        self.index_list_x = index_x
        self.index_list_y = index_y
        self.x = 25 + (self.index_list_x + 8) * 30
        self.y = 25 + (self.index_list_y + 3) * 30
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            if self.index_list_y + 1 >= 20:
                pass
            else:
                self.index_list_y += 1
                self.y = 25 + (self.index_list_y + 3) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))
        elif keys[pygame.K_d]:
            if self.index_list_x + 1 >= 10:
                pass
            else:
                self.index_list_x += 1
                self.x = 25 + (self.index_list_x + 8) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))
        elif keys[pygame.K_a]:
            if self.index_list_x - 1 <= -1:
                pass
            else:
                self.index_list_x -= 1
                self.x = 25 + (self.index_list_x + 8) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))


def draw_main():
    a = pygame.surface.Surface((300, 600))
    a.fill("black")
    a_r = a.get_rect(center=(400, 400))
    screen.blit(a, a_r)


def draw_horizontal_lines():
    x1 = 250
    x2 = 549
    y = 100
    while y <= 700:
        pygame.draw.line(screen, "#7122F7", (x1, y), (x2, y))
        y += 600 / 20


def draw_vertical_lines():
    y1 = 100
    y2 = 699
    x = 250
    while x <= 550:
        pygame.draw.line(screen, "#7122F7", (x, y1), (x, y2))
        x += 300 / 10


def clarify_sides():
    nr = pygame.rect.Rect((247, 97), (306, 606))
    pygame.draw.rect(screen, "#7122F7", nr, 5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_main()
    draw_vertical_lines()
    draw_horizontal_lines()
    clarify_sides()
    clock.tick(10)
    pygame.display.update()
