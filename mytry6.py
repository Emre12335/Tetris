# Obstacles movement and types
import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
screen.fill("#301D50")


class block(pygame.sprite.Sprite):
    def __init__(self, color="red", tl=(250, 100)):
        super().__init__()
        self.image = pygame.surface.Surface((300 / 10, 600 / 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=tl)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 30
        elif keys[pygame.K_d]:
            self.rect.x += 30
        elif keys[pygame.K_a]:
            self.rect.x -= 30

    def update(self, *args, **kwargs) -> None:
        self.move()


class obs_type:
    def __init__(self, o_type):
        if o_type == 1: # square
            self.b1 = block(color="yellow")
            self.b2 = block(tl=(280, 100),color="yellow")
            self.b3 = block(tl=(250, 130),color="yellow")
            self.b4 = block(tl=(280, 130),color="yellow")
        elif o_type == 2: # I
            self.b1 = block(color="cyan")
            self.b2 = block(tl=(250, 130),color="cyan")
            self.b3 = block(tl=(250, 160),color="cyan")
            self.b4 = block(tl=(250, 190),color="cyan")
        elif o_type == 3: # I-
            self.b1 = block(color="purple")
            self.b2 = block(tl=(250,130),color="purple")
            self.b3 = block(tl=(280,130),color="purple")
            self.b4 = block(tl=(250,160),color="purple")
        elif o_type == 4: # Z
            self.b1 = block()
            self.b2 = block(tl=(280,100))
            self.b3 = block(tl=(280,130))
            self.b4 = block(tl=(310,130))
        elif o_type == 5: # Reverse Z
            self.b1 = block(tl=(280,100),color="green")
            self.b2 = block(tl=(310,100),color="green")
            self.b3 = block(tl=(250,130),color="green")
            self.b4 = block(tl=(280,130),color="green")
        elif o_type == 6: # L horizontal
            self.b1 = block(tl=(310,100),color="orange")
            self.b2 = block(tl=(250,130),color="orange")
            self.b3 = block(tl=(280,130),color="orange")
            self.b4 = block(tl=(310,130),color="orange")
        elif o_type == 7:
            self.b1 = block(color="blue")
            self.b2 = block(tl=(250,130),color="blue")
            self.b3 = block(tl=(280,130),color="blue")
            self.b4 = block(tl=(310,130),color="blue")

        else:
            pass
        self.active_fall = True
        self.active_move = True

    def update(self):
        if not self.active_fall:
            self.active_move = False
        else:
            self.active_move = self.active_check()
        if self.active_move:
            self.b1.update()
            self.b2.update()
            self.b3.update()
            self.b4.update()

    def active_check(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.b1.rect.top - 30 < 100 or self.b2.rect.top - 30 < 100 or self.b3.rect.top - 30 < 100 \
                    or self.b4.rect.top - 30 < 100:
                return False
        if keys[pygame.K_d]:
            if self.b1.rect.right + 30 > 550 or self.b2.rect.right + 30 > 550 or self.b3.rect.right + 30 > 550 \
                    or self.b4.rect.right + 30 > 550:
                return False
        if keys[pygame.K_a]:
            if self.b1.rect.left - 30 < 250 or self.b2.rect.left - 30 < 250 or self.b3.rect.left - 30 < 250 \
                    or self.b4.rect.left - 30 < 250:
                return False
        return True

    def draw(self):
        screen.blit(self.b1.image, self.b1.rect)
        screen.blit(self.b2.image, self.b2.rect)
        screen.blit(self.b3.image, self.b3.rect)
        screen.blit(self.b4.image, self.b4.rect)


main_obs = []

new_event = pygame.USEREVENT + 1
pygame.time.set_timer(new_event, 1000)


def draw_obst():
    for member in main_obs:
        member.draw()


def update_obst():
    for member in main_obs:
        member.update()


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
            if len(main_obs) == 0:
                main_obs.append(obs_type(randint(1,7)))
            else:
                for ct in main_obs:
                    if ct.active_fall:
                        if ct.b1.rect.bottom < 700 and ct.b2.rect.bottom < 700 and ct.b3.rect.bottom < 700 \
                                and ct.b4.rect.bottom < 700:
                            ct.b1.rect.bottom += 30
                            ct.b2.rect.bottom += 30
                            ct.b3.rect.bottom += 30
                            ct.b4.rect.bottom += 30
                        else:
                            ct.active_fall = False
                            main_obs.append(obs_type(randint(1,7)))
    draw_main()
    draw_obst()
    update_obst()
    draw_vertical_lines()
    draw_horizontal_lines()
    clarify_sides()
    pygame.display.update()
    clock.tick(10)
