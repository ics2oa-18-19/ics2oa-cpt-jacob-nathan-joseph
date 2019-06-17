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

player = arcade.Sprite('shag.png', center_x=WIDTH / 2, center_y=350, scale=0.1)

# random coordinate variables
sans_move = random.randint(1, 3)
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
cock = arcade.Sprite('sans_cock.png', center_x=40, center_y=random.randint(265, 450), scale=0.2)
cock_2 = arcade.Sprite('sans_cock.png', center_x=600, center_y=random.randint(265, 450), scale=0.2)
cock.change_x = +8
cock_2.change_x = -8

bone = arcade.Sprite('sans_bone.png', center_x=700, center_y=location_x_1, scale=0.35)
bone.change_x = -10

emeralds = arcade.Sprite('sans_master_emerald.png', center_x=700, center_y=location_x_1, scale=0.2)
emeralds_2 = arcade.Sprite('sans_blue_emerald.png', center_x=690, center_y=location_x_2, scale=0.07)
emeralds_3 = arcade.Sprite('sans_yellow_emerald.png', center_x=750, center_y=location_x_3, scale=0.4)
emeralds_4 = arcade.Sprite('sans_red_emerald.png', center_x=800, center_y=location_x_4, scale=0.08)
emeralds_5 = arcade.Sprite('sans_white_emerald.png', center_x=840, center_y=location_x_5, scale=0.07)
emeralds.change_x = -10
emeralds_2.change_x = -10
emeralds_3.change_x = -10
emeralds_4.change_x = -10
emeralds_5.change_x = -10

button6 = [22, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]
button7 = [184, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]
button8 = [353, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]
button9 = [518, 1.5, 115, 40, False, (255, 0, 0, 0), arcade.color.GREEN]

BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

health = 100
sans_health = 150

n = 1

