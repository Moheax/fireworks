countdown = 0
firework: game.LedSprite = None

def on_button_pressed_b():
    global countdown, firework
    countdown = 2
    while countdown >= 0:
        basic.show_number(countdown)
        basic.pause(100)
        countdown += -1
    firework = game.create_sprite(2, 4)
    basic.pause(500)
    for index in range(4):
        basic.pause(100)
        firework.change(LedSpriteProperty.Y, -1)
    firework.delete()
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . # .
        """, 80)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """, 80)
    basic.show_leds("""
        . . # . .
        . . # . .
        # # . # #
        . . # . .
        . . # . .
        """, 80)
    for index2 in range(10):
        led.plot(randint(0, 4), randint(0, 4))
        led.plot(randint(0, 4), randint(0, 4))
        basic.pause(200)
input.on_button_pressed(Button.B, on_button_pressed_b)
