import json
from random import randint
import numpy as np

def appendZoom(mainArray):
    tmpA = []
    for element in mainArray:
        for x in range(45,55,10):
            for y in range(10,20,10):
                tmp = element.copy()
                tmp.append([(x/100,x/100,y/100,y/100)])
                tmpA.append(tmp)
    return tmpA
def initWithResolution():
    tmpR = []
    for i in [
        #"640x480",
        #"720x576",
        #"1024x576",
        #"1280x720",
        "1920x1080"
        ]:
        tmpR.append([i])
    return tmpR
def appendContrast(mainArray):
    tmpR = []
    for element in mainArray:
        for i in range(100,90,-10):
            tmp = element.copy()
            tmp.append(i)
            tmpR.append(tmp)
    return tmpR
def appendISO(mainArray):
    tmpR = []
    for element in mainArray:
        for i in range(100,150,50):
            tmp = element.copy()
            tmp.append(i)
            tmpR.append(tmp)
    return tmpR
def appendSharpness(mainArray):
    tmpR = []
    for elements in mainArray:
        for i in range(100,95,-5):
            tmp = elements.copy()
            tmp.append(i)
            tmpR.append(tmp)
    return tmpR
def appendCBrightness(mainArray):
    tmpR = []
    for element in mainArray:
        for i in range(100,95,-5):
            tmp = element.copy()
            tmp.append(i)
            tmpR.append(tmp)
    return tmpR

def generateLEDArray():
    LEDArray = []
    LED = []
    idOnOne = 0
    idOnZero = 50
    for y in range(8):
        LEDx = []
        for x in range(8):
            LEDx.append(1)
        LED.append(LEDx)
    LEDArray.append(LED)
    if idOnOne != 0:
        for element in range(idOnOne):
            LEDArray.append(LED.copy())
        LEDx = []
        for i in range(8):
            LEDx.append(0)

        for i in range(1,idOnOne+1,1):
            LEDArray[i][i-1] = LEDx.copy()
    if idOnZero != 0:
        for i in range(idOnZero):
            LED = []
            for y in range(8):
                LEDx = []
                for x in range(8):
                    LEDx.append(0)
                LED.append(LEDx)
            LEDArray.append(LED.copy())
        for i in range(idOnOne+1,idOnOne+idOnZero+1,1):
            for j in range(randint(20,30)):
                LEDArray[i][randint(0,7)][randint(0,7)] = 1
    return LEDArray
def appendLEDArray(mainArray):
    tmpR = []
    for element in mainArray:
        for i in generateLEDArray():
            tmp = element.copy()
            tmp.append(i)
            tmpR.append(tmp)
    return tmpR

def appendShutterSpeed(mainArray):
    exposures = np.array([60000, 60000, 60000, 60000, 60000, 60000, 60000, 60000])
    tmpr = []
    for element in mainArray:
        for i in range(8000,12000,500):
            tmp = element.copy()
            tmp.append(6000)
            tmpr.append(tmp)
    return tmpr

if __name__=="__main__":
    # Immer zuerst initXYZ
    # Reihenfolge sonst egal
    # Jede Methode in dictList ergänzen -> Dort ist die Reihenfolge wichtig
    mainArray = \
    appendShutterSpeed(
        #appendLEDArray(
            appendCBrightness(
                appendSharpness(
                    appendISO(
                        appendContrast(
                            initWithResolution()
                        )
                    )
                )
            )
        #)
    )
    print(len(mainArray))
    mainDict = {}
    dictList = [
        #"Zoom",
        "Resolution",
        "Contrast",
        "ISO",
        "Sharpness",
        "cBrightness",
        #"LEDArray",
        "ShutterSpeed"
    ]
    i = 0
    for e in mainArray:
        tmpDict = dict((dictList[i],e[i]) for i in range(len(dictList)))
        mainDict[str(i)] = tmpDict
        i = i + 1
    with open("../Mikroskop/config_file.json","w") as file:
        json.dump(json.dumps(mainDict),file)