fight = arcade.Sprite('fight.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)


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
    arcade.start_render()
    fight.draw()
    player.draw()
    cock.draw()
    cock_2.draw()
    bone.draw()
    emeralds.draw()
    emeralds_2.draw()
    emeralds_3.draw()
    emeralds_4.draw()
    emeralds_5.draw()
    if cock.center_x == 600:
        cock.change_x = -10
        cock.center_y = random.randint(265,450)
    elif cock.center_x == 40:
        cock.change_x = 10
        cock.center_y = random.randint(265, 450)
    if cock_2.center_x == 40:
        cock_2.change_x = 10
        cock_2.center_y = random.randint(265, 450)
    elif cock_2.center_x == 600:
        cock_2.change_x = -10
        cock_2.center_y = random.randint(265, 450)
    if bone.center_y == 400:
        bone.center_y += HEIGHT
        bone.center_x = random.randint(1,640)
    if emeralds.center_y == 160:
        emeralds.center_y += HEIGHT
        emeralds.center_x = random.randint(1,640)
    if emeralds_2.center_y == 160:
        emeralds_2.center_y += HEIGHT
        emeralds_2.center_x = random.randint(1,640)
    if emeralds_3.center_y == 160:
        emeralds_3.center_y += HEIGHT
        emeralds_3.center_x = random.randint(1,640)
    if emeralds_4.center_y == 160:
        emeralds_4.center_y += HEIGHT
        emeralds_4.center_x = random.randint(1,640)
    if emeralds_5.center_y == 160:
        emeralds_5.center_y += HEIGHT
        emeralds_5.center_x = random.randint(1,640)

    if button6[BTN_IS_CLICKED]:
        color = button6[BTN_CLICKED_COLOR]
    else:
        color = button6[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button6[BTN_X], button6[BTN_Y], button6[BTN_WIDTH], button6[BTN_HEIGHT],
                                      color)

    if button7[BTN_IS_CLICKED]:
        color = button7[BTN_CLICKED_COLOR]
    else:
        color = button7[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button7[BTN_X], button7[BTN_Y], button7[BTN_WIDTH], button7[BTN_HEIGHT],
                                      color)

    if button8[BTN_IS_CLICKED]:
        color = button8[BTN_CLICKED_COLOR]
    else:
        color = button8[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button8[BTN_X], button8[BTN_Y], button8[BTN_WIDTH], button8[BTN_HEIGHT],
                                      color)

    if button9[BTN_IS_CLICKED]:
        color = button9[BTN_CLICKED_COLOR]
    else:
        color = button9[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button9[BTN_X], button9[BTN_Y], button9[BTN_WIDTH], button9[BTN_HEIGHT],
                                      color)

    arcade.draw_xywh_rectangle_filled(220, 50, health * 2, 20, arcade.color.GREEN)
    arcade.draw_xywh_rectangle_filled(160, 90, sans_health * 2, 20, arcade.color.RED)


def update(delta_time):
    # moving shaggy
    global up_pressed, player_y, health, sans_health
    if up_pressed == True:
        player.center_y += 6
    if down_pressed == True:
        player.center_y -= 6
    if left_pressed == True:
        player.center_x -= 6
    if right_pressed == True:
        player.center_x += 6

    # stopping attacks
    cock.update()
    cock_2.update()
    bone.update()
    if bone.center_x == -100:
        bone.stop()
    bone_2.update()
    if bone_2.center_x == -100:
        bone_2.stop()
    bone_3.update()
    if bone_3.center_y == -80:
        bone_3.stop()
    bone_4.update()
    if bone_4.center_y == -80:
        bone_4.stop()
    emeralds.update()
    if emeralds.center_y == 265:
        emeralds.stop()
    emeralds_2.update()
    if emeralds_2.center_y == 265:
        emeralds_2.stop()
    emeralds_3.update()
    if emeralds_3.center_y == 265:
        emeralds_3.stop()
    emeralds_4.update()
    if emeralds_4.center_y == 265:
        emeralds_4.stop()
    emeralds_5.update()
    if emeralds_5.center_y == 265:
        emeralds_5.stop()

    if button6[BTN_IS_CLICKED]:
        sans_health -= 1

    if button7[BTN_IS_CLICKED]:
        health += 0.7

    cock.update()

    cock_hit = arcade.check_for_collision(player, cock)
    while cock_hit == True:
        health -= 2
        break
    cock_2.update()
    cock_hit_2 = arcade.check_for_collision(player, cock_2)
    while cock_hit_2 == True:
        health -= 2
        break

    bone.update()
    bone_hit = arcade.check_for_collision(player, bone)
    while bone_hit == True:
        health -= 1
        break
    emeralds.update()
    hit = arcade.check_for_collision(player, emeralds)
    while hit == True:
        health -= 2
        break
    emeralds_2.update()
    hit_2 = arcade.check_for_collision(player, emeralds_2)
    while hit_2 == True:
        health -= 2
        break
    emeralds_3.update()
    hit_3 = arcade.check_for_collision(player, emeralds_3)
    while hit_3 == True:
        health -= 2
        break
    emeralds_4.update()
    hit_4 = arcade.check_for_collision(player, emeralds_4)
    while hit_4 == True:
        break
    emeralds_5.update()
    hit_5 = arcade.check_for_collision(player, emeralds_5)
    while hit_5 == True:
        health -= 2
        break

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
    if (x > button6[BTN_X] and x < button6[BTN_X] + button6[BTN_WIDTH] and
            y > button6[BTN_Y] and y < button6[BTN_Y] + button6[BTN_HEIGHT]):
        button6[BTN_IS_CLICKED] = True
    if (x > button7[BTN_X] and x < button7[BTN_X] + button7[BTN_WIDTH] and
            y > button7[BTN_Y] and y < button7[BTN_Y] + button7[BTN_HEIGHT]):
        button7[BTN_IS_CLICKED] = True
    if (x > button8[BTN_X] and x < button8[BTN_X] + button8[BTN_WIDTH] and
            y > button8[BTN_Y] and y < button8[BTN_Y] + button8[BTN_HEIGHT]):
        button8[BTN_IS_CLICKED] = True
    if (x > button9[BTN_X] and x < button9[BTN_X] + button9[BTN_WIDTH] and
            y > button9[BTN_Y] and y < button9[BTN_Y] + button9[BTN_HEIGHT]):
        button9[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    button6[BTN_IS_CLICKED] = False
    button7[BTN_IS_CLICKED] = False
    button8[BTN_IS_CLICKED] = False
    button9[BTN_IS_CLICKED] = False


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
