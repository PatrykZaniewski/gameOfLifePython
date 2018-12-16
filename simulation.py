import numpy as np


class Simulation:
    historyArray = []

    def __init__(self, arr, length, heigth):
        self.arr = arr
        self.length = length
        self.heigth = heigth

    def simulate(self, amount):
        self.historyArray.append(np.array(self.arr))

        for i in range(0, int(amount)):
            self.arr = np.array(self.arr)
            arrHelp = np.copy(self.arr)
            for j in range(1, self.heigth + 1):
                for k in range(1, self.length + 1):
                    if self.arr[j][k] == 0:
                        oneCount = 0
                        if self.arr[j - 1][k] == 1:
                            oneCount += 1
                        if self.arr[j - 1][k + 1] == 1:
                            oneCount += 1
                        if self.arr[j][k + 1] == 1:
                            oneCount += 1
                        if self.arr[j + 1][k + 1] == 1:
                            oneCount += 1
                        if self.arr[j + 1][k] == 1:
                            oneCount += 1
                        if self.arr[j + 1][k - 1] == 1:
                            oneCount += 1
                        if self.arr[j][k - 1] == 1:
                            oneCount += 1
                        if self.arr[j - 1][k - 1] == 1:
                            oneCount += 1
                        if oneCount == 3:
                            arrHelp[j][k] = 1

                    elif self.arr[j][k] == 1:
                        oneCount = 0
                        if self.arr[j - 1][k] == 1:
                            oneCount += 1
                        if self.arr[j - 1][k + 1] == 1:
                            oneCount += 1
                        if self.arr[j][k + 1] == 1:
                            oneCount += 1
                        if self.arr[j + 1][k + 1] == 1:
                            oneCount += 1
                        if self.arr[j + 1][k] == 1:
                            oneCount += 1
                        if self.arr[j + 1][k - 1] == 1:
                            oneCount += 1
                        if self.arr[j][k - 1] == 1:
                            oneCount += 1
                        if self.arr[j - 1][k - 1] == 1:
                            oneCount += 1
                        if (oneCount != 3) and (oneCount != 2):
                            arrHelp[j][k] = 0
            self.historyArray.append(arrHelp)
            self.arr = np.copy(arrHelp)
        return self.historyArray
