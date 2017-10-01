import os
import sys
import argparse
import random
from timeit import default_timer as timer

class insertSorter:
    def sort(self, data):
    #TODO add timing, add to return struct to be written out
        length = len(data)
        for j in range (1, length):
            valToSort = data[j]
            i = j - 1
            while (i > -1) and (data[i] > valToSort):
                data[i+1] = data[i]
                i = i-1
            data[i+1] = valToSort
        #DEBUG
        #print("***Sorted data is: ")
        #print(data)
        #print("\n")
        #DEBUG

def main(sizes):
    parser = argparse.ArgumentParser(description="insertsortTimed will create an array of random integers, time how long it takes to sort that array and will then print the time out to a file.")
    #parser.add_argument(default="data.txt", nargs="?", dest='datafile', action='store', help="A path to the file with lines of integers to sort. Will default to data.txt if not provided.")
    data = []
    for i in range(len(sizes)):
        n = sizes[i]
        #create n-sized arrays of random integers
        for j in range(n):
            data.append(randint(1, 10000))

        shuffle(data)   # for good measure

        iSorter = insertSorter()    #create an instance of the object

        #sort those integers
        start = timer()
        iSorter.sort(data)          #do stuff with that object
        end = timer()
        totalTime = end - start

        #record n and the amount of time it took to sort
        with open("insertTimed.out", "a") as dataOut:
            dataOut.write(str(n) + ", " + str(totalTime) + "\n")

        dataOut.close()





if __name__ == '__main__':
    main([1000, 2000, 5000, 10000])
