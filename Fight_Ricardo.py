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

ricardo_move = random.randint(1,3)
ricardo_health = 150

flex = arcade.Sprite('images/ricardo_flex.png', center_x = 40, center_y = random.randint(265,450), scale=0.3)
flex_2 = arcade.Sprite('images/ricardo_flex.png', center_x = 600, center_y = random.randint(265,450), scale=0.3)
flex.change_x = 6
flex_2.change_x = -6
flex.change_angle = 10
flex_2.change_angle = 10
flex_pos_1 = random.randint(265,450)
flex_pos_2 = random.randint(265,450)


charm = arcade.Sprite('images/ricardo_charm.png', center_x = random.randint(1,640)
, center_y = 500, scale=0.07)
charm_2 = arcade.Sprite('images/ricardo_charm.png', center_x = random.randint(1,640)
, center_y = 500, scale=0.07)
charm.change_y = -7
charm_2.change_y = -7



milos = arcade.Sprite('images/ricardo_ricardo3.png',center_x = -30
, center_y = 520, scale= 0.25)

milos_2 = arcade.Sprite('images/ricardo_ricardo4.gif',center_x= 660
, center_y = 520, scale= 0.6)


milos.change_x = +6.4
milos.change_y = -5
milos_2.change_x = -6.4
milos_2.change_y = -5


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
    flex.draw()
    flex_2.draw()
    charm.draw()
    charm_2.draw()
    milos.draw()
    milos_2.draw()
    if flex.center_x == 600:
        flex.change_x = -10
        flex.center_y = random.randint(265,450)
    elif flex.center_x == 40:
        flex.change_x = 10
        flex.center_y = random.randint(265, 450)
    if flex_2.center_x == 40:
        flex_2.change_x = 10
        flex_2.center_y = random.randint(265, 450)
    elif flex_2.center_x == 600:
        flex_2.change_x = -10
        flex_2.center_y = random.randint(265, 450)
    if charm.center_y == 0:
        charm.center_y == 500
        charm.center_x = 50
    if charm_2.center_y == 0:
        charm.center_y == 500
        charm.center_x = random.randint(0, 640)
    if milos.center_y == -30:
        milos.center_y = 520
        milos.center_x = -30
    if milos_2.center_y == -30:
        milos_2.center_y = 520
        milos_2.center_x = 660

















    arcade.draw_xywh_rectangle_filled(220, 50, health * 2, 20, arcade.color.GREEN)
    arcade.draw_xywh_rectangle_filled(160, 90, ricardo_health * 2, 20, arcade.color.RED)
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
    global ricardo_health
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
        if player.center_y < 150:
         player.center_y += 20

    if button1[BTN_IS_CLICKED]:
        ricardo_health -= 0.5
        ricardo_health -= 1

    if button2[BTN_IS_CLICKED]:
        health += 0.5
        health += 0.7

    flex.update()

    flex_hit = arcade.check_for_collision(player, flex)
    while flex_hit == True:
        health -= 2
        break
    flex_2.update()
    flex_hit_2 = arcade.check_for_collision(player, flex_2)
    while flex_hit_2 == True:
        health -= 2
        print("hit")
        break
    charm.update()
    charm_hit = arcade.check_for_collision(player, charm)
    while charm_hit == True:
        print("hit")
        health -= 1
        break
    charm_2.update()
    charm_hit_2 = arcade.check_for_collision(player, charm_2)
    while charm_hit_2 == True:
        print("hit")
        health -= 1
        break
    milos.update()
    hit_3 = arcade.check_for_collision(player, milos)
    while hit_3 == True:
        print("hit")
        health -= 2
        break
    milos_2.update()
    hit_4 = arcade.check_for_collision(player, milos_2)
    while hit_4 == True:
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
