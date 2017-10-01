import os
import sys
import argparse
import time

class mergeSorter:
    def merge(self, a, p, q, r):    #off by 1 issues?
        print("In Merge.")#\np is: " + str(p) +"\nq is: " + str(q) + "\nr is: " + str(r) + "\nlen(a) is: " + str(len(a)))
        n = q - p + 1
        m = r - q
        left = []
        right = []
        i = 0
        j = 0
        for i in range(n):
            #print(str(i) + "th time filling in left array.")
            left.append(a[p + i])
        for j in range(m):
            #print(str(j) +"the time filling in right array.")
            right.append(a[q + j])
        #Add sentinels
        left.append(sys.maxsize)
        right.append(sys.maxsize)
        i = 0
        j = 0
        for k in range(p, r):
            if left[i] <= right[j]:
                a[k] = left[i]
                i = i + 1
            else:
                a[k] = right[j]
                j = j + 1
        print("***Merged data array is:")
        print(a)
        return a;
            #if i == n-1:
                #fill in a[] with rest of right[]
            #    return;
            #else:
                #fill in a[] with rest of left[]
            #    return;

    def divide(self, data, p, r, side):
        print("On the " + side + " of DIVIDE. Data is:\n" +str(data)+ "\nsmall index is: " + str(p) + "\nbig index is: " + str(r))
        #print("Begin DIVIDE.\ndata size is: " + str(len(data)) + "\np is: " + str(p) +"\nr is: " + str(r))
    #TODO add timing, add to return struct to be written out
        if p < r:
            q = (p+r)//2  #off by 1 issue?
            #print("q is: " + str(q))
            self.divide(data, p, q, "left")
            self.divide(data, q+1, r, "right")
            #print("In DIVIDE, about to merge.\ndata size is: " + str(len(data)) + "\np is: " + str(p) +"\nq is: " + str(q) + "\nr is: " + str(r))
            self.merge(data, p, q, r+1)    #TODO write merge() 
        #DEBUG
        #print("***Sorted data is: ")
        #print(data)
        #print("\n")
        #DEBUG

def main():
    parser = argparse.ArgumentParser(description="Use insertSort to divide lines of integers in a file. Results will be stored in insert.out.")
    parser.add_argument(default="data.txt", nargs="?", dest='datafile', action='store', help="A path to the file with lines of integers to divide. Will default to data.txt if not provided.")
    #use nargs="?" to indicate it is optional; without nargs, arg is required
    args = parser.parse_args(sys.argv[1:])
    path = args.datafile
    print("Data file is: " + path)
    if(os.path.exists(path)):
        with open(path, "r") as file1, open("merge.out", "w") as file2:
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
                print("***givenLength is: " + str(givenLength) + " and actLength is: " + str(actLength))
                print("***Undivided data is: ")
                print(data)
                print("p is: 0\nr is: " + str(len(data)-1))
                #DEBUG
                if (givenLength == actLength):
                    mSorter = mergeSorter()    #create an instance of the object
                    mSorter.divide(data, 0, len(data)-1, "initial")          #do stuff with that object
                    #DEBUG
                    print("***Sorted data is: ")
                    print(data)
                    print("\n")
                    #DEBUG
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
