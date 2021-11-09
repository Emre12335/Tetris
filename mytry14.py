# Düzenleme 7 (deneme)
# flip ayarları oturtuldu
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
    left_x = False
    right_x = False
    down_motion = False
    main_coor = (0, 0)

    def __init__(self, color="red", index_x=0, index_y=0, main_c=False, flip_c=True, I_type = False):
        super().__init__()
        self.image = pygame.surface.Surface((300 / 10, 600 / 20))
        self.image.fill(color)
        self.index_list_x = index_x
        self.index_list_y = index_y
        self.x = 25 + (self.index_list_x + 8) * 30
        self.y = 25 + (self.index_list_y + 3) * 30
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sit_check = False
        self.flip_c = flip_c
        self.I_type = I_type
        if main_c:
            if I_type:
                block.main_coor = (index_x + 0.5,index_y - 0.5)
                self.difx = - 0.5
                self.dify =  0.5
            else:
                block.main_coor = (index_x, index_y)
                self.difx = 0
                self.dify = 0
        else:
            self.difx = self.index_list_x - block.main_coor[0]
            self.dify = self.index_list_y - block.main_coor[1]

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
            if block.max_x == 9:
                pass
            elif block.right_x:
                pass
            else:
                self.index_list_x += 1
                self.x = 25 + (self.index_list_x + 8) * 30
                self.rect = self.image.get_rect(center=(self.x, self.y))
        elif keys[pygame.K_a]:
            if block.min_x == 0:
                pass
            elif block.left_x:
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


class block_side(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pass


g1 = pygame.sprite.Group()
g2 = pygame.sprite.Group()
pos_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]

new_event = pygame.USEREVENT + 1
pygame.time.set_timer(new_event, 1000)
types_of_blocks = [choice(["I", "O", "J", "L", "S", "Z", "T"]) for ast in range(5)]


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
        for ind in indcs_y:
            for o in g2:
                if o.index_list_y < ind:
                    o.index_list_y += 1
                    o.y = 25 + (o.index_list_y + 3) * 30
                    o.rect = o.image.get_rect(center=(o.x, o.y))
            del pos_list[ind]
            pos_list.insert(0, [0 for i in range(10)])


def add_new_block_type():
    type_b = types_of_blocks.pop(0)
    if type_b == "I":
        g1.add(block("cyan", 0, 2, True,I_type=True))
        g1.add(block("cyan", 0, 0))
        g1.add(block("cyan", 0, 1))
        g1.add(block("cyan", 0, 3))

    elif type_b == "T":
        g1.add(block("purple", 0, 1, True))
        g1.add(block("purple", 0, 0))
        g1.add(block("purple", 0, 2))
        g1.add(block("purple", 1, 1))
    elif type_b == "Z":
        g1.add(block("red", 1, 1, True))
        g1.add(block("red", 0, 0))
        g1.add(block("red", 1, 0))
        g1.add(block("red", 2, 1))
    elif type_b == "S":
        g1.add(block("green", 1, 1, True))
        g1.add(block("green", 1, 0))
        g1.add(block("green", 2, 0))
        g1.add(block("green", 0, 1))
    elif type_b == "J":
        g1.add(block("blue", 1, 1, True))
        g1.add(block("blue", 0, 0))
        g1.add(block("blue", 0, 1))
        g1.add(block("blue", 2, 1))
    elif type_b == "L":
        g1.add(block("yellow", 1, 1, True))
        g1.add(block("yellow", 2, 0))
        g1.add(block("yellow", 2, 1))
        g1.add(block("yellow", 0, 1))
    elif type_b == "O":
        g1.add(block("orange", 1, 1, flip_c=False))
        g1.add(block("orange", 0, 0, flip_c=False))
        g1.add(block("orange", 0, 1, flip_c=False))
        g1.add(block("orange", 1, 0, flip_c=False))


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
        add_new_block_type()
        types_of_blocks.append(choice(["I", "O", "J", "L", "S", "Z", "T"]))
        print(pos_list)
        print(types_of_blocks)


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
        types_of_blocks.append(choice(["I", "O", "J", "L", "S", "Z", "T"]))


