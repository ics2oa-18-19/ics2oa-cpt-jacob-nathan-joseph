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

player = arcade.Sprite('images/shagstill.png', center_x=WIDTH / 15, center_y=HEIGHT / 15, scale=0.2)
player_title = arcade.Sprite('images/shagstill.png', center_x=WIDTH / 2, center_y= 350, scale=0.5)
you_died = arcade.Sprite('images/death.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=2.6)
the_end = arcade.Sprite('images/end.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)

start_y = 220
start_x = 300

button5 = [204, 130, 200, 50, False, arcade.color.ANTI_FLASH_WHITE, arcade.color.ANTI_FLASH_WHITE]

herobrine = arcade.Sprite('images/herobrine.png', center_x = 600, center_y = 410, scale = 0.1)

herobrine_move = random.randint(1, 3)
herobrine_health = 80
shaggy = arcade.Sprite('images/shaggy.png', center_x = 530, center_y = 350, scale = 0.8)
mine = arcade.Sprite('images/herobrine_mine.png', center_x=40, center_y=random.randint(265, 450), scale=0.065)
mine_2 = arcade.Sprite('images/herobrine_mine.png', center_x=600, center_y=random.randint(265, 450), scale=0.065)
mine.change_x = 5
mine_2.change_x = -5
mine.change_angle = 5
mine_2.change_angle = 5

smite = arcade.Sprite('images/herobrine_smite.png', center_x=random.randint(1, 640)
                      , center_y=HEIGHT + 300, scale=0.35)
smite.change_y = -3

bolt = arcade.Sprite('images/herobrine_bolt.png', center_x=random.randint(1, 640)
                     , center_y=HEIGHT, scale=0.08)
bolt_2 = arcade.Sprite('images/herobrine_bolt.png', center_x=random.randint(1, 640)
                       , center_y=HEIGHT, scale=0.08)
bolt_3 = arcade.Sprite('images/herobrine_bolt.png', center_x=random.randint(1, 640)
                       , center_y=HEIGHT, scale=0.08)
bolt_4 = arcade.Sprite('images/herobrine_bolt.png', center_x=random.randint(1, 640)
                       , center_y=HEIGHT, scale=0.08)
bolt_5 = arcade.Sprite('images/herobrine_bolt.png', center_x=random.randint(1, 640)
                       , center_y=HEIGHT, scale=0.08)
bolt.change_y = -4
bolt_2.change_y = -4
bolt_3.change_y = -4
bolt_4.change_y = -4
bolt_5.change_y = -4

ricardo = arcade.Sprite('images/ricardo_milos.png', center_x=600
                        , center_y=440, scale=0.1)

ricardo_move = random.randint(1, 3)
ricardo_health = 70

flex = arcade.Sprite('images/ricardo_flex.png', center_x=40, center_y=random.randint(265, 450), scale=0.3)
flex_2 = arcade.Sprite('images/ricardo_flex.png', center_x=600, center_y=random.randint(265, 450), scale=0.3)
flex.change_x = 10
flex_2.change_x = -10
flex.change_angle = 5
flex_2.change_angle = 5

charm = arcade.Sprite('images/ricardo_charm.png', center_x=random.randint(1, 640)
                      , center_y=HEIGHT + 300, scale=0.13)
charm.change_y = -4

milos = arcade.Sprite('images/ricardo_milos2.png', center_x=random.randint(1, 640)
                      , center_y=HEIGHT, scale=0.4)

milos.change_y = -6

peter = arcade.Sprite('images/peter_sans.png', center_x = 585
                      ,center_y = 420, scale = 0.1)

sans_move = random.randint(1,3)
sans_health = 90

cock = arcade.Sprite('images/sans_cock.png', center_x = 40, center_y = random.randint(265,450), scale=0.12)
cock_2 = arcade.Sprite('images/sans_cock.png', center_x = 600, center_y = random.randint(265,450), scale=0.12)
cock.change_x = 3
cock_2.change_x = -3
cock.change_angle = 10
cock_2.change_angle = 10
cock_pos_1 = random.randint(265,450)
cock_pos_2 = random.randint(265,450)


bone = arcade.Sprite('images/sans_bone.png', center_x = random.randint(1,640)
, center_y = HEIGHT + 300, scale=0.35)
bone_2 = arcade.Sprite('images/sans_bone2.png', center_x = 700
, center_y = random.randint(100,640), scale=0.35)
bone.change_y = -5
bone_2.change_x = -5


emerald = arcade.Sprite('images/sans_master_emerald.png', center_x= random.randint(1,640)
, center_y =HEIGHT, scale=0.08)
emerald_2 = arcade.Sprite('images/sans_red_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT + 70, scale= 0.08)
emerald_3 = arcade.Sprite('images/sans_blue_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT + 140, scale= 0.08)
emerald_4 = arcade.Sprite('images/sans_white_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT + 210, scale= 0.08)
emerald_5 = arcade.Sprite('images/sans_yellow_emerald.png',center_x= random.randint(1,640)
, center_y = HEIGHT + 280, scale= 0.08)
emerald.change_y = -6
emerald_2.change_y = -6
emerald_3.change_y = -6
emerald_4.change_y = -6
emerald_5.change_y = -6
turn = random.randint(1, 2)

button1 = [22, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button2 = [184, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]


button11 = [22, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button12 = [184, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]


button21 = [22, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]
button22 = [184, 2, 115, 40, False, (0, 0, 0, 0), arcade.color.GREEN]


health = 120

fight = arcade.Sprite('images/fight.png', center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)

n = 1

def update(delta_time):
    global current_screen, up_pressed, player_y, herobrine_health, health, ricardo_health, sans_health

    if current_screen == "movement" or "movement2" or "movement3":
        if up_pressed == True:
            player.center_y += 6
        if down_pressed == True:
            player.center_y -= 6
        if left_pressed == True:
            player.center_x -= 6
        if right_pressed == True:
            player.center_x += 6
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
            current_screen = "boss_two"
        health = 120
        ricardo_health = 80

    if current_screen == "movement2":
        if player.center_x > 600 and player.center_y > 400:
            current_screen = "boss_one"
        health = 120
        herobrine_health = 80

    if current_screen == "movement3":
        if player.center_x > 600 and player.center_y > 400:
            current_screen = "boss_three"
        health = 120
        sans_health = 80

    if current_screen == "boss_one":
        if up_pressed == True:
            player.center_y += 6
        if down_pressed == True:
            player.center_y -= 6
        if left_pressed == True:
            player.center_x -= 6
        if right_pressed == True:
            player.center_x += 6
        if player.center_x > 640:
            player.center_x -= 20
        if player.center_x < 20:
            player.center_x += 20
        if player.center_y > 450:
            player.center_y -= 20
        if player.center_y < 150:
            player.center_y += 20

        if button1[BTN_IS_CLICKED]:
            herobrine_health -= 1

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
            health -= 1
            break
        bolt_2.update()
        hit_2 = arcade.check_for_collision(player, bolt_2)
        while hit_2 == True:
            health -= 1
            break
        bolt_3.update()
        hit_3 = arcade.check_for_collision(player, bolt_3)
        while hit_3 == True:
            health -= 1
            break
        bolt_4.update()
        hit_4 = arcade.check_for_collision(player, bolt_4)
        while hit_4 == True:
            break
        bolt_5.update()
        hit_5 = arcade.check_for_collision(player, bolt_5)
        while hit_5 == True:
            health -= 1
            break

        if health < 0:
            current_screen = "death"
        if herobrine_health < 0:
            current_screen = "movement3"

    if current_screen == "boss_two":
        if up_pressed == True:
            player.center_y += 6
        if down_pressed == True:
            player.center_y -= 6
        if left_pressed == True:
            player.center_x -= 6
        if right_pressed == True:
            player.center_x += 6
        if player.center_x > 640:
            player.center_x -= 20
        if player.center_x < 20:
            player.center_x += 20
        if player.center_y > 450:
            player.center_y -= 20
        if player.center_y < 150:
            player.center_y += 20

        if button11[BTN_IS_CLICKED]:
            ricardo_health -= 1

        if button12[BTN_IS_CLICKED]:
            health += 0.7

        flex.update()

        flex_hit = arcade.check_for_collision(player, flex)
        while flex_hit == True:
            health -= 1
            break
        flex_2.update()
        flex_hit_2 = arcade.check_for_collision(player, flex_2)
        while flex_hit_2 == True:
            health -= 1
            break

        charm.update()
        charm_hit = arcade.check_for_collision(player, charm)
        while charm_hit == True:
            health -= 5
            break
        milos.update()
        hit = arcade.check_for_collision(player, milos)
        while hit == True:
            health -= 2
            break
        if health < 0:
            current_screen = "death"
        if ricardo_health < 0:
            current_screen = "movement2"

    if current_screen == "boss_three":
        if up_pressed == True:
            player.center_y += 6
        if down_pressed == True:
            player.center_y -= 6
        if left_pressed == True:
            player.center_x -= 6
        if right_pressed == True:
            player.center_x += 6
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

        if button21[BTN_IS_CLICKED]:
            sans_health -= 1

        if button22[BTN_IS_CLICKED]:
            health += 0.5

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
            break
        bone.update()
        bone_hit = arcade.check_for_collision(player, bone)
        while bone_hit == True:
            health -= 1
            break
        bone_2.update()
        bone_hit_2 = arcade.check_for_collision(player, bone_2)
        while bone_hit_2 == True:
            health -= 1
            break
        emerald.update()
        hit = arcade.check_for_collision(player, emerald)
        while hit == True:
            health -= 2
            break
        emerald_2.update()
        hit_2 = arcade.check_for_collision(player, emerald_2)
        while hit_2 == True:
            health -= 2
            break
        emerald_3.update()
        hit_3 = arcade.check_for_collision(player, emerald_3)
        while hit_3 == True:
            health -= 2
            break
        emerald_4.update()
        hit_4 = arcade.check_for_collision(player, emerald_4)
        while hit_4 == True:
            break
        emerald_5.update()
        hit_5 = arcade.check_for_collision(player, emerald_5)
        while hit_5 == True:
            health -= 2
            break
        if health < 0:
            current_screen = "death_screen"
        if sans_health < 0:
            current_screen = "final"

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
        herobrine.draw()
    elif current_screen == "boss_two":
        draw_boss_two()
        ricardo.draw()
    elif current_screen == "boss_three":
        draw_boss_three()
        peter.draw()


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

    if current_screen == "boss_two":
        if (x > button11[BTN_X] and x < button11[BTN_X] + button11[BTN_WIDTH] and
                y > button11[BTN_Y] and y < button11[BTN_Y] + button11[BTN_HEIGHT]):
            button11[BTN_IS_CLICKED] = True

        if (x > button12[BTN_X] and x < button12[BTN_X] + button12[BTN_WIDTH] and
                y > button12[BTN_Y] and y < button12[BTN_Y] + button12[BTN_HEIGHT]):
            button12[BTN_IS_CLICKED] = True

    if current_screen == "boss_three":

        if (x > button21[BTN_X] and x < button21[BTN_X] + button21[BTN_WIDTH] and
                y > button21[BTN_Y] and y < button21[BTN_Y] + button21[BTN_HEIGHT]):
            button21[BTN_IS_CLICKED] = True
        if (x > button22[BTN_X] and x < button22[BTN_X] + button22[BTN_WIDTH] and
                y > button22[BTN_Y] and y < button22[BTN_Y] + button22[BTN_HEIGHT]):
            button22[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    global current_screen

    if current_screen == "open":
        button5[BTN_IS_CLICKED] = False

    if current_screen == "boss_one":
        button1[BTN_IS_CLICKED] = False

        button2[BTN_IS_CLICKED] = False



    if current_screen == "boss_two":
        button11[BTN_IS_CLICKED] = False

        button12[BTN_IS_CLICKED] = False

    if current_screen == "boss_three":
        button21[BTN_IS_CLICKED] = False
        button22[BTN_IS_CLICKED] = False

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
    for i in range(1):
        shaggy.draw()
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
    arcade.draw_text("You will have 100 health each fight. You can dodge to avoid damage", start_x, 250,
                     arcade.color.BLACK, 10,
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



    button5[BTN_IS_CLICKED] = False

    button1[BTN_IS_CLICKED] = False

    button2[BTN_IS_CLICKED] = False




def draw_boss_two():
    fight.draw()
    player.draw()
    flex.draw()
    flex_2.draw()
    charm.draw()
    milos.draw()

    if flex.center_x == 670:
        flex.change_x = -10
        flex.center_y = random.randint(100, 450)
    elif flex.center_x == -30:
        flex.change_x = 10
        flex.center_y = random.randint(100, 450)
    if flex_2.center_x == -30:
        flex_2.change_x = 10
        flex_2.center_y = random.randint(100, 450)
    elif flex_2.center_x == 670:
        flex_2.change_x = -10
        flex_2.center_y = random.randint(100, 450)
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


    button11[BTN_IS_CLICKED] = False

    button12[BTN_IS_CLICKED] = False



def draw_boss_three():
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
        cock.center_y = random.randint(100,450)
    elif cock.center_x == 40:
        cock.change_x = 10
        cock.center_y = random.randint(100, 450)
    if cock_2.center_x == 40:
        cock_2.change_x = 10
        cock_2.center_y = random.randint(100, 450)
    elif cock_2.center_x == 600:
        cock_2.change_x = -10
        cock_2.center_y = random.randint(100, 450)
    if bone.center_y == -20:
        bone.center_y += HEIGHT
        bone.center_x = random.randint(1,640)
    if bone_2.center_x == -20:
        bone_2.center_x += WIDTH
        bone_2.center_y = random.randint(1,640)
    if emerald.center_y == 100:
        emerald.center_y += HEIGHT
        emerald.center_x = random.randint(1,640)
    if emerald_2.center_y == 100:
        emerald_2.center_y += HEIGHT
        emerald_2.center_x = random.randint(1,640)
    if emerald_3.center_y == 100:
        emerald_3.center_y += HEIGHT
        emerald_3.center_x = random.randint(1,640)
    if emerald_4.center_y == 100:
        emerald_4.center_y += HEIGHT
        emerald_4.center_x = random.randint(1,640)
    if emerald_5.center_y == 100:
        emerald_5.center_y += HEIGHT
        emerald_5.center_x = random.randint(1,640)

    arcade.draw_xywh_rectangle_filled(220, 50, health * 2, 20, arcade.color.GREEN)
    arcade.draw_xywh_rectangle_filled(160, 90, sans_health * 2, 20, arcade.color.RED)
    if button21[BTN_IS_CLICKED]:
        color = button21[BTN_CLICKED_COLOR]
    else:
        color = button21[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button21[BTN_X], button21[BTN_Y], button21[BTN_WIDTH], button21[BTN_HEIGHT],
                                      color)
    if button22[BTN_IS_CLICKED]:
        color = button22[BTN_CLICKED_COLOR]
    else:
        color = button22[BTN_COLOR]
    arcade.draw_xywh_rectangle_filled(button22[BTN_X], button22[BTN_Y], button22[BTN_WIDTH], button22[BTN_HEIGHT],
                                      color)

    button21[BTN_IS_CLICKED] = False
    button22[BTN_IS_CLICKED] = False


if __name__ == '__main__':
    setup()
