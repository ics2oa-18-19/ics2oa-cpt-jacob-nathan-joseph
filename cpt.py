import os
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

BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

current_screen = "open"

player = arcade.Sprite('shag.png', center_x=WIDTH / 15, center_y=HEIGHT / 15, scale=0.2)
player_title = arcade.Sprite('shag.png', center_x=WIDTH / 2, center_y=HEIGHT / 1.7, scale=0.5)
you_died = arcade.Sprite('death.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=2.6)
the_end = arcade.Sprite('end.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)

start_y = 220
start_x = 300

button5 = [204, 130, 200, 50, False, arcade.color.ANTI_FLASH_WHITE, arcade.color.ANTI_FLASH_WHITE]

herobrine_move = random.randint(1,3)
herobrine_health = 150

mine = arcade.Sprite('mine.png', center_x = 40, center_y = random.randint(265,450), scale=0.065)
mine_2 = arcade.Sprite('mine.png', center_x = 600, center_y = random.randint(265,450), scale=0.065)
mine.change_x = 10
mine_2.change_x = -10
mine.change_angle = 10
mine_2.change_angle = 10


smite = arcade.Sprite('smite.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.35)
smite.change_y = -10


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

ricardo_move = random.randint(1,3)
ricardo_health = 150

flex = arcade.Sprite('ricardo_flex.png', center_x = 40, center_y = random.randint(265,450), scale=0.5)
flex_2 = arcade.Sprite('ricardo_flex.png', center_x = 600, center_y = random.randint(265,450), scale=0.5)
flex.change_x = 10
flex_2.change_x = -10
flex.change_angle = 10
flex_2.change_angle = 10


charm = arcade.Sprite('ricardo_charm.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.13)
charm.change_y = -10



milos = arcade.Sprite('ricardo_ricardo.png', center_x= random.randint(1,640)
, center_y =HEIGHT, scale=0.1)

milos.change_y = -10

button1 = [22, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button2 = [184, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button3 = [353, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button4 = [518, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]

button11 = [22, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button12 = [184, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button13 = [353, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button14 = [518, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]

health = 120

fight = arcade.Sprite('fight.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=1)

n = 1

def update(delta_time):
    global current_screen, up_pressed, player_y, herobrine_health, health, ricardo_health

    if current_screen == "movement" or "movement2" or "movement3":
        if up_pressed == True:
            player.center_y += 8
        if down_pressed == True:
            player.center_y -= 8
        if left_pressed == True:
            player.center_x -= 8
        if right_pressed == True:
            player.center_x += 8
        if player.center_x > 620:
            player.center_x -= 5
        if player.center_x < 20:
            player.center_x += 5
        if player.center_y > 415:
            player.center_y -= 5
        if player.center_y < 20:
            player.center_y += 5


    if current_screen == "movement":
        if player.center_x > 600 and player.center_y > 400:
            current_screen = "boss_one"
        health = 120

    if current_screen == "movement2":
        if player.center_x > 600 and player.center_y > 400:
            current_screen = "boss_two"
        health = 120

    if current_screen == "boss_one":
        if up_pressed == True:
            player.center_y += 7
        if down_pressed == True:
            player.center_y -= 7
        if left_pressed == True:
            player.center_x -= 7
        if right_pressed == True:
            player.center_x += 7
        if player.center_x > 640:
            player.center_x -= 20
        if player.center_x < 20:
            player.center_x += 20
        if player.center_y > 450:
            player.center_y -= 20
        if player.center_y < 150:
            player.center_y += 20

        if button1[BTN_IS_CLICKED]:
            herobrine_health -= 2.5

        if button2[BTN_IS_CLICKED]:
            health += 0.7

        mine.update()

        mine_hit = arcade.check_for_collision(player, mine)
        while mine_hit == True:
            health -= 1
            break
        mine_2.update()
        mine_hit_2 = arcade.check_for_collision(player, mine_2)
        while mine_hit_2 == True:
            health -= 1
            break

        smite.update()
        smite_hit = arcade.check_for_collision(player, smite)
        while smite_hit == True:
            health -= 1
            break
        bolt.update()
        hit = arcade.check_for_collision(player, bolt)
        while hit == True:
            health -= 2
            break
        bolt_2.update()
        hit_2 = arcade.check_for_collision(player, bolt_2)
        while hit_2 == True:
            health -= 2
            break
        bolt_3.update()
        hit_3 = arcade.check_for_collision(player, bolt_3)
        while hit_3 == True:
            health -= 2
            break
        bolt_4.update()
        hit_4 = arcade.check_for_collision(player, bolt_4)
        while hit_4 == True:
            break
        bolt_5.update()
        hit_5 = arcade.check_for_collision(player, bolt_5)
        while hit_5 == True:
            health -= 2
            break

        if health < 0:
            current_screen = "death"
        if herobrine_health < 0:
            current_screen = "movement2"

    if current_screen == "boss_two":
        if up_pressed == True:
            player.center_y += 7
        if down_pressed == True:
            player.center_y -= 7
        if left_pressed == True:
            player.center_x -= 7
        if right_pressed == True:
            player.center_x += 7
        if player.center_x > 640:
            player.center_x -= 20
        if player.center_x < 20:
            player.center_x += 20
        if player.center_y > 450:
            player.center_y -= 20
        if player.center_y < 150:
            player.center_y += 20

        if button11[BTN_IS_CLICKED]:
            ricardo_health -= 2.5

        if button12[BTN_IS_CLICKED]:
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
            break

        charm.update()
        charm_hit = arcade.check_for_collision(player, charm)
        while charm_hit == True:
            health -= 1
            break
        milos.update()
        hit = arcade.check_for_collision(player, milos)
        while hit == True:
            health -= 2
            break
        if health < 0:
            current_screen = "death"
        elif ricardo_health < 0:
            current_screen = "movement3"

def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "open":
        draw_open()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "death":
        draw_death()
    elif current_screen == "final":
        draw_final()
    elif current_screen == "movement":
        draw_movement()
    elif current_screen == "movement2":
        draw_movement2()
    elif current_screen == "movement3":
        draw_movement3()
    elif current_screen == "boss_one":
        draw_boss_one()
    elif current_screen == "boss_two":
        draw_boss_two()
def on_key_press(key, modifiers):
    global current_screen, up_pressed, down_pressed, right_pressed, left_pressed

    if current_screen == "open":
        if key == arcade.key.ESCAPE:
            exit()
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "open"
        if key == arcade.key.ENTER:
            current_screen = "movement"
    elif current_screen == "movement" or "movement2" or "movement3":
        if key == arcade.key.ESCAPE:
            current_screen = "open"
    elif current_screen == "death":
        if key == arcade.key.ESCAPE:
            current_screen = "open"
    elif current_screen == "final":
        if key == arcade.key.ESCAPE:
            current_screen = "open"

    if current_screen == "movement" or "movement2" or "movement3":
        if key == arcade.key.W:
            up_pressed = True

        if key == arcade.key.S:
            down_pressed = True

        if key == arcade.key.D:
            right_pressed = True

        if key == arcade.key.A:
            left_pressed = True

    if current_screen == "boss_one" or "boss_two" or "boss_three":
        if key == arcade.key.W:
            up_pressed = True

        if key == arcade.key.S:
            down_pressed = True

        if key == arcade.key.D:
            right_pressed = True

        if key == arcade.key.A:
            left_pressed = True

def on_key_release(key, modifiers):
    global current_screen, up_pressed, down_pressed, left_pressed, right_pressed
    if current_screen == "movement" or "movement2" or "movement3":
        if key == arcade.key.W:
            up_pressed = False

        if key == arcade.key.S:
            down_pressed = False

        if key == arcade.key.D:
            right_pressed = False

        if key == arcade.key.A:
            left_pressed = False
    if current_screen == "boss_one" or "boss_two" or "boss_three":
        if key == arcade.key.W:
            up_pressed = False

        if key == arcade.key.S:
            down_pressed = False

        if key == arcade.key.D:
            right_pressed = False

        if key == arcade.key.A:
            left_pressed = False

def on_mouse_press(x, y, button, modifiers):
    global current_screen

    if current_screen == "open":
        if mouse_is_over(x, y, button5):
            button5[BTN_IS_CLICKED] = True
            current_screen = "instructions"

    if current_screen == "boss_one":
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
    if current_screen == "boss_two":
        if (x > button11[BTN_X] and x < button11[BTN_X] + button11[BTN_WIDTH] and
                y > button11[BTN_Y] and y < button11[BTN_Y] + button11[BTN_HEIGHT]):
            button11[BTN_IS_CLICKED] = True

        if (x > button12[BTN_X] and x < button12[BTN_X] + button12[BTN_WIDTH] and
                y > button12[BTN_Y] and y < button12[BTN_Y] + button12[BTN_HEIGHT]):
            button12[BTN_IS_CLICKED] = True
        if (x > button13[BTN_X] and x < button13[BTN_X] + button13[BTN_WIDTH] and
                y > button13[BTN_Y] and y < button13[BTN_Y] + button13[BTN_HEIGHT]):
            button13[BTN_IS_CLICKED] = True
        if (x > button14[BTN_X] and x < button14[BTN_X] + button14[BTN_WIDTH] and
                y > button14[BTN_Y] and y < button14[BTN_Y] + button14[BTN_HEIGHT]):
            button14[BTN_IS_CLICKED] = True
def on_mouse_release(x, y, button, modifiers):
    global current_screen

    if current_screen == "open":
        button5[BTN_IS_CLICKED] = False

    if current_screen == "boss_one":
        button1[BTN_IS_CLICKED] = False

        button2[BTN_IS_CLICKED] = False

        button3[BTN_IS_CLICKED] = False

        button4[BTN_IS_CLICKED] = False

    if current_screen == "boss_two":
        button11[BTN_IS_CLICKED] = False

        button12[BTN_IS_CLICKED] = False

        button13[BTN_IS_CLICKED] = False

        button14[BTN_IS_CLICKED] = False
def draw_button(button):
    if button[BTN_IS_CLICKED]:
        color = button[BTN_CLICKED_COLOR]
    else:
        color = button[BTN_COLOR]

    arcade.draw_xywh_rectangle_filled(button[BTN_X],
                                      button[BTN_Y],
                                      button[BTN_WIDTH],
                                      button[BTN_HEIGHT],
                                      color)


def mouse_is_over(x, y, button):
    if (x > button[BTN_X] and x < button[BTN_X] + button[BTN_WIDTH] and
            y > button[BTN_Y] and y < button[BTN_Y] + button[BTN_HEIGHT]):
        return True
    else:
        return False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def draw_open():
    arcade.set_background_color(arcade.color.LIGHT_KHAKI)
    arcade.draw_xywh_rectangle_filled(194, 120, 220, 70, arcade.color.BLACK)
    player_title.draw()
    draw_button(button5)
    arcade.draw_text("Welcome to Shaggy's Adventures!", start_x, start_y, arcade.color.BLACK, 14, width=800,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("Press to Play", start_x, 155, arcade.color.BLACK, 10,
                     width=800,
                     align="center",
                     anchor_x="center", anchor_y="center")


def draw_instructions():
    arcade.set_background_color(arcade.color.LIGHT_KHAKI)
    arcade.draw_text("Instructions", start_x, 400, arcade.color.BLACK, 35, width=400,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("You will play as 'Shaggy' and fight 3 bosses", start_x, 350, arcade.color.BLACK, 10, width=800,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text(
        "Spam attack and heal buttons while you fight the boss", start_x,
        300, arcade.color.BLACK, 10, width=800,
        align="center",
        anchor_x="center", anchor_y="center")
    arcade.draw_text("You will have 100 health each fight. You can dodge to avoid damage", start_x, 250, arcade.color.BLACK, 10,
                     width=800,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("If you die, you will lose all your progress and return to the opening screen", start_x, 200,
                     arcade.color.BLACK, 10, width=800,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("Use 'WASD' Keys to move around in the movement screens", start_x, 150, arcade.color.BLACK, 10,
                     width=800,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("Press 'ESC' to return to the opening screen", 140, 10, arcade.color.BLACK, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")
    arcade.draw_text("Press 'ENTER' to fight your first boss", 520, 10, arcade.color.BLACK, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")


def draw_movement():
    arcade.set_background_color(arcade.color.DARTMOUTH_GREEN)
    arcade.draw_rectangle_filled(10, 10, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(640, 480, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(120, 10, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(160, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(240, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(360, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(480, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(480, 360, 120, 400, arcade.color.HELIOTROPE_GRAY)
    player.draw()
    arcade.draw_text("Walk to the end of the path", 560, 10, arcade.color.BLACK, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")

def draw_movement2():
    arcade.set_background_color(arcade.color.DARTMOUTH_GREEN)
    arcade.draw_rectangle_filled(10, 10, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(640, 480, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(120, 10, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(160, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(240, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(360, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(480, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(480, 360, 120, 400, arcade.color.HELIOTROPE_GRAY)
    player.draw()
    arcade.draw_text("Walk to the end of the path", 560, 10, arcade.color.BLACK, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")

def draw_movement3():
    arcade.set_background_color(arcade.color.DARTMOUTH_GREEN)
    arcade.draw_rectangle_filled(10, 10, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(640, 480, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(120, 10, 200, 200, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(160, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(240, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(360, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(480, 170, 120, 120, arcade.color.HELIOTROPE_GRAY)
    arcade.draw_rectangle_filled(480, 360, 120, 400, arcade.color.HELIOTROPE_GRAY)
    player.draw()
    arcade.draw_text("Walk to the end of the path", 560, 10, arcade.color.BLACK, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")

def draw_death():
    you_died.draw()
    arcade.draw_text("Press 'ESC' to return to the opening screen", 140, 10, arcade.color.RED, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")


def draw_final():
    arcade.set_background_color(arcade.color.LIGHT_KHAKI)
    the_end.draw()
    arcade.draw_text("Press 'ESC' to return to the opening screen", 140, 10, arcade.color.BLACK, 10, width=300,
                     align="center",
                     anchor_x="center", anchor_y="center")


def draw_boss_one():
    fight.draw()
    player.draw()
    mine.draw()
    mine_2.draw()
    smite.draw()
    bolt.draw()
    bolt_2.draw()
    bolt_3.draw()
    bolt_4.draw()
    bolt_5.draw()
    if mine.center_x == 600:
        mine.change_x = -10
        mine.center_y = random.randint(265, 450)
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
        smite.center_x = random.randint(1, 640)
    if bolt.center_y == 160:
        bolt.center_y += HEIGHT
        bolt.center_x = random.randint(1, 640)
    if bolt_2.center_y == 160:
        bolt_2.center_y += HEIGHT
        bolt_2.center_x = random.randint(1, 640)
    if bolt_3.center_y == 160:
        bolt_3.center_y += HEIGHT
        bolt_3.center_x = random.randint(1, 640)
    if bolt_4.center_y == 160:
        bolt_4.center_y += HEIGHT
        bolt_4.center_x = random.randint(1, 640)
    if bolt_5.center_y == 160:
        bolt_5.center_y += HEIGHT
        bolt_5.center_x = random.randint(1, 640)

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
    button5[BTN_IS_CLICKED] = False

    button1[BTN_IS_CLICKED] = False

    button2[BTN_IS_CLICKED] = False

    button3[BTN_IS_CLICKED] = False

    button4[BTN_IS_CLICKED] = False


def draw_boss_two():
    fight.draw()
    player.draw()
    flex.draw()
    flex_2.draw()
    charm.draw()
    milos.draw()

    if flex.center_x == 600:
        flex.change_x = -10
        flex.center_y = random.randint(265, 450)
    elif flex.center_x == 40:
        flex.change_x = 10
        flex.center_y = random.randint(265, 450)
    if flex_2.center_x == 40:
        flex_2.change_x = 10
        flex_2.center_y = random.randint(265, 450)
    elif flex_2.center_x == 600:
        flex_2.change_x = -10
        flex_2.center_y = random.randint(265, 450)
    if charm.center_y == 180:
        charm.center_y += HEIGHT
        charm.center_x = random.randint(1, 640)
    if milos.center_y == 160:
        milos.center_y += HEIGHT
        milos.center_x = random.randint(1, 640)

    arcade.draw_xywh_rectangle_filled(220, 50, health * 2, 20, arcade.color.GREEN)
    arcade.draw_xywh_rectangle_filled(160, 90, ricardo_health * 2, 20, arcade.color.RED)

    if button11[BTN_IS_CLICKED]:
        color = button11[BTN_CLICKED_COLOR]
    else:
        color = button11[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button11[BTN_X], button11[BTN_Y], button11[BTN_WIDTH], button11[BTN_HEIGHT],
                                      color)

    if button12[BTN_IS_CLICKED]:
        color = button12[BTN_CLICKED_COLOR]
    else:
        color = button12[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button12[BTN_X], button12[BTN_Y], button12[BTN_WIDTH], button12[BTN_HEIGHT],
                                      color)

    if button13[BTN_IS_CLICKED]:
        color = button13[BTN_CLICKED_COLOR]
    else:
        color = button13[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button13[BTN_X], button13[BTN_Y], button13[BTN_WIDTH], button13[BTN_HEIGHT],
                                      color)

    if button14[BTN_IS_CLICKED]:
        color = button14[BTN_CLICKED_COLOR]
    else:
        color = button14[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button14[BTN_X], button14[BTN_Y], button14[BTN_WIDTH], button14[BTN_HEIGHT],
                                      color)
    button11[BTN_IS_CLICKED] = False

    button12[BTN_IS_CLICKED] = False

    button13[BTN_IS_CLICKED] = False

    button14[BTN_IS_CLICKED] = False
#def draw_boss_three():

if __name__ == '__main__':
    setup()
