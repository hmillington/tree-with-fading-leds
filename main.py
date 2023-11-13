def dim(led2: number):
    pass
range2: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 6, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
list2: List[number] = []
list2.append(neopixel.colors(NeoPixelColors.RED))
list2.append(neopixel.colors(NeoPixelColors.ORANGE))
list2.append(neopixel.colors(NeoPixelColors.YELLOW))
list2.append(neopixel.colors(NeoPixelColors.GREEN))
list2.append(neopixel.colors(NeoPixelColors.BLUE))
list2.append(neopixel.colors(NeoPixelColors.INDIGO))
list2.append(neopixel.colors(NeoPixelColors.VIOLET))
list2.append(neopixel.colors(NeoPixelColors.PURPLE))
strip.set_brightness(20)

def on_forever():
    global range2
    strip.clear()
    for index in range(6):
        range2 = strip.range(index, 1)
        range2.show_color(list2[randint(0, len(list2) - 1)])
    basic.pause(1000)
basic.forever(on_forever)
