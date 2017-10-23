import os
import sys
import argparse
import time

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

def main():
    parser = argparse.ArgumentParser(description="Use insertSort to sort lines of integers in a file. Results will be stored in insert.out.")
    parser.add_argument(default="data.txt", nargs="?", dest='datafile', action='store', help="A path to the file with lines of integers to sort. Will default to data.txt if not provided.")
    #use nargs="?" to indicate it is optional; without nargs, arg is required
    args = parser.parse_args(sys.argv[1:])
    path = args.datafile
    print("Data file is: " + path)
    if(os.path.exists(path)):
        with open(path, "r") as file1, open("insert.out", "w") as file2:
            k = 0
            for line in file1:
                #DEBUG
                #print("*Pass number: " + str(k))
                k = k+1
                #DEBUG
                data = line.split()
                for d in range(len(data)):      #convert list of str to list of int
                    data[d] = int(data[d])
                givenLength = int(data.pop(0))   #remove and return the indexed element
                actLength = len(data)
                #DEBUG
                #print("***givenLength is: " + str(givenLength) + " and actLength is: " + str(actLength))
                #print("***Unsorted data is: ")
                #print(data)
                #DEBUG
                if (givenLength == actLength):
                    iSorter = insertSorter()    #create an instance of the object
                    iSorter.sort(data)          #do stuff with that object
                    if(file2.tell() > 0):   #if prev written, add a new line
                        file2.write("\n")
                    for i in range(len(data)):
                        file2.write(str(data[i]) + " ")
                else:
                    print("***Error with input data.  Please fix and try again.\nError on line:\n")
                    print(line)
        file2.close()
        file1.close()
    else:
        print("Please put data.txt in this directory and try again!")

if __name__ == '__main__':
    main()
