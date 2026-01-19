# Asteroids Game

A classic Asteroids arcade game implementation in Python using Pygame.

## Features

- Classic asteroids gameplay mechanics
- Player spaceship with rotation and movement
- Shooting mechanics with cooldown
- Asteroid splitting system (large asteroids break into smaller ones)
- Score tracking
- Collision detection
- Screen wrapping (player wraps around edges)
- Game state and event logging to JSONL files

## Prerequisites

- Python 3.12 or higher
- uv package manager (recommended) or pip

## Installation

Using uv:
```bash
uv sync
```

Using pip:
```bash
pip install pygame==2.6.1
```

## How to Play

Run the game:
```bash
python main.py
```

### Controls

- `W` - Move forward
- `S` - Move backward
- `A` - Rotate left
- `D` - Rotate right
- `SPACE` - Shoot

### Objective

Destroy asteroids by shooting them. Each asteroid splits into two smaller, faster asteroids when hit. Avoid colliding with asteroids. Score points for each asteroid destroyed.

## Project Structure

- `main.py` - Main game loop and initialization
- `player.py` - Player spaceship class
- `asteroid.py` - Asteroid class with splitting logic
- `asteroidfield.py` - Asteroid spawning system
- `shot.py` - Projectile class
- `circleshape.py` - Base class for circular game objects
- `score.py` - Score tracking
- `logger.py` - Game state and event logging
- `constants.py` - Game configuration constants

## Game Mechanics

- **Player Health**: One hit = game over
- **Asteroid Types**: Three sizes (small, medium, large)
- **Shooting**: 0.3 second cooldown between shots
- **Screen Size**: 1280x720 pixels
- **Asteroid Spawning**: New asteroids spawn every 0.8 seconds

## Logging

The game logs state and events to JSONL files:
- `game_state.jsonl` - Game state snapshots (once per second for 16 seconds)
- `game_events.jsonl` - Game events (asteroid hits, player deaths, etc.)
