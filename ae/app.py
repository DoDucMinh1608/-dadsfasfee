import pygame


class App:
    screen = (600, 600)
    fps = 60
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(screen)

    def __init__(self: str) -> None:
        pass

    def write() -> list:
        return

    def run(self) -> None:
        pygame.init()
        while True:
            pygame.display.flip()
            # pygame.draw.lines(self.display, (255, 255, 255), points=[
            #                   [0, 0], [100, 300], [200, 30]], closed=False, width=3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


app = App()

app.run()
