from picamera import PiCamera
from LEDArray import allLEDOn
import time
if __name__ == '__main__':
    with PiCamera() as camera:
        allLEDOn()
        camera.zoom = (0.45,0.45,0.2,0.2)
        camera.sharpness = 100
        camera.shutter_speed = 10000
        camera.contrast = 100
        camera.ISO = 100
        camera.start_preview()
        while True:
            pass
        camera.stop_preview()