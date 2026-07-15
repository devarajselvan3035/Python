import pygame
from pygame.locals import *
import sys


class SimpleButton:
    # Used to track the state of the button
    STATE_IDLE = "idle"  # button is up, mouse not over button
    STATE_ARMED = "armed"  # button is down, mouse over button
    STATE_DISARMED = "disarmed"  # clicked down on button, rolled off

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # Get the rect of the button (used to see if the mouse is over the button)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        # This method will return True if user clicks the button.
        # Normally returns False.

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # The button only cares about mouse-related events
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True  # clicked!

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED
        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # Draw the button's current appearance to the window
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)

        else:  # IDLE or DISARMED
            self.window.blit(self.surfaceUp, self.loc)


# if __name__ == "__main__":
#     # Pygame demo 7 - SimpleButton test
#     BLACK = (0, 0, 0)
#     WINDOW_WIDTH = 640
#     WINDOW_HEIGHT = 480
#     FRAMES_PER_SECOND = 30
#     GRAY = (0, 255, 255)
#
#     # 3 - Initialize the world
#     pygame.init()
#     window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#     clock = pygame.time.Clock()
#
#     # 5 - Initialize variables
#     # Create an instance of a SimpleButton
#     oButton = SimpleButton(
#         window, (150, 30), "./img/buttonAUp.png", "./img/buttonADown.png"
#     )
#
#     # 6 - Loop forever
#     while True:
#         # 7 - Check for and handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#             # Pass the event to the button, see if it has been clicked on
#             if oButton.handleEvent(event):
#                 print("User has clicked the button")
#
#         # 8 - Do any "per frame" actions
#
#         # 9 - Clear the window
#         window.fill(GRAY)
#         # 10 - Draw all window elements
#         oButton.draw()  # draw the button
#
#         # 11 - Update the window
#         pygame.display.update()
#
#         # 12 - Slow things down a bit
#         clock.tick(FRAMES_PER_SECOND)
