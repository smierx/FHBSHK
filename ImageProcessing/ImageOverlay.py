from PIL import Image
import numpy as np
import os
import time
#todo Pfad ändern um nicht mehr per Hand zu schieben -> sollte funktionieren
#todo Wie lösche ich aufem RSP am besten?
#todo Aus welchen Repos kann ich was klauen?
def overlay(path):
    pass

if __name__=="__main__":
    rawDict = {}
    rawImages = []
    for elements in os.listdir(os.getcwd()+"/configs/"):
        if os.path.isdir(os.getcwd()+"/configs/"+elements):
            for element in os.listdir(os.getcwd()+"/configs/"+elements):
                if not os.path.isdir(os.getcwd()+"/configs/"+elements+"/"+element):
                    rawImages.append(os.getcwd()+"/configs/"+elements+"/"+element)
            rawDict[elements] = rawImages


    imgDict = {}
    for elements in rawDict:
        imgArray = []
        k = len(rawDict[elements])%10
        for j in range(0,len(rawDict[elements])-k,10):
            img = []
            for i in range(10):
                img.append(np.asarray(Image.open(rawDict[elements][j+i]).convert('RGB')))
            imgArray.append(img)
        imgDict[elements] = imgArray
    #-------------------------------------------------
    for elements in imgDict:
        if not os.path.exists(os.getcwd()+"/configs/"+elements+"/Overlay1/"):
            os.mkdir(os.getcwd()+"/configs/"+elements+"/Overlay1/")
            for img in imgDict[elements]:
                newImg = []
                for row in range(len(img[0])):
                    for i in range(len(img)):
                        newImg.append(img[i][row])

                image = Image.fromarray(np.asarray(newImg))
                image.save(os.getcwd()+"/configs/"+elements+"/Overlay1/"+str(time.time())+".jpg")
        if not os.path.exists(os.getcwd() + "/configs/" + elements + "/Overlay2/"):
            os.mkdir(os.getcwd() + "/configs/" + elements + "/Overlay2/")
            for img in imgDict[elements]:
                newImg = []
                for row in range(len(img[0])):
                    newImgRow = []
                    for cell in range(len(img[0][0])):
                        for i in range(len(img)):
                            newImgRow.append(img[i][row][cell])

                    newImg.append(newImgRow)
                image = Image.fromarray(np.asarray(newImg))
                image.save(os.getcwd()+"/configs/"+elements+"/Overlay2/"+str(time.time())+".jpg")
        if not os.path.exists(os.getcwd()+"/configs/"+elements+"/Overlay3/"):

            # Anzahl der jeweiligen Elemente passen nicht
            # 3 ca. 15 Elemente
            # 5 3 Elemente?!
            os.mkdir(os.getcwd()+"/configs/"+elements+"/Overlay3/")
            """
            imgHochArray = []
            imgBreitArray = []
            for element in os.listdir(os.getcwd()+"/configs/"+elements+"/Overlay2/"):
                imgBreitArray.append(np.asarray(Image.open(os.getcwd()+"/configs/"+elements+"/Overlay2/"+element)))
            for element in os.listdir(os.getcwd()+"/configs/"+elements+"/Overlay1/"):
                imgHochArray.append(np.asarray(Image.open(os.getcwd()+"/configs/"+elements+"/Overlay1/"+element)))
            hoehenFaktor = int(len(imgHochArray[0]) / len(imgBreitArray[0]))
            breitenFaktor = int(len(imgBreitArray[0][0])/len(imgHochArray[0][0]))
            newHochImgArray = []
            for j in range(len(imgHochArray)):
                newImg = []
                for row in imgHochArray[j]:
                    newImgRow = []
                    for cell in row:
                        for i in range(breitenFaktor):
                            newImgRow.append(cell)
                    newImg.append(newImgRow.copy())
                newHochImgArray.append(newImg.copy())
            for element in newHochImgArray:
                image = Image.fromarray(np.asarray(element))
                image.save(os.getcwd() + "/configs/" + elements + "/Overlay3/" + str(time.time()) + ".jpg")
        """
        if not os.path.exists(os.getcwd()+"/configs/"+elements+"/Overlay4"):
            os.mkdir(os.getcwd()+"/configs/"+elements+"/Overlay4/")
            imgHochArray = []
            imgBreitArray = []
            for element in os.listdir(os.getcwd() + "/configs/" + elements + "/Overlay2/"):
                imgBreitArray.append(
                    np.asarray(Image.open(os.getcwd() + "/configs/" + elements + "/Overlay2/" + element)))
            for element in os.listdir(os.getcwd() + "/configs/" + elements + "/Overlay1/"):
                imgHochArray.append(
                    np.asarray(Image.open(os.getcwd() + "/configs/" + elements + "/Overlay1/" + element)))
            breitenFaktor = int(len(imgBreitArray[0][0])/len(imgHochArray[0][0]))
            hoehenFaktor = int(len(imgHochArray[0]) / len(imgBreitArray[0]))
            newBreitImgArray = []
            for j in range(len(imgBreitArray)):
                newImg = []
                for row in imgBreitArray[j]:
                    for k in range(hoehenFaktor):
                        newImg.append(row)
                newBreitImgArray.append(newImg)

            for element in newBreitImgArray:
                image = Image.fromarray(np.asarray(element))
                image.save(os.getcwd()+"/configs/"+elements+"/Overlay4/"+str(time.time())+".jpg")

        if not os.path.exists(os.getcwd()+"/configs/"+elements+"/Overlay5/"):
            os.mkdir(os.getcwd()+"/configs/"+elements+"/Overlay5/")
            dirArr = []
            for element in os.listdir(os.getcwd()+"/configs/"+elements+"/"):
                if not os.path.isdir(os.getcwd()+"/configs/"+elements+"/"+element):
                    dirArr.append(element)
            for i in range(0,len(dirArr)-1,2):
                background = Image.open(os.getcwd()+"/configs/"+elements+"/"+dirArr[i])
                foreground = Image.open(os.getcwd()+"/configs/"+elements+"/"+dirArr[i+1])
                background = background.convert(mode="RGBA")
                foreground = foreground.convert(mode="RGBA")
                Image.alpha_composite(background,foreground).save(os.getcwd()+"/configs/"+elements+"/Overlay5/"+str(time.time())+".tiff")
                Image.blend(background,foreground,0.5).save(os.getcwd()+"/configs/"+elements+"/Overlay5/"+str(time.time())+"-1.tiff")
            imgT = Image.open(os.getcwd()+"/configs/"+elements+"/"+dirArr[0])
            imgT = imgT.convert(mode="RGBA")
            lenArr = 1./len(dirArr)
            for i in range(1,len(dirArr)-1,2):
                background = Image.open(os.getcwd() + "/configs/" + elements + "/" + dirArr[i])
                background = background.convert(mode="RGBA")
                imgT = Image.blend(background,imgT,0.5)
            imgT.save(os.getcwd()+"/configs/"+elements+"/Overlay5/"+str(0)+"-2.tiff")

            """
            newImg = []
            for row in range(len(img[0])):
                newImgRow = []
                for cell in range(len(img[0][0])):
                    cellS = []
                    r,g,b = 0,0,0
                    for i in range(len(img)):
                        r = r+img[i][row][cell][0] / len(img)
                        g = g+img[i][row][cell][1] / len(img)
                        b = b+img[i][row][cell][2] / len(img)
                    cellS.append(int(r))
                    cellS.append(int(g))
                    cellS.append(int(b))
                    cellS.append(255)
                    newImgRow.append(np.asarray(cellS,dtype="uint8"))
                newImg.append(newImgRow)
                """
            """


    image = Image.fromarray(np.asarray(newImg))
    image.save("./images/ImageOverlay2.tiff")
    newImg = []
    for row in range(len(imgHoch)):
        newImgRow = []
        for cell in range(len(imgHoch[0])):
            cellS = []
            r = (imgBreit[row][cell][0] + imgHoch[row][cell][0]) / 2
            g = (imgBreit[row][cell][1] + imgHoch[row][cell][1]) / 2
            b = (imgBreit[row][cell][2] + imgHoch[row][cell][2]) / 2
            cellS.append(int(r))
            cellS.append(int(g))
            cellS.append(int(b))
            cellS.append(255)
            newImgRow.append(np.asarray(cellS, dtype="uint8"))
        newImg.append(newImgRow)

    image = Image.fromarray(np.asarray(newImg))
    image.save("./images/ImageOverlay6.tiff")
    """
