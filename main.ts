let countdown = 0
let firework: game.LedSprite = null
input.onButtonPressed(Button.B, function () {
    countdown = 3
    while (countdown >= 0) {
        basic.showNumber(countdown)
        basic.pause(100)
        countdown += -1
    }
    firework = game.createSprite(2, 4)
    basic.pause(500)
    for (let index = 0; index < 3; index++) {
        basic.pause(100)
        firework.change(LedSpriteProperty.Y, -1)
    }
    firework.delete()
    basic.pause(500)
    led.plot(2, 2)
    led.unplot(2, 2)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Target)
    basic.showIcon(IconNames.Diamond)
})
