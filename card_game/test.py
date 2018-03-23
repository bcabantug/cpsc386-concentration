import pygame, os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


pygame.init()
screen = pygame.display.set_mode((680, 420))
font = pygame.font.SysFont("Arial", 100, False, False)
text = font.render("test", False, (0, 0, 0))
background = pygame.image.load(os.path.join(img_folder, "background.png")).convert()
background = pygame.transform.scale(background, (680, 420))
rect = background.get_rect()
rect.center = (680 / 2, 420 / 2)
text_rect = text.get_rect()
text_rect.center = (680 / 2, 420 / 2)
screen.fill((0, 0, 0))



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(background, rect)
    screen.blit(text, text_rect)

    pygame.display.flip()

