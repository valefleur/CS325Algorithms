import os
import sys
import argparse
import random
from timeit import default_timer as timer

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


def main(sizes):
    parser = argparse.ArgumentParser(description="mergesortTimed will create an array of random integers, time how long it takes to sort that array and will then print the time out to a file.")
    #parser.add_argument(default="data.txt", nargs="?", dest='datafile', action='store', help="A path to the file with lines of integers to sort. Will default to data.txt if not provided.")
    data = []
    with open("mergeTimed.out", "w") as dataOut:
        for i in range(len(sizes)):
            n = sizes[i]
            #create n-sized arrays of random integers
            for j in range(n):
                data.append(random.randint(1, 10000))

            random.shuffle(data)   # for good measure

            mSorter = mergeSorter()    #create an instance of the object

            #sort those integers
            start = timer()
            mSorter.divide(data, "init")          #do stuff with that object
            end = timer()
            totalTime = end - start

            #record n and the amount of time it took to sort
            dataOut.write(str(n) + ", " + str(totalTime) + "\n")

    dataOut.close()





if __name__ == '__main__':
    main([1000, 2000, 5000, 10000, 100000, 1000000, 10000000, 100000000])
