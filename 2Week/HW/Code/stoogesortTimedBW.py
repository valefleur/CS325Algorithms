import os
import sys
import argparse
import random
from timeit import default_timer as timer
import math

class stoogeSorter:
    def stooge(self, A, low_index, high_index):
        n = high_index - low_index + 1
        #DEBUG
        #print("\n\nLow index is: " + str(low_index) +" High index is: " + str(high_index) + " n is: " + str(n))
        #print("A is: " + str(A))
        #DEBUG
        if n < 2:
            #print("In n < 2, returning: " + str(A))
            return A
        elif n == 2:
            #DEBUG
            #print("In n == 2")
            #print("A["+str(low_index)+"] is: " + str(A[low_index]))
            #print("A["+str(high_index)+"] is: " + str(A[high_index]))
            #DEBUG
            if int(A[low_index]) > int(A[high_index]):
                #print("In n == 2, swapping: " + str(A[low_index]) + " and " + str(A[high_index]))
                temp = A[low_index]
                A[low_index] = A[high_index]
                A[high_index] = temp
            #else:
            #    print("In n == 2, A already sorted.")
            #print("In n == 2, returning: " + str(A) + "\n")
            return A
        else: #n > 2
            m = int(math.ceil(2.0 * float(high_index-low_index+1)/3.0))
            #m = int(math.ceil(float(high_index - low_index)+1)/3.0)
            #print("In n > 2, m = " + str(m))
            stoogeSorter.stooge(self, A, low_index, low_index + m - 1)
            stoogeSorter.stooge(self, A, high_index - m + 1 , high_index)
            stoogeSorter.stooge(self, A, low_index, low_index + m - 1)
            #print("In n > 2, returning: " + str(A))
            return A

def main(sizes):
    parser = argparse.ArgumentParser(description="stoogesortTimed will create an array of random integers, time how long it takes to sort that array and will then print the time out to a file.")
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
    with open("stoogeTimedBW.out", "a") as dataOut:
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

            sSorter = stoogeSorter()    #create an instance of the object

            #sort those integers
            start = timer()
            sSorter.stooge(data, 0, n-1)          #do stuff with that object
            end = timer()
            totalTime = end - start

            #record n and the amount of time it took to sort
            dataOut.write(str(n) + ", " + str(totalTime) + "\n")
    dataOut.close()
    if(both):   #already did BEST, now do WORST
        with open("stoogeTimedBW.out", "a") as dataOut:
            for i in range(len(sizes)):
                n = sizes[i]
                #create n-sized arrays of random integers
                data.append(n - j)

            sSorter = stoogeSorter()    #create an instance of the object
            #sort those integers
            start = timer()
            sSorter.stooge(data, 0, n-1)          #do stuff with that object
            end = timer()
            totalTime = end - start

            #record n and the amount of time it took to sort
            dataOut.write(str(n) + ", " + str(totalTime) + "\n")
        dataOut.close()

if __name__ == '__main__':
    main([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])#, 100000, 1000000, 10000000, 100000000])
    #main([100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
