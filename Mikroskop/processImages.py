from LEDArray import ledArrayOn, allLEDOn
import time
from picamera import PiCamera,array
import picamera
import os
import shutil
import numpy as np
import cv2
from PIL import Image
import json


if __name__=="__main__":
    storage = np.zeros((2464, 3280, 8))
    with open("config_file.json","r") as file:
        config = json.loads(json.load(file))
    j = 0
    with PiCamera() as camera:
        camera.framerate = 5
        camera.shutter_speed = 6000
        t = int(time.time())
        os.mkdir("./images/configs/"+str(t)+"/")
        camera.start_preview()
        for i in range(len(config)):
            jetzt = time.time()
            #camera.zoom = config[str(i)]["Zoom"]
            camera.resolution = config[str(i)]["Resolution"]
            camera.contrast = config[str(i)]["Contrast"]
            camera.ISO = config[str(i)]["ISO"]
            camera.sharpness = config[str(i)]["Sharpness"]
            camera.brightness = config[str(i)]["cBrightness"]
            #ledArrayOn(config[str(i)]["LEDArray"])
            allLEDOn()
            camera.shutter_speed = config[str(i)]["ShutterSpeed"]
            #camera.color_effects = (128,128)
            with picamera.array.PiBayerArray(camera) as stream:
                if i%12==0 and j>8:
                    storage[:,:,j] = stream.array
                    j=j+1
                camera.capture(stream,"jpeg",bayer=True)
                #camera.capture("./images/configs/"+str(t)+"/"+str(int(i))+".png")
                #>> 2
                output = (stream.demosaic()>>2).astype(np.uint8)
                cv2.imwrite("./images/configs/"+str(t)+"/"+str(int(i))+".tif",output)
                print("Dauer: "+str(time.time()-jetzt))

        camera.stop_preview()
