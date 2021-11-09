import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
screen.fill("#301D50")


class block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((300 / 10, 600 / 20))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(250, 100))
        self.active = True

    def move(self):
        keys = pygame.key.get_pressed()
        if self.active:
            if keys[pygame.K_w]:
                if self.rect.top > 100:
                    self.rect.y -= 30
            elif keys[pygame.K_d]:
                if self.rect.right < 550:
                    self.rect.x += 30
            elif keys[pygame.K_a] :
                if self.rect.left > 250:
                    self.rect.x -= 30

    def update(self, *args, **kwargs) -> None:
        self.move()


a = block()
g1 = pygame.sprite.Group()
g1.add(a)

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
                if member.active:
                    if member.rect.bottom < 700:
                        member.rect.bottom += 30
                    else:
                        member.active = False
                        g1.add(block())
    draw_main()
    g1.draw(screen)
    g1.update()
    draw_vertical_lines()
    draw_horizontal_lines()
    clarify_sides()
    pygame.display.update()
    clock.tick(10)
