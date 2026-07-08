"""Defines a simple clickable Button (used for the Play button)."""

import pygame
import pygame.font


class Button:
    """A rectangular button with centered text."""

    def __init__(self, screen, msg, *, width=200, height=50,
                 bg_color=(0, 135, 0), text_color=(255, 255, 255)):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = width, height
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 44)

        # Build the button rect and center it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image, centered on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.bg_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the blank button, then draw the message on top."""
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
