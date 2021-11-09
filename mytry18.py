# Score board
# gelecek blok tipi gösterici
# ı type dönme noktası düzeltildi
# yeni çalışma tam değil
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

    def __init__(self, color="red", index_x=0, index_y=0, main_c=False, flip_c=True, I_type=False):
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
                block.main_coor = (index_x + 0.5, index_y - 0.5)
                self.difx = - 0.5
                self.dify = 0.5
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
    def __init__(self, color="red", index_x=0, index_y=0, num_type=1):
        super().__init__()
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill(color)
        self.index_list_x = index_x
        self.index_list_y = index_y
        self.num_type = num_type
        if num_type == 0:
            self.x = 5 + (self.index_list_x + 31) * 20
            self.y = 10 + (self.index_list_y + 11) * 20
        elif num_type == 1:
            self.x = 5 + (self.index_list_x + 31) * 20
            self.y = 10 + (self.index_list_y + 17) * 20
        elif num_type == 2:
            self.x = 5 + (self.index_list_x + 31) * 20
            self.y = 10 + (self.index_list_y + 23) * 20
        self.rect = self.image.get_rect(center=(self.x, self.y))


g1 = pygame.sprite.Group()
g2 = pygame.sprite.Group()
g3_side = pygame.sprite.Group()
pos_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]

new_event = pygame.USEREVENT + 1
pygame.time.set_timer(new_event, 1000)
types_of_blocks = [choice(["I", "O", "J", "L", "S", "Z", "T"]) for ast in range(5)]


def write_tetris():
    t_font = pygame.font.Font("minecrafter/Minecrafter.Alt.ttf", 50)
    tetris = t_font.render("TETRIS", False, (44, 206, 239))
    tetris_r = tetris.get_rect(midtop=(400, 30))
    screen.blit(tetris, tetris_r)


score = 0
top_score = 0


def top_score_board():
    t1_font = pygame.font.Font("minecrafter/Minecrafter.Reg.ttf", 30)
    score_t = t1_font.render("top score", False, (44, 206, 239))
    score_b = t1_font.render(f"{top_score}", False, (44, 206, 239))
    score_tr = score_t.get_rect(center=(120, 150))
    score_br = score_b.get_rect(midtop=(score_tr.centerx, score_tr.bottom + 5))
    screen.blit(score_t, score_tr)
    screen.blit(score_b, score_br)


def score_board():
    t2_font = pygame.font.Font("minecrafter/Minecrafter.Reg.ttf", 30)
    score_t = t2_font.render("score", False, (44, 206, 239))
    score_b = t2_font.render(f"{score}", False, (44, 206, 239))
    score_tr = score_t.get_rect(center=(120, 280))
    score_br = score_b.get_rect(midtop=(score_tr.centerx, score_tr.bottom + 5))
    screen.blit(score_t, score_tr)
    screen.blit(score_b, score_br)


a = 0
b = 0
hour = 0
minu = 0
sec = 0


def time_board():
    t3_font = pygame.font.Font("minecrafter/Minecrafter.Reg.ttf", 30)
    t4_font = pygame.font.Font(None, 40)
    time_t = t3_font.render("time", False, (44, 206, 239))
    time_b = t3_font.render(f"{str(hour).zfill(2)}:{str(minu).zfill(2)}:{str(sec).zfill(2)}", False, (44, 206, 239))
    time_b2 = t4_font.render("".ljust(6) + ":" + "".ljust(6) + ":" + "".ljust(6), False, (44, 206, 239))
    time_tr = time_t.get_rect(center=(120, 600))
    time_br = time_b.get_rect(midtop=(time_tr.centerx, time_tr.bottom + 5))
    time_br2 = time_b2.get_rect(midtop=(time_tr.centerx, time_tr.bottom + 5))
    screen.blit(time_t, time_tr)
    screen.blit(time_b2, time_br2)
    screen.blit(time_b, time_br)


blocks_cleared = 0


def level_board():
    t5_font = pygame.font.Font("minecrafter/Minecrafter.Reg.ttf", 30)
    score_t = t5_font.render("level", False, (44, 206, 239))
    score_b = t5_font.render(f"{blocks_cleared//10}", False, (44, 206, 239))
    score_tr = score_t.get_rect(center=(120, 470))
    score_br = score_b.get_rect(midtop=(score_tr.centerx, score_tr.bottom + 5))
    screen.blit(score_t, score_tr)
    screen.blit(score_b, score_br)


def time_update():
    global a, b, hour, minu, sec
    a = pygame.time.get_ticks()
    main_t = (a - b) // 1000  # milliseconds
    hour, main_t = main_t // 3600, main_t % 3600
    minu, main_t = main_t // 60, main_t % 60
    sec = main_t


def draw_sidemain():
    b = pygame.surface.Surface((120, 360))
    b.fill("black")
    b_r = b.get_rect(center=(675, 400))
    screen.blit(b, b_r)


