
import os
import arcade

WIDTH = 640
HEIGHT = 480

player_x = WIDTH/2
player_y = HEIGHT/2

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

player = arcade.Sprite('images/shagstill.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=0.2)

# Add a horizontal speed to the player sprite


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


def update(delta_time):
    global up_pressed, player_y
    if up_pressed == True:
        player.center_y += 3
    if down_pressed == True:
        player.center_y -= 3
    if left_pressed == True:
        player.center_x -= 3
    if right_pressed == True:
        player.center_x += 3

       
def on_draw():
    arcade.start_render()
    # Draw in here...
    player.draw()


def on_key_press(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = True

    global down_pressed
    if key == arcade.key.S:
        down_pressed = True
    global right_pressed
    if key == arcade.key.D:
        right_pressed = True
    global left_pressed
    if key == arcade.key.A:
        left_pressed = True


def on_key_release(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = False

    global down_pressed
    if key == arcade.key.S:
        down_pressed = False
        
    global right_pressed
    if key == arcade.key.D:
        right_pressed = False

    global left_pressed
    if key == arcade.key.A:
        left_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
