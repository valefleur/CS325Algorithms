import os
import sys
import argparse
import time

class mergeSorter:
    def merge(self, l, r):    #off by 1 issues?
        #print("In Merge.\np is: " + str(p) +"\nq is: " + str(q) + "\nr is: " + str(r) + "\nlen(a) is: " + str(len(a)))

        if not len(l) or not len(r):
            return l or r;
        sorted = []
        i = 0
        j = 0
        while( len(sorted) < len(l) + len(r)):
            if l[i] < r[j]:
                sorted.append(l[i])
                i += 1
            else:
                sorted.append(r[j])
                j += 1
            if i == len(l) or j == len(r):
                sorted.extend(l[i:] or r[j:])
                break
        print("***Merged data array is:")
        print(sorted)
        return sorted;
            #if i == n-1:
                #fill in a[] with rest of right[]
            #    return;
            #else:
                #fill in a[] with rest of left[]
            #    return;

    def divide(self, data, side):
		#Thanks to https://gist.github.com/jvashishtha/2720700
        print("On the " + side + " of DIVIDE. Data is:\n" +str(data))
        #print("Begin DIVIDE.\ndata size is: " + str(len(data)) + "\np is: " + str(p) +"\nr is: " + str(r))
    #TODO add timing, add to return struct to be written out
        if len(data) < 2:
            return data
        mid = len(data)/2
		
        left = self.divide(data[:mid], "left")
        right = self.divide(data[mid:], "right")
        return self.merge(left, right)

        # if p < r:
            # q = (p+r)//2  # chav is double // mean divide? #off by 1 issue?
            # print("q is: " + str(q))
            # self.divide(data, p, q, "left")
            # self.divide(data, q+1, r, "right")
            # print("In DIVIDE, about to merge.\ndata size is: " + str(len(data)) + "\np is: " + str(p) +"\nq is: " + str(q) + "\nr is: " + str(r))
            # self.merge(data, p, q, r)    #TODO write merge() 
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
                    result = mSorter.divide(data, "initial")          #do stuff with that object
                    #DEBUG
                    print("***Result is: ")
                    print(result)
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
