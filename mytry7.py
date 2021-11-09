# Yeniden düzenleme
import pygame
from random import choice

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
        self.active = True
        self.down_active = True

    def move(self):
        keys = pygame.key.get_pressed()
        if self.active:
            if keys[pygame.K_s]:
                self.down_active = False
                if self.index_list_y + 1 < 20:
                    self.index_list_y += 1
                    self.y = 25 + (self.index_list_y + 3) * 30
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                else:
                    pos_list[member.index_list_y][member.index_list_x] = 1
                    print(pos_list)
                    self.active = False
                    g1.add(block(choice(("red", "cyan", "yellow", "purple"))))

            elif keys[pygame.K_d]:
                if self.index_list_x + 1 < 10:
                    self.index_list_x += 1
                    self.x = 25 + (self.index_list_x + 8) * 30
                    self.rect = self.image.get_rect(center=(self.x, self.y))
            elif keys[pygame.K_a]:
                if self.index_list_x - 1 > -1:
                    self.index_list_x -= 1
                    self.x = 25 + (self.index_list_x + 8) * 30
                    self.rect = self.image.get_rect(center=(self.x, self.y))
            else:
                self.down_active = True

    def update(self, *args, **kwargs) -> None:
        self.move()


a = block(choice(("red", "cyan", "yellow", "purple")))
g1 = pygame.sprite.Group()
g1.add(a)
pos_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]

new_event = pygame.USEREVENT + 1
pygame.time.set_timer(new_event, 1000)


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
        if event.type == new_event:
            for member in g1:
                if member.active and member.down_active:
                    if member.index_list_y + 1 < 20:
                        member.index_list_y += 1
                        member.y = 25 + (member.index_list_y + 3) * 30
                        member.rect = member.image.get_rect(center=(member.x, member.y))
                    else:
                        pos_list[member.index_list_y][member.index_list_x] = 1
                        print(pos_list)
                        member.active = False
                        g1.add(block(choice(("red", "cyan", "yellow", "purple"))))
    draw_main()
    g1.draw(screen)
    g1.update()
    draw_vertical_lines()
    draw_horizontal_lines()
    clarify_sides()
    pygame.display.update()
    clock.tick(10)
