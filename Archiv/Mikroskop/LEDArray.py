import unicornhat as unicorn
def getColorList():
    colorList = {
        "weis"  : (255, 255, 255),
        "gruen" : (0, 255, 0),
        "rot"   : (255,0,0),
        "lila"  : (255,0,255),
        "blau"  : (0,0,255),
        "gelb"  : (255,255,0),
        "hellblau" : (0,255,255),
    }
    return colorList

def ledArrayOn(LEDArray,color="weis"):
    unicorn.brightness(0.3)
    colorList = getColorList()
    width,height = unicorn.get_shape()
    for x in range(width):
        for y in range(height):
            if LEDArray[x][y] == 1:
                unicorn.set_pixel(x,y,colorList[color])
            else:
                unicorn.set_pixel(x,y,(0,0,0))
            unicorn.show()
def allLEDOn(color="weis"):
    unicorn.brightness(0.2)
    colorList = getColorList()
    width, height = unicorn.get_shape()
    for x in range(width):
        for y in range(height):
            unicorn.set_pixel(x, y, colorList[color])
            unicorn.show()
def allLEDOnList(list):
    unicorn.brightness(0.2)
    colorList = getColorList()
    width, height = unicorn.get_shape()
    print(list)
    for x in range(width):
        for y in range(height):
            unicorn.set_pixel(x, y, list)
            unicorn.show()