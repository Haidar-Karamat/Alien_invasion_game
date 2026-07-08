

import pygame


class CollisionSystem:
    """Class manages all cross-domain interactions"""

    def __init__(self, bullets, fleet, ship, settings, stats, scoreboard,
                 game_over_callback):
        self.bullets = bullets
        self.fleet = fleet
        self.ship = ship
        self.settings = settings
        self.stats = stats
        self.scoreboard = scoreboard
        self.game_over_callback = game_over_callback

    def update(self):
        """Coordinate interactions - public entry point"""
        self._handle_aliens_bullets_collisions()

        if self.stats.ships_left <= 0:
            return

        self._handle_alien_ship_collisions()

        if self.stats.ships_left <= 0:
            return

        self._handle_aliens_reached_bottom()

    def _handle_aliens_bullets_collisions(self):
        """Processes alien and bullets collisions"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.fleet.aliens, True, True
        )

        if collisions:
            for aliens_hit in collisions.values():
                self.stats.update_score(
                    len(aliens_hit) * self.settings.alien_points
                )
            self.scoreboard.prep_score()
            self.scoreboard.prep_high_score()

        if not self.fleet.aliens:
            self.bullets.empty()
            self._level_up()

    def _handle_alien_ship_collisions(self):
        """React to any alien colliding directly with the ship."""
        if pygame.sprite.spritecollideany(self.ship, self.fleet.aliens):
            self._ship_hit()

    def _handle_aliens_reached_bottom(self):
        """Treat an alien reaching the bottom of the screen like a hit."""
        for alien in self.fleet.aliens:
            if alien.rect.bottom >= self.ship.screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship losing a life."""
        self.stats.ships_left -= 1
        self.scoreboard.prep_ships()

        if self.stats.ships_left > 0:
            self.fleet.aliens.empty()
            self.bullets.empty()
            self.fleet.create()
            self.ship.recenter()
        else:
            self.game_over_callback()

    def _level_up(self):
        """Increase difficulty and spawn a fresh fleet."""
        self.stats.level += 1
        self.scoreboard.prep_level()
        self.settings.increase_speed()
        self.fleet.create()
