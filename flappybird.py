import pygame

gravity = 10
speed = 1
time = 0


class Character:
    def __init__(
        self, image: str, x: float, y: float, w: float = 200, h: float = 200
    ) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.hitBox = (w, h)
        self.image = pygame.transform.scale(self.image, (w, h))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, pygame.Color("black"), self.hitBox)
        screen.blit(self.image, (self.x, self.y))

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float):
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float):
        self._y = y

    @property
    def pos(self) -> tuple:
        return self._pos

    @pos.setter
    def pos(self, pos: tuple):
        self._pos = pos

    @property
    def hitBox(self) -> pygame.Rect:
        return self._hitBox

    @hitBox.setter
    def hitBox(self, widthHeight: tuple):
        self._hitBox = pygame.Rect(self.pos, widthHeight)


class Pole:
    def __init__(self, image: str, x: float, y: float, w: float, h: float) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.hitBox = (w, h)
        self.image = pygame.transform.scale(self.image, (w, h))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float):
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float):
        self._y = y

    @property
    def pos(self) -> tuple:
        return self._pos

    @pos.setter
    def pos(self, pos: tuple):
        self._pos = pos

    @property
    def hitBox(self) -> pygame.Rect:
        return self._hitBox

    @hitBox.setter
    def hitBox(self, widthHeight: tuple):
        self._hitBox = pygame.Rect(self.pos, widthHeight)


def areColliding(character: Character, pole: Pole) -> bool:
    return character.pos == pole.pos


def characterGravity(player: Character, screen: pygame.Surface) -> bool:
    player.draw(screen)
    global time
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
        return False

    return True


def main():
    # setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("font", 20)
    player = Character("character.png", 540, 260, 150, 150)
    pole = Pole("Pole.png", 550, 200, 300, 600)
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global time
                    time = 0
                    if player.y > 0:
                        for _ in range(4):
                            player.y = player.y - 25

        # pygame.display.update()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE
        if not characterGravity(player, screen):
            running = False
        pole.draw(screen)
        # pole.x -= 10
        print(areColliding(player, pole))

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
