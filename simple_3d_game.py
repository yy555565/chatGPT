import pyglet
from pyglet.gl import *

window = pyglet.window.Window(800, 600, "Simple 3D Game")

# Load sound
jump_sound = pyglet.media.load('jump.wav', streaming=False)

# Simple cube using triangles (vertex list)
vertices = [
    -0.5, -0.5, -0.5,
     0.5, -0.5, -0.5,
     0.5,  0.5, -0.5,
    -0.5,  0.5, -0.5,
    -0.5, -0.5,  0.5,
     0.5, -0.5,  0.5,
     0.5,  0.5,  0.5,
    -0.5,  0.5,  0.5
]

indices = [0,1,2, 2,3,0, 4,5,6, 6,7,4, 0,4,5, 5,1,0, 2,6,7, 7,3,2, 0,4,7, 7,3,0, 1,5,6, 6,2,1]

rotation = 0

def update(dt):
    global rotation
    rotation += dt * 50

@window.event
def on_draw():
    window.clear()
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -3.0)
    glRotatef(rotation, 0, 1, 0)
    pyglet.graphics.draw_indexed(8, GL_TRIANGLES, indices, ("v3f", vertices))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        jump_sound.play()

if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()
