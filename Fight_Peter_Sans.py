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

player = arcade.Sprite('images/shagstill.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=0.2)

herobrine_move = random.randint(1,3)

herobrine_health = 150

cock = arcade.Sprite('images/sans_cock.png', center_x = 40, center_y = random.randint(265,450), scale=0.065)
cock_2 = arcade.Sprite('images/sans_cock.png', center_x = 600, center_y = random.randint(265,450), scale=0.065)
cock.change_x = 10
cock_2.change_x = -10
cock.change_angle = 10
cock_2.change_angle = 10
cock_pos_1 = random.randint(265,450)
cock_pos_2 = random.randint(265,450)


bone = arcade.Sprite('images/sans_bone.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.35)
bone_2 = arcade.Sprite('images/sans_bone2.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.35)
bone.change_y = -10
bone_2.change_y = -10



emerald = arcade.Sprite('images/sans_master_emerald.png', center_x= random.randint(1,640)
, center_y =HEIGHT, scale=0.08)
emerald_2 = arcade.Sprite('images/sans_red_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
emerald_3 = arcade.Sprite('images/sans_blue_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
emerald_4 = arcade.Sprite('images/sans_white_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
emerald_5 = arcade.Sprite('images/sans_yellow_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
emerald.change_y = -10
emerald_2.change_y = -10
emerald_3.change_y = -10
emerald_4.change_y = -10
emerald_5.change_y = -10
turn = random.randint(1, 2)
button1 = [22, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button2 = [184, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button3 = [353, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button4 = [518, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6
health = 100
fight = arcade.Sprite('images/screen_fight.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=1)
n = 1
def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)
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
    bone_2.draw()
    emerald.draw()
    emerald_2.draw()
    emerald_3.draw()
    emerald_4.draw()
    emerald_5.draw()
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
    if emerald.center_y == 160:
        emerald.center_y += HEIGHT
        emerald.center_x = random.randint(1,640)
    if emerald_2.center_y == 160:
        emerald_2.center_y += HEIGHT
        emerald_2.center_x = random.randint(1,640)
    if emerald_3.center_y == 160:
        emerald_3.center_y += HEIGHT
        emerald_3.center_x = random.randint(1,640)
    if emerald_4.center_y == 160:
        emerald_4.center_y += HEIGHT
        emerald_4.center_x = random.randint(1,640)
    if emerald_5.center_y == 160:
        emerald_5.center_y += HEIGHT
        emerald_5.center_x = random.randint(1,640)


















    arcade.draw_xywh_rectangle_filled(220, 50, health * 2, 20, arcade.color.GREEN)
    arcade.draw_xywh_rectangle_filled(160, 90, herobrine_health * 2, 20, arcade.color.RED)
    if button1[BTN_IS_CLICKED]:
        color = button1[BTN_CLICKED_COLOR]
    else:
        color = button1[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button1[BTN_X], button1[BTN_Y], button1[BTN_WIDTH], button1[BTN_HEIGHT],
                                      color)
    if button2[BTN_IS_CLICKED]:
        color = button2[BTN_CLICKED_COLOR]
    else:
        color = button2[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button2[BTN_X], button2[BTN_Y], button2[BTN_WIDTH], button2[BTN_HEIGHT],
                                      color)
    if button3[BTN_IS_CLICKED]:
        color = button3[BTN_CLICKED_COLOR]
    else:
        color = button3[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button3[BTN_X], button3[BTN_Y], button3[BTN_WIDTH], button3[BTN_HEIGHT],
                                      color)
    if button4[BTN_IS_CLICKED]:
        color = button4[BTN_CLICKED_COLOR]
    else:
        color = button4[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button4[BTN_X], button4[BTN_Y], button4[BTN_WIDTH], button4[BTN_HEIGHT],
                                      color)
def update(delta_time):
    global herobrine_health
    global up_pressed, player_y
    global health
    if up_pressed == True:
        player.center_y += 9
    if down_pressed == True:
        player.center_y -= 9
    if left_pressed == True:
        player.center_x -= 9
    if right_pressed == True:
        player.center_x += 9
    if player.center_x > 640:
        player.center_x -= 20
    if player.center_x < 20:
        player.center_x += 20
    if player.center_y > 450:
        player.center_y -= 20
    if player.center_y < 100:
        player.center_y += 20
    if player.center_y < 150:
        player.center_y += 20

    if button1[BTN_IS_CLICKED]:
        herobrine_health -= 0.5
        herobrine_health -= 1

    if button2[BTN_IS_CLICKED]:
        health += 0.5
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
        health -= 2
        print("hit")
        break
    bone.update()
    bone_hit = arcade.check_for_collision(player, bone)
    while bone_hit == True:
        print("hit")
        health -= 1
        break
    bone_2.update()
    bone_hit_2 = arcade.check_for_collision(player, bone_2)
    while bone_hit_2 == True:
        print("hit")
        health -= 1
        break
    emerald.update()
    hit = arcade.check_for_collision(player, emerald)
    while hit == True:
        print("hit")
        health -= 2
        break
    emerald_2.update()
    hit_2 = arcade.check_for_collision(player, emerald_2)
    while hit_2 == True:
        print("hit")
        health -= 2
        break
    emerald_3.update()
    hit_3 = arcade.check_for_collision(player, emerald_3)
    while hit_3 == True:
        print("hit")
        health -= 2
        break
    emerald_4.update()
    hit_4 = arcade.check_for_collision(player, emerald_4)
    while hit_4 == True:
        print("hit")
        break
    emerald_5.update()
    hit_5 = arcade.check_for_collision(player, emerald_5)
    while hit_5 == True:
        health -= 2
        print("hit")
        break
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
