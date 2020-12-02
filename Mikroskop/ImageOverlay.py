from PIL import Image
import numpy as np
import os
if __name__=="__main__":

    rawImages = []
    for elements in os.listdir(os.getcwd() + "/images/"):
        if elements != "Test":
            if elements !="png":
                rawImages.append("./images/"+elements)


    img = []
    for elements in rawImages:
        img.append(np.asarray(Image.open(elements)))

    #-------------------------------------------------

    newImg = []
    for row in range(len(img[0])):
        for i in range(len(img)):
            newImg.append(img[i][row])
    image = Image.fromarray(np.asarray(newImg))
    image.save("./images/Test/ImageOverlay3.tiff")

    newImg = []
    for row in range(len(img[0])):
        newImgRow = []
        for cell in range(len(img[0][0])):
            for i in range(len(img)):
                newImgRow.append(img[i][row][cell])

        newImg.append(newImgRow)

    image = Image.fromarray(np.asarray(newImg))
    image.save("./images/Test/ImageOverlay.tiff")
    imgBreit = np.asarray(Image.open("./images/Test/ImageOverlay.tiff"))
    imgHoch = np.asarray(Image.open("./images/Test/ImageOverlay3.tiff"))
    hoehenFaktor = int(len(imgHoch) / len(imgBreit))
    breitenFaktor = int(len(imgBreit[0]) / len(imgHoch[0]))
    newImg = []
    for row in imgBreit:
        for i in range(hoehenFaktor):
            newImg.append(row)
    imgBreit = newImg
    newImg = []
    for row in imgHoch:
        newImgRow = []
        for cell in row:
            for i in range(breitenFaktor):
                newImgRow.append(cell)
        newImg.append(newImgRow)
    imgHoch = newImg
    image = Image.fromarray(np.asarray(imgBreit))
    image.save("./images/Test/ImageOverlay4Breit.tiff")
    image = Image.fromarray(np.asarray(imgHoch))
    image.save("./images/Test/ImageOverlay5Hoch.tiff")
    background = Image.open("./images/Test/ImageOverlay4Breit.tiff")
    foreground = Image.open("./images/Test/ImageOverlay5Hoch.tiff")
    background = background.convert(mode="RGBA")
    foreground = foreground.convert(mode="RGBA")
    Image.alpha_composite(background,foreground).save("./images/Test/ImageOverlay6.tiff")
    Image.blend(background,foreground,0.5).save("./images/Test/ImageOverlay7.tiff")
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