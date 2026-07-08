# Alien Invasion

A classic space-shooter built with Python and [Pygame](https://www.pygame.org/). Defend against a descending alien fleet, level up as you clear waves, and chase your high score.

## Requirements

- Python 3.9+
- Pygame

```bash
pip install pygame
```

## Running the Game

From the project folder:

```bash
python alien_invasion.py
```

## Controls

| Key / Action          | Effect                          |
|------------------------|----------------------------------|
| **P**                  | Start the game                  |
| **Click "Play" button**| Start the game                  |
| **←  Left Arrow**      | Move ship left                  |
| **→  Right Arrow**     | Move ship right                 |
| **Space**              | Fire a bullet                   |
| **Q**                  | Quit the game                   |

The mouse cursor is visible on the start screen and hides automatically once you start playing.

## How to Play

1. Launch the game — you'll see the **Play** button on a blank screen.
2. Press **P** or click **Play** to begin.
3. Move your ship with the arrow keys and shoot the descending aliens with **Space**.
4. Clearing every alien in a wave **levels you up**: a new fleet spawns, and your ship, bullets, and the aliens all move faster.
5. You lose a ship if an alien collides with you or reaches the bottom of the screen. Losing your last ship ends the game and returns you to the start screen.
6. Your best score is saved automatically and reloaded the next time you play.

## Scoring & Leveling

- Each alien destroyed adds points to your score, based on the current level's point value.
- Point value per alien increases each level (`alien_points *= score_scale`).
- Ship, bullet, and alien speeds all increase each level (`speed *= speedup_scale`).
- Difficulty resets to the base values whenever a fresh game starts.

Both scaling factors live in `settings.py` and can be tuned:

```python
speedup_scale: float = 1.1   # how much faster things get per level
score_scale: float = 1.5     # how much more each alien is worth per level
```

## On-Screen HUD

Displayed at the top of the screen during play:

- **Ships** (top-left) — lives remaining
- **High Score** (top-center) — best score ever recorded, loaded from `high_score.json`
- **Score** (top-right) — current run's score
- **Level** (below score, top-right) — current wave/level number

## Project Structure

```
Alien_Invasion_Game/
├── alien_invasion.py       # Entry point; main game loop and state
├── settings.py             # All tunable game settings + difficulty scaling
├── ship.py                 # Player ship
├── bullet.py                # Bullets fired by the ship
├── alien.py                # Single alien sprite
├── fleet.py                 # Manages the alien fleet as a group
├── collision_system.py     # Bullet/alien, ship/alien, scoring, leveling, game over
├── input_handler.py        # Maps keyboard events to actions (command pattern)
├── asset_factory.py        # Loads and caches scaled images
├── layout.py                 # Calculates fleet row/column layout
├── button.py                # Play button shown on the start screen
├── game_stats.py            # Score, level, ships left, high score persistence
├── scoreboard.py             # Renders the HUD (score, high score, level, ships)
├── high_score.json           # Auto-created; stores the persisted high score
├── images/                   # Ship and alien sprite images
└── tests/                    # Pytest test suite
```

## Persisted High Score

`game_stats.py` reads and writes `high_score.json` in the project folder:

```json
{"high_score": 1250}
```

If the file doesn't exist or is unreadable, the game simply starts with a high score of `0` — no crash, no setup required.

## Running Tests

```bash
pip install pytest
pytest tests/
```
