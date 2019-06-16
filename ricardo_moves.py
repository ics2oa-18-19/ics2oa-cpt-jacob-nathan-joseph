import arcade
import random

WIDTH = 640
HEIGHT = 480

player_x = WIDTH / 2
player_y = HEIGHT / 2

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

player = arcade.Sprite('images/shagstill.png', center_x=WIDTH / 2, center_y=350, scale=0.1)

# random coordinate variables
Ricardo_move = random.randint(1,3)
location_1 = random.randint(1, 640)
location_2 = random.randint(1, 640)
location_3 = random.randint(1, 640)
location_4 = random.randint(1, 640)
location_5 = random.randint(1, 640)
location_x_1 = random.randint(240, 480)
location_x_2 = random.randint(240, 480)
location_x_3 = random.randint(240, 480)
location_x_4 = random.randint(240, 480)
location_x_5 = random.randint(240, 480)

# attacks
flex = arcade.Sprite('images/ricardo_flex.png', center_x=320, center_y=-200, scale=3)
flex.change_y = +4

charm = arcade.Sprite('images/ricardo_charm.png', center_x=700, center_y=location_x_1, scale=0.07)
charm_2 = arcade.Sprite('images/ricardo_charm.png', center_x=780, center_y=location_x_2, scale=0.07)
charm_3 = arcade.Sprite('images/ricardo_charm.png', center_x=860, center_y=location_x_3, scale=0.07)
charm_4 = arcade.Sprite('images/ricardo_charm.png', center_x=940, center_y=location_x_4, scale=0.07)
charm.change_x = -6
charm_2.change_x = -6
charm_3.change_x = -6
charm_4.change_x = -6

ricardo = arcade.Sprite('images/ricardo_ricardo2.gif', center_x=700, center_y=300, scale=0.2)
ricardo_2 = arcade.Sprite('images/ricardo_ricardo3.png', center_x=-750, center_y=340, scale=0.25)
ricardo_3 = arcade.Sprite('images/ricardo_ricardo4.gif', center_x=-1500, center_y=2000, scale=0.5)
ricardo_4 = arcade.Sprite('images/ricardo_ricardo5.gif', center_x=2950, center_y=2600, scale=0.6)
ricardo_5 = arcade.Sprite('images/ricardo_ricardo.png', center_x=320, center_y=-968, scale=0.4)
ricardo.change_x = -10
ricardo_2.change_x = +10
ricardo_3.change_x = +10
ricardo_3.change_y = -10
ricardo_4.change_x = -11
ricardo_4.change_y = -10
ricardo_5.change_y = +3

button1 = [22, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]
button2 = [184, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]
button3 = [353, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]
button4 = [518, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]

BTN_X = 1
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

health = 100

fight = arcade.Sprite('images/screen_fight.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


def on_draw():
    arcade.draw_xywh_rectangle_filled(220, 50, health * 2, 20, arcade.color.GREEN)
    if button1[BTN_IS_CLICKED]:
        color = button1[BTN_CLICKED_COLOR]
    else:
        color = button1[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button1[BTN_Y > 184], button1[BTN_X], button1[BTN_WIDTH], button1[BTN_HEIGHT],
                                      color)
    if button2[BTN_IS_CLICKED]:
        color = button2[BTN_CLICKED_COLOR]
    else:
        color = button2[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button2[BTN_Y > 184], button2[BTN_X], button2[BTN_WIDTH], button2[BTN_HEIGHT],
                                      color)
    if button3[BTN_IS_CLICKED]:
        color = button3[BTN_CLICKED_COLOR]
    else:
        color = button3[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button3[BTN_Y > 184], button3[BTN_X], button3[BTN_WIDTH], button3[BTN_HEIGHT],
                                      color)
    if button4[BTN_IS_CLICKED]:
        color = button4[BTN_CLICKED_COLOR]
    else:
        color = button4[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button4[BTN_Y > 184], button4[BTN_X], button4[BTN_WIDTH], button4[BTN_HEIGHT],
                                      color)

    arcade.start_render()
    fight.draw()
    player.draw()
    if Ricardo_move == 1:
        flex.draw()
    if Ricardo_move == 2:
        charm.draw()
        charm_2.draw()
        charm_3.draw()
        charm_4.draw()
    if Ricardo_move == 3:
        ricardo.draw()
        ricardo_2.draw()
        ricardo_3.draw()
        ricardo_4.draw()
        ricardo_5.draw()

def update(delta_time):
    # moving shaggy
    global up_pressed, player_y
    if up_pressed == True:
        player.center_y += 6
    if down_pressed == True:
        player.center_y -= 6
    if left_pressed == True:
        player.center_x -= 6
    if right_pressed == True:
        player.center_x += 6

    # border
    if player.center_x > 640:
        player.center_x -= 5
    if player.center_x < 20:
        player.center_x += 5
    if player.center_y > 480:
        player.center_y -= 5
    if player.center_y < 230:
        player.center_y += 5

    # stopping attacks
    flex.update()
    if flex.center_y == 600:
        flex.stop
    charm.update()
    if charm.center_x == -100:
        charm.stop()
    charm_2.update()
    if charm_2.center_x == -100:
        charm_2.stop()
    charm_3.update()
    if charm_3.center_x == -100:
        charm_3.stop()
    charm_4.update()
    if charm_4.center_x == -100:
        charm_4.stop()
    ricardo.update()
    if ricardo.center_y == 265:
        ricardo.stop()
    ricardo_2.update()
    if ricardo_2.center_y == 265:
        ricardo_2.stop()
    ricardo_3.update()
    if ricardo_3.center_y == 265:
        ricardo_3.stop()
    ricardo_4.update()
    if ricardo_4.center_y == 265:
        ricardo_4.stop()
    ricardo_5.update()
    if ricardo_5.center_y == 273:
        ricardo_5.stop()


def on_key_press(key, modifiers):
    # key presses
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
    # buttons
    print(f"Click at ({x}, {y})")
    if (x > button1[BTN_X] and x < button1[BTN_X] + button1[BTN_WIDTH] and
            y > button1[BTN_Y] and y < button1[BTN_Y] + button1[BTN_HEIGHT]):
        button1[BTN_IS_CLICKED] = True
    if (x > button2[BTN_X] and x < button2[BTN_X] + button2[BTN_WIDTH] and
            y > button2[BTN_Y] and y < button2[BTN_Y] + button2[BTN_HEIGHT]):
        button2[BTN_IS_CLICKED] = True
    if (x > button3[BTN_X] and x < button3[BTN_X] + button3[BTN_WIDTH] and
            y > button3[BTN_Y] and y < button3[BTN_Y] + button3[BTN_HEIGHT]):
        button3[BTN_IS_CLICKED] = True
    if (x > button4[BTN_X] and x < button4[BTN_X] + button4[BTN_WIDTH] and
            y > button4[BTN_Y] and y < button4[BTN_Y] + button4[BTN_HEIGHT]):
        button4[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    button1[BTN_IS_CLICKED] = False
    button2[BTN_IS_CLICKED] = False
    button3[BTN_IS_CLICKED] = False
    button4[BTN_IS_CLICKED] = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


if __name__ == '__main__':
    setup()
