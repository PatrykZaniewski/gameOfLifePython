from dataRead import *
from simulation import *
from dataOut import *

class gameOfLife:

    def main(self):
        x = "test.txt"
        read = Read(x)
        arr, lineNumber, maxLen = read.readFile()
        afterBorder = Border(arr, maxLen, lineNumber)
        arr, length, heigth = afterBorder.border()

        simulation = Simulation(arr, length, heigth)
        genNumber = input('Amount of gen: ')
        arrHistory = simulation.simulate(genNumber)

        printData = PrintData('wynik.txt')
        printData.printToFile(arrHistory[(arrHistory.__len__() - 1)])
        printData.printPNG(genNumber, arrHistory, heigth, length)


if __name__ == "__main__":
    gameOfLife().main()
