# Simple 3D Game Example

This repository contains a minimal example of a 3D game written in Python using
[PyGame](https://www.pygame.org/) and [PyOpenGL](https://pyopengl.sourceforge.net/).
The example features a basic player, bots, monsters, the ability to place blocks
for simple building, and a placeholder audio effect. It serves as a starting
point for a more advanced project.

## Requirements

- Python 3.10+
- `pygame`
- `PyOpenGL` and `PyOpenGL_accelerate`
- `numpy`

Install the dependencies with:

```bash
pip install pygame PyOpenGL PyOpenGL_accelerate numpy
```

## Running the Game

Run the main script:

```bash
python3 game/main.py
```

Controls:

- **Arrow keys**: Move the player around.
- **B**: Place a block at the player's current location.
- **Esc**: Quit the game.

Bots and monsters roam randomly as placeholders. Blocks are rendered as wireframe
cubes. The game demonstrates the basics for a larger project with real
structures, bots, monsters, audio, weapons, and tools.
