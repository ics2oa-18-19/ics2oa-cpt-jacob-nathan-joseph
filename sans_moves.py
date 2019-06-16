import arcade
import random
WIDTH = 640
HEIGHT = 480

player_x = WIDTH/2
player_y = HEIGHT/2

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

player = arcade.Sprite('images/shagstill.png', center_x=WIDTH/2, center_y=350, scale=0.1)

#random coordinate variables
Herobrine_move = random.randint(1,3)
location_1 = random.randint(1,640)
location_2 = random.randint(1,640)
location_3 = random.randint(1,640)
location_4 = random.randint(1,640)
location_5 = random.randint(1,640)
location_x_1 = random.randint(240,480)
location_x_2 = random.randint(240,480)
location_x_3 = random.randint(240,480)
location_x_4 = random.randint(240,480)
location_x_5 = random.randint(240,480)

#attacks
cock = arcade.Sprite('images/sans_cock.png', center_x = 40, center_y = random.randint(265,450), scale=0.2)
cock_2 = arcade.Sprite('images/sans_cock.png', center_x = 600, center_y = random.randint(265,450), scale=0.2)
cock.change_x = +8
cock_2.change_x = -8

bone = arcade.Sprite('images/sans_bone.png', center_x = 700, center_y = location_x_1, scale=0.35)
bone_2 = arcade.Sprite('images/sans_bone.png', center_x = 700, center_y = location_x_2, scale=0.35)
bone_3 = arcade.Sprite('images/sans_bone2.png', center_x = location_1, center_y = 690, scale = 0.35)
bone_4 = arcade.Sprite('images/sans_bone2.png', center_x = location_2, center_y = 690, scale = 0.35)
bone.change_x = -10
bone_2.change_x = -10
bone_3.change_y = -10
bone_4.change_y = -10


emeralds = arcade.Sprite('images/sans_master_emerald.png', center_x=700, center_y =location_x_1, scale=0.2)
emeralds_2 = arcade.Sprite('images/sans_blue_emerald.png', center_x= 690, center_y = location_x_2, scale= 0.07)
emeralds_3 = arcade.Sprite('images/sans_yellow_emerald.png', center_x= 750, center_y = location_x_3, scale= 0.4)
emeralds_4 = arcade.Sprite('images/sans_red_emerald.png', center_x= 800, center_y = location_x_4, scale= 0.08)
emeralds_5 = arcade.Sprite('images/sans_white_emerald.png', center_x= 840, center_y = location_x_5, scale= 0.07)
emeralds.change_x = -10
emeralds_2.change_x = -10
emeralds_3.change_x = -10
emeralds_4.change_x = -10
emeralds_5.change_x = -10

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

fight = arcade.Sprite('images/screen_fight.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=1)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)

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
    if Herobrine_move == 1:
            cock.draw()
            cock_2.draw()
    if Herobrine_move == 2:
            bone.draw()
            bone_2.draw()
            bone_3.draw()
            bone_4.draw()
    if Herobrine_move == 3:
            emeralds.draw()
            emeralds_2.draw()
            emeralds_3.draw()
            emeralds_4.draw()
            emeralds_5.draw()



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


def update(delta_time):
#moving shaggy
    global up_pressed, player_y
    if up_pressed == True:
        player.center_y += 6
    if down_pressed == True:
        player.center_y -= 6
    if left_pressed == True:
        player.center_x -= 6
    if right_pressed == True:
        player.center_x += 6

#border
    if player.center_x > 640:
        player.center_x -= 5
    if player.center_x < 20:
        player.center_x += 5
    if player.center_y > 480:
        player.center_y -= 5
    if player.center_y < 230:
        player.center_y += 5
    
    #stopping attacks
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


def on_key_press(key, modifiers):
#key presses
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
#buttons
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
    arcade.schedule(update, 1/60)

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
