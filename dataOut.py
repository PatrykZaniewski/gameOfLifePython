from PIL import Image, ImageDraw


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
        numberOfGen = allGen.__len__()
        print(heigth)
        for i in range(0, numberOfGen):
            arr = allGen[i]
        img = Image.new('RGB', (heigth, length), color=(255, 255, 255))
        pixels = img.load()
        pixels[0, 0] = (0, 0, 0)
        img.save('pil_text.png')
