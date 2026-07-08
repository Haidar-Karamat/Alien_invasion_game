
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from fleet import Fleet
from collision_system import CollisionSystem
from input_handler import InputHandler
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


class AlienInvasion:
    """Orchestrates game components"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()

        self.stats = GameStats(self.settings)
        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.fleet = Fleet(self.screen, self.settings)
        self.scoreboard = Scoreboard(self.screen, self.settings, self.stats)
        self.collision_system = CollisionSystem(
            self.bullets, self.fleet, self.ship, self.settings,
            self.stats, self.scoreboard, self._end_game
        )
        self.play_button = Button(self.screen, "Play")

        # Game starts on the start screen: not active, cursor visible.
        self.game_active = False
        pygame.mouse.set_visible(True)

        self._setup_input_handler() # An attempt at command pattern

    def run_game(self):
        while True:
            # Process user input events
            self._check_events()

            if self.game_active:
                # Logic update phase
                self.ship.update()
                self._update_bullets()
                self.fleet.update()
                self.collision_system.update()

            # Render phase
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responds to mouse and keypress events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(pygame.mouse.get_pos())
            else:
                self.input_handler.handle_input(event)

    def _check_play_button(self, mouse_pos):
        """Start the game if the Play button was clicked."""
        if not self.game_active and self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()

    def _start_game(self):
        """Reset game state and begin a new playthrough."""
        if self.game_active:
            return

        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.scoreboard.prep_images()

        self.fleet.aliens.empty()
        self.bullets.empty()
        self.fleet.create()
        self.ship.recenter()

        self.game_active = True
        pygame.mouse.set_visible(False)

    def _end_game(self):
        """Called by the collision system when the player runs out of ships."""
        self.game_active = False
        pygame.mouse.set_visible(True)

    def _fire_bullets(self):
        if not self.game_active:
            return
        if self.settings.bullet_active_limit > len(self.bullets):
            new_bullet = Bullet(self.screen, self.settings, self.ship.rect)
            self.bullets.add(new_bullet)

    def _setup_input_handler(self):
        """
        Configure key to action mapping.

        Initialise and instantiate the input handler.
        """
        keydown_map = {
            pygame.K_RIGHT: self.ship.start_moving_right,
            pygame.K_LEFT: self.ship.start_moving_left,
            pygame.K_SPACE: self._fire_bullets,
            pygame.K_p: self._start_game,
            pygame.K_q: sys.exit
        }
        keyup_map = {
            pygame.K_RIGHT: self.ship.stop_moving_right,
            pygame.K_LEFT: self.ship.stop_moving_left
        }

        self.input_handler = InputHandler(keydown_map, keyup_map)

    def _update_bullets(self):
        """Processes bullets' positions."""
        self.bullets.update()

        # Remove bullet if it reaches top of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Render to the display surface"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        self.fleet.draw()
        self.scoreboard.show_score()

        if not self.game_active:
            self.play_button.draw()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
