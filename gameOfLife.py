from dataRead import *


class gameOfLife:

    def main(self):
        x = "test.txt"
        read = Read(x)
        arr, lineNumber, maxLen = read.readFile()
        afterBorder = Border(arr, len, lineNumber)
        afterBorder.Boder()

if __name__ == "__main__":
    gameOfLife().main()
