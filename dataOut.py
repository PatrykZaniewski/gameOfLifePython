from PIL import Image
import os


class PrintData:
    def __init__(self, fileName):
        self.fileName = fileName

    def printToFile(self, lastGen):
        saveMe = open(self.fileName, "w")
        for i in lastGen:
            for j in i:
                saveMe.write(str(j))
            saveMe.write('\n')

    def printPNG(self, amount, allGen, heigth, length):
        imgArray = []
        for i in range(0, amount + 1):
            arr = allGen[i]
            img = Image.new('RGB', (heigth, length), color=(255, 0, 0))
            pixels = img.load()
            for j in range(1, heigth + 1):
                for k in range(1, length + 1):
                    if arr[j][k] == 0:
                        pixels[j - 1, k - 1] = (255, 255, 255)
                    elif arr[j][k] == 1:
                        pixels[j - 1, k - 1] = (0, 0, 0)
            if (os.path.exists(os.getcwd() + "/images")) is False:
                os.makedirs('images')
            path = os.getcwd() + '/images/'
            imgArray.append(img)
            fileOutName = str(i) + '.png'
            img.save(path + fileOutName)
        print(imgArray.__len__())
        self.printGIF(imgArray)

    def printGIF(self, imgArray):
        imgArray[0].save('moving_ball.gif', append_images=imgArray[:], save_all=True, duration=100, loop=0)
