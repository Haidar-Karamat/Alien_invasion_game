"""Defines settings data class"""

from dataclasses import dataclass, field


@dataclass
class Settings:
    """Represents game settings data"""
    screen_width: int = 900
    screen_height: int = 600
    bg_color: tuple = (42, 42, 42)

    # Ship settings
    ship_height: int = 40
    ship_speed: float = 1.5
    ship_limit: int = 3

    # Bullet settings
    bullet_speed: float = 2.5
    bullet_width : int = 3
    bullet_height: int = 15
    bullet_color: tuple = (247, 240, 82)
    bullet_active_limit: int = 5

    # Alien settings
    alien_height: int = 55
    alien_buffer_rows: int = 3
    alien_speed: float = 1.0
    alien_points: int = 50

    # Fleet settings
    fleet_drop_step: int = 20

    # HUD settings
    hud_height: int = 55

    # Difficulty/leveling settings
    speedup_scale: float = 1.1
    score_scale: float = 1.5

    # Base values retained so speeds can be reset for a fresh game
    _base_ship_speed: float = field(init=False, repr=False, default=0.0)
    _base_bullet_speed: float = field(init=False, repr=False, default=0.0)
    _base_alien_speed: float = field(init=False, repr=False, default=0.0)
    _base_alien_points: int = field(init=False, repr=False, default=0)

    def __post_init__(self):
        # Remember the values the settings were created with, then use
        # them as the baseline every time a new game starts.
        self._base_ship_speed = self.ship_speed
        self._base_bullet_speed = self.bullet_speed
        self._base_alien_speed = self.alien_speed
        self._base_alien_points = self.alien_points

    def initialize_dynamic_settings(self):
        """Reset speeds and scoring back to their starting values."""
        self.ship_speed = self._base_ship_speed
        self.bullet_speed = self._base_bullet_speed
        self.alien_speed = self._base_alien_speed
        self.alien_points = self._base_alien_points

    def increase_speed(self):
        """Scale up speeds and alien point value; called on level up."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)