def draw_sidevertical():
    y1 = 220
    y2 = 579
    x = 615
    while x <= 750:
        pygame.draw.line(screen, "#7122F7", (x, y1), (x, y2))
        x += 120 / 6


def draw_sidehorizontal():
    x1 = 615
    x2 = 734
    y = 220
    while y <= 580:
        pygame.draw.line(screen, "#7122F7", (x1, y), (x2, y))
        y += 360 / 18


def clarify_side2():
    nr = pygame.rect.Rect((612, 217), (126, 366))
    pygame.draw.rect(screen, "#7122F7", nr, 5)
    pygame.draw.line(screen, "#7122F7", (615, 340), (734, 340), 5)
    pygame.draw.line(screen, "#7122F7", (615, 460), (734, 460), 5)
    t_font = pygame.font.Font("minecrafter/Minecrafter.Reg.ttf", 30)
    nxt = t_font.render("next:", False, (44, 206, 239))
    nxt_r = nxt.get_rect(midbottom=(685, 210))
    screen.blit(nxt, nxt_r)


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
    global score,blocks_cleared
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
    if len(indcs_y) == 1:
        score += 40 * ((blocks_cleared//10) + 1)
        blocks_cleared += 1
    elif len(indcs_y) == 2:
        score += 100 * ((blocks_cleared//10) + 1)
        blocks_cleared += 2
    elif len(indcs_y) == 3:
        score += 300 * ((blocks_cleared//10) + 1)
        blocks_cleared += 3
    elif len(indcs_y) == 4:
        score += 1200 * ((blocks_cleared//10) + 1)
        blocks_cleared += 4
    else:
        pass


def add_new_block_type():
    type_b = types_of_blocks.pop(0)
    if type_b == "I":
        g1.add(block("cyan", 0, 2, True, I_type=True))
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


def show_side_blocks():
    g3_side.empty()
    liste = types_of_blocks[:3]
    for i in range(len(liste)):
        if liste[i] == "I":
            g3_side.add(block_side("cyan", 3, 3, i))
            g3_side.add(block_side("cyan", 3, 1, i))
            g3_side.add(block_side("cyan", 3, 2, i))
            g3_side.add(block_side("cyan", 3, 4, i))

        elif liste[i] == "T":
            g3_side.add(block_side("purple", 2, 2, i))
            g3_side.add(block_side("purple", 2, 1, i))
            g3_side.add(block_side("purple", 2, 3, i))
            g3_side.add(block_side("purple", 3, 2, i))
        elif liste[i] == "Z":
            g3_side.add(block_side("red", 3, 3, i))
            g3_side.add(block_side("red", 2, 2, i))
            g3_side.add(block_side("red", 3, 2, i))
            g3_side.add(block_side("red", 4, 3, i))
        elif liste[i] == "S":
            g3_side.add(block_side("green", 3, 3, i))
            g3_side.add(block_side("green", 3, 2, i))
            g3_side.add(block_side("green", 4, 2, i))
            g3_side.add(block_side("green", 2, 3, i))
        elif liste[i] == "J":
            g3_side.add(block_side("blue", 3, 3, i))
            g3_side.add(block_side("blue", 2, 2, i))
            g3_side.add(block_side("blue", 2, 3, i))
            g3_side.add(block_side("blue", 4, 3, i))
        elif liste[i] == "L":
            g3_side.add(block_side("yellow", 3, 3, i))
            g3_side.add(block_side("yellow", 4, 2, i))
            g3_side.add(block_side("yellow", 4, 3, i))
            g3_side.add(block_side("yellow", 2, 3, i))
        elif liste[i] == "O":
            g3_side.add(block_side("orange", 3, 3, i))
            g3_side.add(block_side("orange", 2, 2, i))
            g3_side.add(block_side("orange", 2, 3, i))
            g3_side.add(block_side("orange", 3, 2, i))


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
            coor = (m.index_list_x - m.difx, m.index_list_y - m.dify)
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
            coor = (m.index_list_x - m.difx, m.index_list_y - m.dify)
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
    # Main design
    screen.fill("#301D50")
    write_tetris()
    draw_main()
    draw_sidemain()
    top_score_board()
    score_board()
    time_update()
    time_board()
    level_board()
    # Block control
    if_g1_empty()
    block.min_x, block.max_x = min_max_x()
    left_x()
    right_x()
    # Block draw
    g2.draw(screen)
    g1.draw(screen)
    # g3
    show_side_blocks()
    g3_side.draw(screen)
    # Block update
    g1.update()
    # Block control
    kill_g1()
    # Lines for design
    draw_vertical_lines()
    draw_horizontal_lines()
    draw_sidevertical()  # -->
    draw_sidehorizontal()  # -->
    clarify_sides()
    clarify_side2()
    # Remove blocks
    remove_blocks()
    pygame.display.update()
    clock.tick(10)
