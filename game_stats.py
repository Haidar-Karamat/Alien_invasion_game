

import json
from pathlib import Path


class GameStats:
    """Track statistics that change during and across games."""

    # Store the high score file next to the rest of the game source
    # so it works regardless of the current working directory.
    HIGH_SCORE_FILE = Path(__file__).resolve().parent / "high_score.json"

    def __init__(self, settings):
        self.settings = settings
        self.high_score = self._load_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Reset statistics that change during a single playthrough."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_score(self, points):
        """Add points to the score and update the high score if beaten."""
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def _load_high_score(self):
        """Load the high score from disk, defaulting to 0."""
        if self.HIGH_SCORE_FILE.exists():
            try:
                with open(self.HIGH_SCORE_FILE, encoding="utf-8") as f:
                    data = json.load(f)
                return int(data.get("high_score", 0))
            except (json.JSONDecodeError, OSError, ValueError):
                return 0
        return 0

    def save_high_score(self):
        """Persist the current high score to disk."""
        try:
            with open(self.HIGH_SCORE_FILE, "w", encoding="utf-8") as f:
                json.dump({"high_score": self.high_score}, f)
        except OSError:
            # Don't crash the game if the file can't be written.
            pass
