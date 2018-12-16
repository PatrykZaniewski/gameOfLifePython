import numpy as np


class Read:

    def __init__(self, fileName):
        self.fileName = fileName

    def readFile(self):

        readMe = open(self.fileName, "r")
        line = readMe.readline()
        arr = []
        lineNumber = 0
        maxLen = 0
        while line:
            lineNumber += 1
            line = line.strip("\n")
            line = line.strip(" ")
            if line.__len__() > maxLen:
                maxLen = line.__len__()
            arrLine = []
            for letter in line:
                if letter == '0':
                    arrLine.append(0)
                elif letter == '1':
                    arrLine.append(1)
                else:
                    arrLine.append(2)
            arr.append(arrLine)
            line = readMe.readline()
        return arr, lineNumber, maxLen


class Border:

    def __init__(self, arr, length, heigth):
        self.arr = arr
        self.length = length
        self.heigth = heigth

    def border(self):
        for x in range(0, self.heigth):
            self.arr[x].insert(0, 2)
        for x in self.arr:
            if x.__len__() < self.length:
                for i in range(0, self.length - x.__len__()):
                    x.append(2)
            x.append(2)
        a = np.full(self.length + 2, 2, dtype=int)
        self.arr.insert(0, a)
        self.arr.insert(self.heigth + 1, a)
        return self.arr, self.length, self.heigth
