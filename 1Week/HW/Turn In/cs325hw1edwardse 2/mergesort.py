import os
import sys
import argparse
import time

class mergeSorter:
#Thanks to https://gist.github.com/jvashishtha/2720700
    def merge(self, l, r):
        if not len(l) or not len(r):
            return l or r;
        sorted = []
        i = 0
        j = 0
        while(len(sorted) < len(l) + len(r)):
            if l[i] < r[j]:
                sorted.append(l[i])
                i += 1
            else:
                sorted.append(r[j])
                j += 1
            if i == len(l) or j == len(r):
                sorted.extend(l[i:] or r[j:])
                break
        #print("***Merged data array is:")
        #print(sorted)
        return sorted;

    def divide(self, data, side):
        #print("On the " + side + " of DIVIDE. Data is:\n" +str(data))
        if len(data) < 2:
            return data
        mid = len(data)/2
		
        left = self.divide(data[:mid], "left")
        right = self.divide(data[mid:], "right")
        return self.merge(left, right)


def main():
    parser = argparse.ArgumentParser(description="Use insertSort to divide lines of integers in a file. Results will be stored in insert.out.")
    parser.add_argument(default="data.txt", nargs="?", dest='datafile', action='store', help="A path to the file with lines of integers to divide. Will default to data.txt if not provided.")
    #use nargs="?" to indicate it is optional; without nargs, arg is required
    args = parser.parse_args(sys.argv[1:])
    path = args.datafile
    print("Input file is: " + path)
    if(os.path.exists(path)):
        with open(path, "r") as file1, open("merge.out", "w") as file2:
            for line in file1:
                data = line.split()
                for d in range(len(data)):      #convert list of str to list of int
                    data[d] = int(data[d])
                givenLength = int(data.pop(0))   #remove and return the indexed element
                actLength = len(data)
                if (givenLength == actLength):
                    mSorter = mergeSorter()    #create an instance of the object
                    result = mSorter.divide(data, "initial")          #do stuff with that object
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
