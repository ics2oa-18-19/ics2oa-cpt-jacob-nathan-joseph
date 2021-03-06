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
player = arcade.Sprite('shag.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=0.2)
herobrine_move = random.randint(1,3)
herobrine_health = 150
mine = arcade.Sprite('mine.png', center_x = 40, center_y = random.randint(265,450), scale=0.065)
mine_2 = arcade.Sprite('mine.png', center_x = 600, center_y = random.randint(265,450), scale=0.065)
mine.change_x = 10
mine_2.change_x = -10
mine.change_angle = 10
mine_2.change_angle = 10
mine_pos_1 = random.randint(265,450)
mine_pos_2 = random.randint(265,450)


smite = arcade.Sprite('smite.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.35)
smite_2 = arcade.Sprite('smite.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.35)
smite.change_y = -10
smite_2.change_y = -10



bolt = arcade.Sprite('bolt.png', center_x= random.randint(1,640)
, center_y =HEIGHT, scale=0.08)
bolt_2 = arcade.Sprite('bolt.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
bolt_3 = arcade.Sprite('bolt.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
bolt_4 = arcade.Sprite('bolt.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
bolt_5 = arcade.Sprite('bolt.png',center_x= random.randint(1,640)
, center_y = HEIGHT, scale= 0.08)
bolt.change_y = -10
bolt_2.change_y = -10
bolt_3.change_y = -10
bolt_4.change_y = -10
bolt_5.change_y = -10
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
fight = arcade.Sprite('fight.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=1)
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
    mine.draw()
    mine_2.draw()
    smite.draw()
    smite_2.draw()
    bolt.draw()
    bolt_2.draw()
    bolt_3.draw()
    bolt_4.draw()
    bolt_5.draw()
    if mine.center_x == 600:
        mine.change_x = -10
        mine.center_y = random.randint(265,450)
    elif mine.center_x == 40:
        mine.change_x = 10
        mine.center_y = random.randint(265, 450)
    if mine_2.center_x == 40:
        mine_2.change_x = 10
        mine_2.center_y = random.randint(265, 450)
    elif mine_2.center_x == 600:
        mine_2.change_x = -10
        mine_2.center_y = random.randint(265, 450)
    if smite.center_y == 400:
        smite.center_y += HEIGHT
        smite.center_x = random.randint(1,640)
    if bolt.center_y == 160:
        bolt.center_y += HEIGHT
        bolt.center_x = random.randint(1,640)
    if bolt_2.center_y == 160:
        bolt_2.center_y += HEIGHT
        bolt_2.center_x = random.randint(1,640)
    if bolt_3.center_y == 160:
        bolt_3.center_y += HEIGHT
        bolt_3.center_x = random.randint(1,640)
    if bolt_4.center_y == 160:
        bolt_4.center_y += HEIGHT
        bolt_4.center_x = random.randint(1,640)
    if bolt_5.center_y == 160:
        bolt_5.center_y += HEIGHT
        bolt_5.center_x = random.randint(1,640)


















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

    mine.update()

    mine_hit = arcade.check_for_collision(player, mine)
    while mine_hit == True:
        health -= 2
        break
    mine_2.update()
    mine_hit_2 = arcade.check_for_collision(player, mine_2)
    while mine_hit_2 == True:
        health -= 2
        print("hit")
        break
    smite.update()
    smite_hit = arcade.check_for_collision(player, smite)
    while smite_hit == True:
        print("hit")
        health -= 1
        break
    smite_2.update()
    smite_hit_2 = arcade.check_for_collision(player, smite_2)
    while smite_hit_2 == True:
        print("hit")
        health -= 1
        break
    bolt.update()
    hit = arcade.check_for_collision(player, bolt)
    while hit == True:
        print("hit")
        health -= 2
        break
    bolt_2.update()
    hit_2 = arcade.check_for_collision(player, bolt_2)
    while hit_2 == True:
        print("hit")
        health -= 2
        break
    bolt_3.update()
    hit_3 = arcade.check_for_collision(player, bolt_3)
    while hit_3 == True:
        print("hit")
        health -= 2
        break
    bolt_4.update()
    hit_4 = arcade.check_for_collision(player, bolt_4)
    while hit_4 == True:
        print("hit")
        break
    bolt_5.update()
    hit_5 = arcade.check_for_collision(player, bolt_5)
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
