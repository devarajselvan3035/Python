import pygame
from pygame.locals import *
import sys
import random


class Ball:
    def __init__(self, window, window_width, widdow_hight) -> None:
        self.window = window
        self.windowWidth = window_width
        self.windowHeight = widdow_hight

        self.image = pygame.image.load("./img/ball.png")
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = self.windowWidth - self.width
        self.maxHeight = self.windowHeight - self.height

        # Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not zero,
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]

        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


# if __name__ == "__main__":
#     # 2 - Define constants
#     BLACK = (0, 0, 0)
#     WINDOW_WIDTH = 640
#     WINDOW_HEIGHT = 480
#     FRAMES_PER_SECOND = 30
#
#     # 3 - Initialize the world
#     pygame.init()
#     window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#     clock = pygame.time.Clock()
#
#     # 4 - Load assets: image(s), sound(s), etc.
#
#     # 5 - Initialize variables
#     oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
#     oBall1 = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
#     oBall2 = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
#
#     # 6 - Loop forever
#     while True:
#         # 7 - Check for and handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#         # 8 - Do any "per frame" actions
#         oBall.update()  # tell the Ball to update itself
#         oBall1.update()
#         oBall2.update()
#
#         # 9 - Clear the window before drawing it again
#         window.fill(BLACK)
#
#         # 10 - Draw the window elements
#         oBall.draw()
#         oBall1.draw()  # tell the Ball to draw itself
#         oBall2.draw()  # tell the Ball to draw itself
#
#         # 11 - Update the window
#         pygame.display.update()
#         clock.tick(FRAMES_PER_SECOND)