def left_x():
    for m in g1:
        if block.min_x != 0:
            if pos_list[m.index_list_y][m.index_list_x - 1] == 1:
                block.left_x = True
                break
            else:
                block.left_x = False


def right_x():
    for m in g1:
        if block.max_x != 9:
            if pos_list[m.index_list_y][m.index_list_x + 1] == 1:
                block.right_x = True
                break
            else:
                block.right_x = False


def down_motion_check():
    an = pygame.key.get_pressed()
    if an[pygame.K_s]:
        block.down_motion = True
    else:
        block.down_motion = False


def flip_blocks_left():
    coor = ()
    for m in g1:
        if m.difx == 0 and m.dify == 0 and not m.I_type:
            coor = (m.index_list_x, m.index_list_y)
        elif m.I_type:
            coor = (m.index_list_x + m.difx,m.index_list_y + m.dify)
    situation = True
    for m in g1:
        if not m.flip_c:
            situation = False
            break
        elif coor[1] - m.difx < 0 or coor[1] - m.difx > 19 or coor[0] + m.dify < 0 or coor[0] + m.dify > 9:
            situation = False
            break
        else:
            if pos_list[int(coor[1] - m.difx)][int(coor[0] + m.dify)] == 1:
                situation = False
                break
    if situation:
        for m in g1:
            m.index_list_x = int(coor[0] + m.dify)
            m.index_list_y = int(coor[1] - m.difx)
            m.x = 25 + (m.index_list_x + 8) * 30
            m.y = 25 + (m.index_list_y + 3) * 30
            m.rect = m.image.get_rect(center=(m.x, m.y))
            m.difx, m.dify = m.dify, -m.difx


def flip_blocks_right():
    coor = ()
    for m in g1:
        if m.difx == 0 and m.dify == 0 and not m.I_type:
            coor = (m.index_list_x, m.index_list_y)
        elif m.I_type:
            coor = (m.index_list_x + m.difx,m.index_list_y + m.dify)
    situation = True
    for m in g1:
        if not m.flip_c:
            situation = False
            break
        elif coor[1] + m.difx < 0 or coor[1] + m.difx > 19 or coor[0] - m.dify < 0 or coor[0] - m.dify > 9:
            situation = False
            break
        else:
            if pos_list[int(coor[1] + m.difx)][int(coor[0] - m.dify)] == 1:
                situation = False
                break
    if situation:
        for m in g1:
            m.index_list_x = int(coor[0] - m.dify)
            m.index_list_y = int(coor[1] + m.difx)
            m.x = 25 + (m.index_list_x + 8) * 30
            m.y = 25 + (m.index_list_y + 3) * 30
            m.rect = m.image.get_rect(center=(m.x, m.y))
            m.difx, m.dify = -m.dify, m.difx


block.min_x, block.max_x = min_max_x()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                flip_blocks_left()
            elif event.key == pygame.K_l:
                flip_blocks_right()
        if event.type == new_event:
            down_motion_check()
            for member in g1:
                if member.index_list_y + 1 >= 20:
                    pass
                elif pos_list[member.index_list_y + 1][member.index_list_x] != 0:
                    pass
                elif block.down_motion:
                    pass
                else:
                    member.index_list_y += 1
                    member.y = 25 + (member.index_list_y + 3) * 30
                    member.rect = member.image.get_rect(center=(member.x, member.y))

    draw_main()
    if_g1_empty()
    block.min_x, block.max_x = min_max_x()
    left_x()
    right_x()
    g2.draw(screen)
    g1.draw(screen)
    g1.update()
    kill_g1()
    draw_vertical_lines()
    draw_horizontal_lines()
    clarify_sides()
    remove_blocks()
    pygame.display.update()
    clock.tick(10)
