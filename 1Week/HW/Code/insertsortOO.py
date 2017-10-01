import os
import sys
import time


class fileManager:
    "Manages opening, reading, writing and closing of files"
    inputData = []
    def readFile(self):
        if( sys.args > 1 ):
            with open(sys.argv[1], "r") as file1:
                inputData = file1.read().split(' ')
        elif( os.path.exists("~/data.txt") ):
            inputData = open("data.txt", "r").read().split(' ')

    "def closeFile(self):"

    def writeFile(self):
        with open("output.txt", "w"):
            for element in dataToSort:
                print element + "\n"


class insertSorter(self):
    "Manages sorting the raw data."
    t = Timer()
    dataToSort = []
    def insertSort(dataToSort):
        t.startTimer
        length = dataToSort.length
        if (length == 0):
            dataToSort = [8, 2, 3, 9, 1]
            length = dataToSort.length
        for j in range (1, length):
            valToSort = dataToSort[j]
            i = j - 1
            while i >= 0 and dataToSort[i] > valToSort:
                dataToSort[i+1] = dataToSort[i]
                i = i-1
            A[i+1] = valToSort
        t.stopTimer

class Timer(self):
    "Manages the stop watch."
    startTime = 0.0
    totalTime = 0.0
    diff = 0.0
    def startTimer(self):
        startTime = time.time()
    def stopTimer(self): 
        stopTime = time.time()
        diff = stopTime - startTime
        print("***Elapsed time: " + diff)
