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
            arr.append(line)
            line = readMe.readline()
        return arr, lineNumber, maxLen


class Border:

    def __init__(self, arr, length, hei):
        self.arr = arr
        self.length = length
        self.hei = hei

    def border(self):
        for x in self.arr:
            size = x.__len__()
#TODO otoczyc
        a = np.full((self.length), 2)
        self.arr.insert(0, a)
        self.arr.insert(self.hei + 1, a)
        print(self.arr[1][1])
