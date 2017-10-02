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
    parser.add_argument('-b', '--best', dest="best", nargs="?", help="Generate and run the BEST case scenario.")
    parser.add_argument('-w', '--worst', dest="worst", nargs="?", help="Generate and run the WORST case scenario.")
    data = []
    data2 = []
    best = False
    worst = False
    both = False
    #parse arguments
    args = parser.parse_args()
    if best and worst:
        both = True
    with open("insertTimedBW.out", "w") as dataOut:
        for i in range(len(sizes)):
            n = sizes[i]
            #create n-sized arrays of random integers
            
            if(best):
                for j in range(n):
                    data.append(j)
            elif(worst):
                for j in range(n):
                    data.append(n - j)
            #elif(both)     #do BEST now, do WORST after BEST
            else:   #if neither BEST nor WORST
                for j in range(n):
                    data.append(random.randint(1, 10000))
                    random.shuffle(data)   # for good measure

            iSorter = insertSorter()    #create an instance of the object


            #sort those integers
            start = timer()
            iSorter.sort(data)          #do stuff with that object
            end = timer()
            totalTime = end - start

            #record n and the amount of time it took to sort
            dataOut.write(str(n) + ", " + str(totalTime) + "\n")
    dataOut.close()
    if(both):   #already did BEST, now do WORST
        with open("insertTimedBW.out", "a") as dataOut:
            for i in range(len(sizes)):
                n = sizes[i]
                #create n-sized arrays of random integers
                data.append(n - j)

                iSorter = insertSorter()    #create an instance of the object

                #sort those integers
                start = timer()
                iSorter.sort(data)          #do stuff with that object
                end = timer()
                totalTime = end - start

                #record n and the amount of time it took to sort
                dataOut.write(str(n) + ", " + str(totalTime) + "\n")
        dataOut.close()

if __name__ == '__main__':
    main([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])#, 20000, 30000, 50000, 100000])
