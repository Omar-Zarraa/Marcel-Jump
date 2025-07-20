import pygame

gravity = 10
speed = 1
time = 0


class Character:
    def __init__(self, image, x, y, w=200, h=200) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y

        self.image = pygame.transform.scale(self.image, (w, h))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


def main():
    # setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("font", 20)
    player = Character("character.png", 540, 260, 150, 150)
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global time
                    time = 0
                    if player.y > 0:
                        player.y = player.y - 100

        # pygame.display.update()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE
        player.draw(screen)
        time += 1
        if player.y < screen.get_height() - 200:
            global speed
            speed = gravity * time / 60
            player.y = player.y + speed
        else:
            speed = 1
            time = 0
            
        if player.y > screen.get_height() - 201:
            print("Dead")
            running = False

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
