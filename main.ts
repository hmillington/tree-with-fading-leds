function dim (led2: number) {
	
}
let colour = 0
let hue = 0
let led2 = 0
let range: neopixel.Strip = null
let strip = neopixel.create(DigitalPin.P0, 6, NeoPixelMode.RGB)
strip.setBrightness(50)
let list: number[] = []
for (let n = 0; n <= 5; n++) {
    list.push(randint(0, 360))
    range = strip.range(n, 1)
    range.showColor(neopixel.hsl(list[n], 100, 50))
}
basic.forever(function () {
    led2 = randint(0, 6)
    hue = randint(0, 360)
    range = strip.range(led2, 1)
    for (let n = 0; n <= 50; n++) {
        colour = neopixel.hsl(list[led2], 100, 50 - n)
        range.showColor(colour)
        basic.pause(10)
    }
    basic.pause(1000)
    for (let n = 0; n <= 50; n++) {
        colour = neopixel.hsl(hue, 100, n)
        range.showColor(colour)
        basic.pause(10)
    }
    list[led2] = hue
    basic.pause(1000)
})
