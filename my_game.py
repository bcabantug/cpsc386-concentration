import sys
import pygame

# global variables
WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
card_list = [1, 2, 3, 4]
turn = 1


# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
pygame.event.set_blocked(pygame.MOUSEMOTION)

screen.fill(WHITE)
card_sample = pygame.draw.rect(screen, BLACK, (200, 50, 50, 100), 1)
pygame.display.update()

# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

        windows_focus = pygame.mouse.get_focused()
        if windows_focus == 1:

            if turn == 1:
                print("player turn")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    card_sample = pygame.draw.rect(screen, BLACK, (40, 5, 50, 100), 1)
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    turn = 2

            if turn == 2:
                print("AI turn")
                turn = 1



    # Draw / render



    # AFTER drawing everything, flip the display
    pygame.display.update()
# end loop
pygame.quit()
exit(0)
