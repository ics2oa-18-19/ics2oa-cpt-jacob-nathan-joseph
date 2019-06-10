import math
import os
import arcade

WIDTH = 640
HEIGHT = 480

health = 100

attack_1 = [640, 240, 30]

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
    global health
    if up_pressed is True:
        player.center_y += 3
    if down_pressed is True:
        player.center_y -= 3
    if left_pressed is True:
        player.center_x -= 3
    if right_pressed is True:
        player.center_x += 3

    a = player_x - attack_1[0]
    b = player_y - attack_1[1]
    dist = math.sqrt(a**2 + b**2)

    # compare distance to r1 and r2
    if dist < attack_1[2] + player_x:
        health -= 10

    global attack_1
    attack_1[0] = attack_1[0] -= 5

    if attack_1[0] <= 0:
        attack_1[0] = 640


def on_draw():
    arcade.start_render()
    # Draw in here...
    player.draw()
    arcade.draw_circle_filled(attack_1[0], attack_1[1], attack_1[2], arcade.color.BLUE)
    arcade.draw_xywh_rectangle_filled(10, 10, health * 2, 50, arcade.color.YELLOW)


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