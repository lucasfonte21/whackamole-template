import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x = random.randrange(0, 20)
        y = random.randrange(0, 16)

        running = True
        while running:
            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "dark blue", (i * 32, 0), (i * 32, 512))
            for i in range(16):
                pygame.draw.line(screen, "dark blue", (0, i * 32), (640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(32 * x, 32 * y)))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if x * 32 <= mouse_x < (x + 1) * 32 and y * 32 <= mouse_y < (y + 1) * 32:
                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(32 * x, 32 * y)))

            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
