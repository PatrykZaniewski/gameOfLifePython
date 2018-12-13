from dataRead import *


class gameOfLife:

    def main(self):
        x = "test.txt"
        read = Read(x)
        arr, lineNumber, maxLen = read.readFile()
        afterBorder = Border(arr, maxLen, lineNumber)
        afterBorder.border()

if __name__ == "__main__":
    gameOfLife().main()
