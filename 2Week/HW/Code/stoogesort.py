import os
import sys
import argparse
import time
import math

class stoogeSorter:
    def stooge(self, A, low_index, high_index):
        n = high_index - low_index + 1
        #DEBUG
        print("\n\nLow index is: " + str(low_index) +" High index is: " + str(high_index) + " n is: " + str(n))
        print("A is: " + str(A))
        #DEBUG
        if n < 2:
            print("In n < 2, returning: " + str(A))
            return A
        elif n == 2:
            #DEBUG
            print("In n == 2")
            print("A["+str(low_index)+"] is: " + str(A[low_index]))
            print("A["+str(high_index)+"] is: " + str(A[high_index]))
            #DEBUG
            if int(A[low_index]) > int(A[high_index]):
                print("In n == 2, swapping: " + str(A[low_index]) + " and " + str(A[high_index]))
                temp = A[low_index]
                A[low_index] = A[high_index]
                A[high_index] = temp
            else:
                print("In n == 2, A already sorted.")
            print("In n == 2, returning: " + str(A) + "\n")
            return A
        else: #n > 2
            m = int(math.ceil(2.0 * float(high_index-low_index+1)/3.0))
            #m = int(math.ceil(float(high_index - low_index)+1)/3.0)
            print("In n > 2, m = " + str(m))
            stoogeSorter.stooge(self, A, low_index, low_index + m - 1)
            stoogeSorter.stooge(self, A, high_index - m + 1 , high_index)
            stoogeSorter.stooge(self, A, low_index, low_index + m - 1)
            #print("In n > 2, returning: " + str(A))
            return A


def main():
    parser = argparse.ArgumentParser(description="Use stoogeSort to divide lines of integers in a file. Results will be stored in insert.out.")
    parser.add_argument(default="data.txt", nargs="?", dest='datafile', action='store', help="A path to the file with lines of integers to divide. Will default to data.txt if not provided.")
    #use nargs="?" to indicate it is optional; without nargs, arg is required
    args = parser.parse_args(sys.argv[1:])
    path = args.datafile
    print("Input file is: " + path)
    if(os.path.exists(path)):
        with open(path, "r") as file1, open("stooge.out", "w") as file2:
            for line in file1:
                data = line.split()
                for d in range(len(data)):      #convert list of str to list of int
                    data[d] = int(data[d])
                givenLength = int(data.pop(0))   #remove and return the indexed element
                actLength = len(data)
                if (givenLength == actLength):
                    #DEBUG
                    print("\n\nData is: " + str(data))
                    #DEBUG 
                    sSorter = stoogeSorter()    #create an instance of the object
                    result = sSorter.stooge(data, 0, actLength-1)          #do stuff with that object
                    #DEBUG
                    #print("***Result is: ")
                    #print(result)
                    #print("\n")
                    #DEBUG
                    if(file2.tell() > 0):   #if prev written, add a new line
                        file2.write("\n")
                    for i in range(len(result)):
                        file2.write(str(result[i]) + " ")
                else:
                    print("***Error with input data.  Please fix and try again.\nError on line:\n")
                    print(line)
        file2.close()
        file1.close()
    else:
        print("Please put data.txt in this directory and try again!")

if __name__ == '__main__':
    main()
