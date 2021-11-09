# Düzenleme 4 (deneme)
# blokların tipleri
import pygame
from random import choice

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
screen.fill("#301D50")


class block(pygame.sprite.Sprite):
    max_x = None
    min_x = None

    def __init__(self, color="red", index_x=0, index_y=0, btype=None):
        super().__init__()
        self.image = pygame.surface.Surface((300 / 10, 600 / 20))
        self.image.fill(color)
        self.index_list_x = index_x
        self.index_list_y = index_y
        self.x = 25 + (self.index_list_x + 8) * 30
        self.y = 25 + (self.index_list_y + 3) * 30
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sit_check = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            if self.index_list_y + 1 >= 20:
                pass
            elif pos_list[self.index_list_y + 1][self.index_list_x] != 0:
                pass
            else:
                self.index_list_y += 1
                self.y = 25 + (self.index_list_y + 3) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))
        elif keys[pygame.K_d]:
            if self.index_list_x + 1 >= 10:
                pass
            elif pos_list[self.index_list_y][self.index_list_x + 1] != 0:
                pass
            elif block.max_x == 9:
                pass
            else:
                self.index_list_x += 1
                self.x = 25 + (self.index_list_x + 8) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))
        elif keys[pygame.K_a]:
            if self.index_list_x - 1 <= -1:
                pass
            elif pos_list[self.index_list_y][self.index_list_x - 1] != 0:
                pass
            elif block.min_x == 0:
                pass
            else:
                self.index_list_x -= 1
                self.x = 25 + (self.index_list_x + 8) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))

    def pos_update(self):
        if self.index_list_y + 1 >= 20 or pos_list[self.index_list_y + 1][self.index_list_x] != 0:
            self.sit_check = True

    def update(self, *args, **kwargs) -> None:
        self.move()
        self.pos_update()


g1 = pygame.sprite.Group()
g2 = pygame.sprite.Group()
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


def remove_blocks():
    indcs_y = []
    for index in range(len(pos_list)):
        if set(pos_list[index]) == {1}:
            indcs_y.append(index)
    if len(indcs_y) > 0:
        for obj in g2:
            if obj.index_list_y in indcs_y:
                obj.kill()
        for i in range(len(indcs_y)):
            pos_list.pop(max(indcs_y))
            pos_list.insert(0, [0 for n in range(10)])
        for o in g2:
            if o.index_list_y < min(indcs_y):
                o.index_list_y += len(indcs_y)
                o.y = 25 + (o.index_list_y + 3) * 30
                o.rect = o.image.get_rect(center=(o.x, o.y))


type_v = 0


def add_new_block_type():
    block_types = ["I", "O", "J", "L", "S", "Z", "T"]
    type_b = choice(block_types)
    if type_b == "I":
        g1.add(block("cyan", 0, 0, type_b))
        g1.add(block("cyan", 0, 1, type_b))
        g1.add(block("cyan", 0, 2, type_b))
        g1.add(block("cyan", 0, 3, type_b))

    elif type_b == "T":
        g1.add(block("purple", 0, 0, type_b))
        g1.add(block("purple", 0, 1, type_b))
        g1.add(block("purple", 0, 2, type_b))
        g1.add(block("purple", 1, 1, type_b))
    elif type_b == "Z":
        g1.add(block("red", 0, 0, type_b))
        g1.add(block("red", 1, 0, type_b))
        g1.add(block("red", 1, 1, type_b))
        g1.add(block("red", 2, 1, type_b))
    elif type_b == "S":
        g1.add(block("green", 1, 0, type_b))
        g1.add(block("green", 2, 0, type_b))
        g1.add(block("green", 1, 1, type_b))
        g1.add(block("green", 0, 1, type_b))
    elif type_b == "J":
        g1.add(block("blue", 0, 0, type_b))
        g1.add(block("blue", 0, 1, type_b))
        g1.add(block("blue", 1, 1, type_b))
        g1.add(block("blue", 2, 1, type_b))
    elif type_b == "L":
        g1.add(block("yellow", 2, 0, type_b))
        g1.add(block("yellow", 2, 1, type_b))
        g1.add(block("yellow", 1, 1, type_b))
        g1.add(block("yellow", 0, 1, type_b))
    elif type_b == "O":
        g1.add(block("orange", 0, 0, type_b))
        g1.add(block("orange", 0, 1, type_b))
        g1.add(block("orange", 1, 1, type_b))
        g1.add(block("orange", 1, 0, type_b))


def kill_g1():
    situation = False
    for m in g1:
        if m.sit_check:
            situation = True
            break
    if situation:
        for m in g1:
            m.kill()
            pos_list[m.index_list_y][m.index_list_x] = 1
            g2.add(m)
        print(pos_list)


def min_max_x():
    new_max = None
    new_min = None
    for m in g1:
        if new_max is None and new_min is None:
            new_max, new_min = m.index_list_x, m.index_list_x
        else:
            if m.index_list_x > new_max:
                new_max = m.index_list_x
            if m.index_list_x < new_min:
                new_min = m.index_list_x
    return new_min, new_max


def if_g1_empty():
    if len(g1) == 0:
        add_new_block_type()


add_new_block_type()
block.min_x, block.max_x = min_max_x()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == new_event:
            for member in g1:
                if member.index_list_y + 1 >= 20:
                    pass
                elif pos_list[member.index_list_y + 1][member.index_list_x] != 0:
                    pass
                else:
                    member.index_list_y += 1
                    member.y = 25 + (member.index_list_y + 3) * 30
                    member.rect = member.image.get_rect(center=(member.x, member.y))

    draw_main()
    if_g1_empty()
    g2.draw(screen)
    g1.draw(screen)
    g1.update()
    block.min_x, block.max_x = min_max_x()
    kill_g1()
    draw_vertical_lines()
    draw_horizontal_lines()
    clarify_sides()
    remove_blocks()
    pygame.display.update()
    clock.tick(10)
