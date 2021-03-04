from PIL import Image
import os
import time

def zuschneiden(path="./configs/",rootPath="../Mikroskop/images/configs/"):
    for elements in os.listdir(rootPath):
        if os.path.isdir(rootPath+elements):
            t = str(int(time.time()))
            os.mkdir(path + t)
            os.mkdir(path + t + "/data/")
            for element in os.listdir(rootPath+elements):
                img = Image.open(rootPath+elements+"/"+element)
                width, height = img.size
                left = 50 * width / 100
                top = 40 * height / 100
                right = 55 * width / 100
                bottom = 50 * height / 100
                img = img.crop((left,top,right,bottom)).resize((1920,1080))
                img.save(path+"/"+t+"/"+element)
                os.rename(rootPath+elements+"/"+element, path + t + "/data/" + element)
            os.rename("../Mikroskop/config_file.json","./configs/"+t+"/data/config_file.json")

if __name__ == '__main__':
    zuschneiden()