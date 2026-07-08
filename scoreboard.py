

import pygame.font


class Scoreboard:
    """Reports scoring info onto the HUD area of the screen."""

    def __init__(self, screen, settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 28)

        # Prepare the initial score images
        self.prep_images()

    def prep_images(self):
        """Prepare all HUD images from scratch."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Render the current score as an image."""
        score_str = f"Score: {self.stats.score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 15

    def prep_high_score(self):
        """Render the high score as an image."""
        high_score_str = f"High Score: {self.stats.high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 15

    def prep_level(self):
        """Render the current level as an image."""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 8

    def prep_ships(self):
        """Render the number of ships remaining as an image."""
        ships_str = f"Ships: {self.stats.ships_left}"
        self.ships_image = self.font.render(
            ships_str, True, self.text_color, self.settings.bg_color
        )
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.left = 20
        self.ships_rect.top = 15

    def show_score(self):
        """Draw scores, level, and ships remaining to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ships_rect)
