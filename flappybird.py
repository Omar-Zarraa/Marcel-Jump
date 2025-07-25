import pygame, sys, random

pygame.init()

# Global variables
gravity = 10
speed = 1
time = 0
stagger = 0


# Character class which the 'player' object is an instance of
class Character:
    def __init__(
        self, image: str, x: float, y: float, w: float = 200, h: float = 200
    ) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pos = (x, y)
        self.hitBox = (w - 60, h - 60)
        self.image = pygame.transform.scale(self.image, (w, h))

    def draw(self, screen: pygame.Surface):
        self.hitBox = (self.hitBox.w, self.hitBox.h)
        screen.blit(self.image, self.pos)

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, w):
        self._w = w

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

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
        self._hitBox = pygame.Rect(
            (self.pos[0] + self.w / 4, self.pos[1] + self.h / 4), widthHeight
        )


# Pole class which the poles are objects of
class Pole:
    def __init__(self, image: str, x: float, y: float, w: float, h: float) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pos = (x, y)
        self.hitBox = (w - 200, h - 300)
        self.image = pygame.transform.scale(self.image, (w, h))

    def draw(self, screen):
        self.hitBox = (self.hitBox.w, self.hitBox.h)
        # pygame.draw.rect(screen, pygame.Color("black"), self.hitBox)
        screen.blit(self.image, self.pos)

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, w):
        self._w = w

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

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
        self._hitBox = pygame.Rect(
            (self.pos[0] + self.w / 3, self.pos[1] + self.h / 4), widthHeight
        )


# Function that enables character gravity and returns False if the character hit the ground
def characterGravity(player: Character, screen: pygame.Surface) -> bool:
    player.draw(screen)
    global time
    time += 1
    if player.pos[1] < screen.get_height() - 200:
        global speed
        speed = gravity * time / 60
        player.y += speed
        player.pos = (player.x, player.y)
    else:
        speed = 1
        time = 0

    if player.pos[1] > screen.get_height() - 201:
        return False

    return True


# Function to move the poles across the screen
def movePole(xMove: float, screen: pygame.Surface, poles: list) -> None:
    for pole in poles:
        pole[0].draw(screen)
        pole[0].x -= 10
        pole[0].pos = (pole[0].x, pole[0].y)
        pole[1].draw(screen)
        pole[1].x -= 10
        pole[1].pos = (pole[1].x, pole[1].y)


# Function that shows the starting screen with the 'play button'
def mainMenu(image: str) -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("font", 20)

    playButton = pygame.image.load(image).convert_alpha()
    playButton = pygame.transform.scale(playButton, (700, 450))
    buttonRect = pygame.Rect((520, 290), (250, 150))

    screen.fill("white")

    screen.blit(playButton, (280, 130))

    while True:
        try:
            flag = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    flag = False
                    break
                if event.type == pygame.MOUSEBUTTONUP:
                    if buttonRect.collidepoint(event.pos):
                        flag = False
                        break

            pygame.display.update()
            pygame.display.flip()

            clock.tick(60)
            if not flag:
                break
        except pygame.error:
            pygame.quit()
            sys.exit()
    main()


# Function that shows the 'Game Over' screen with the 'restart' and 'quit' buttons
def deathScreen(
    screen: pygame.Surface, image: str, w: float, h: float, pos: tuple
) -> None:
    pygame.init()

    global stagger, time
    stagger = time = 0
    clock = pygame.time.Clock()

    screen.fill("White")

    gameOver = pygame.image.load(image).convert_alpha()
    gameOver = pygame.transform.scale(gameOver, (w, h))
    restart = pygame.Rect((500, 280), (200, 100))
    quit = pygame.Rect((500, 435), (200, 100))

    screen.blit(gameOver, pos)

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    main()
                if event.type == pygame.MOUSEBUTTONUP:
                    if restart.collidepoint(event.pos):
                        main()
                    elif quit.collidepoint(event.pos):
                        sys.exit()

            pygame.display.update()
            pygame.display.flip()

            clock.tick(60)
        except pygame.error:
            pygame.quit()


# Functions to create the initial 5 poles of the game
def makePoles(poles: list) -> None:
    for _ in range(5):
        global stagger
        y = random.randint(250, 450)
        poles.append(
            [
                Pole("Pole.png", 2000 + stagger, y, 300, 600),
                Pole("PoleR.png", 2000 + stagger, y - 550, 300, 600),
            ]
        )
        stagger += 500


# Function that checks whether the player has collided with a pole
def checkCollision(poles: list[list[Pole]], player: Character) -> bool:
    for pole in poles:
        if player.hitBox.colliderect(pole[0].hitBox) or player.hitBox.colliderect(
            pole[1].hitBox
        ):
            return True
    return False


# The main function of the game
def main() -> None:
    # setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("font", 20)
    player = Character("character.png", 540, 260, 150, 150)
    poles = []
    # pole = Pole("Pole.png", 1200, 200, 300, 600)
    running = True

    makePoles(poles)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global time
                    time = 0
                    if player.pos[1] > 0:
                        player.y -= 100
                        player.pos = (player.x, player.y)
        # pygame.display.update()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE
        global stagger, deletions
        if len(poles) > 0:
            if poles[0][0].x < 0:
                del poles[0]
                y = random.randint(250, 450)
                poles.append(
                    [
                        Pole("Pole.png", poles[len(poles) - 1][0].x + 500, y, 300, 600),
                        Pole(
                            "PoleR.png",
                            poles[len(poles) - 1][1].x + 500,
                            y - 550,
                            300,
                            600,
                        ),
                    ]
                )

        if not characterGravity(player, screen):
            running = False

        movePole(10, screen, poles)

        if checkCollision(poles, player):
            running = False

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    deathScreen(screen, "GameOver.png", 720, 1000, (250, -150))


if __name__ == "__main__":
    mainMenu("Play.png")
