import os
import sys
import argparse
import time
import errno

class activitySelector:
    #Data must be sorted by INcreasing start time, not decreasing.
    def lastToStart(self, activity):
        #enumerate inner array for readability
        label = 0
        startTime = 1
        finishTime = 2
        n = len(activity) - 1
        #add last-to-start activity to schedule
        optimalSchedule = [activity[n][label]]
        current = n
        for prev in range(n - 1 , -1, -1):
            #print("\ncurrent: " + str(current) + "        prev: " + str(prev))
            #print("activity[current]: " + str(activity[current]) + "    activity[prev]: " + str(activity[prev]))
            #print("activity[current][sTime]: " + str(activity[current][startTime]) + "      activity[prev][fTime]: " + str(activity[prev][finishTime]))
            if activity[prev][finishTime] <= activity[current][startTime]:
                optimalSchedule.insert(0, activity[prev][label])
                current = prev
        return optimalSchedule

class mergeSorter:
#Thanks to https://gist.github.com/jvashishtha/2720700
    def merge(self, l, r):
        if not len(l) or not len(r):
            return l or r;
        sorted = []
        i = 0
        j = 0
        while(len(sorted) < len(l) + len(r)):
            #print("l is: " + str(l) + "     r is: " + str(r))
            #print("i is: " + str(i) + "     l[i] is: " + str(l[i]) + "   l[i][2] is: " + str(l[i][2]) + "\n\n")
            if l[i][1] < r[j][1]:   #[i][1] is start, [i][2] is finish
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
    parser = argparse.ArgumentParser(description="Use activitySelection to find the maximum number of non-competing activities that can be scheduled.")
    parser.add_argument(default="act.txt", nargs="?", dest="datafile", action="store", help="A path to the file containing the input data.  Will default to act.txt if not provided.")
    args = parser.parse_args(sys.argv[1:])
    path = args.datafile
    print("Input file is: " + path)
    jobset = 1
    if(os.path.exists(path)):
        with open(path, "r") as inFile:
            actQtyStr = inFile.readline().split()
            while(actQtyStr != []):
            #if(actQtyStr == [""]): #if actQtyStr is empty, assume no more input data
                #print("No more data.")
                #return
            #else: 
                #todo: check if len(actQtStr) > 1 and report to user
                #print("actQtyStr is: " + str(actQtyStr))
                actQty = int(actQtyStr[0])
                #DEBUG
                #print("actQtyStr is: " + str(actQtyStr))
                #print("actQty is: " + str(actQty))
                #DEBUG
           
                allActivities = [] 
                for activity in range(actQty):
                    act = [0, 0, 0]
                    programStr = inFile.readline()
                    program = programStr.split()
                    
                    label = int(program[0])
                    start = int(program[1])
                    finish = int(program[2])
                    act[0] = label
                    act[1] = start
                    act[2] = finish
                    allActivities.append(act)
                    #DEBUG
                    #print("\nprogram: " + str(program))
                    #print("label: " + str(act[0]))
                    #print("start " + str(act[1]))
                    #print("finish: " + str(act[2]))
                    #DEBUG
                #print("allActivities: " + str(allActivities))
                #use MERGESORT to sort the data by start time
                sorter = mergeSorter()
                allActivitiesSorted = sorter.divide(allActivities, "init")
                #print("allActivitiesSorted: " + str(allActivitiesSorted))
                
                #send sorted data through ACTSEL to find the 
                # latest start time
                scheduler = activitySelector()
                schedule = scheduler.lastToStart(allActivitiesSorted)
                #print("schedule is: " + str(schedule))

                #print JobSet, len(schedule) and schedule
                scheduleStr = ""
                for x in schedule:
                    scheduleStr = scheduleStr + str(x) + " "
                print("Set " + str(jobset))
                print("Number of activities selected = " + str(len(schedule)))
                print("Activities: " + scheduleStr + "\n")

                jobset +=1
                actQtyStr = inFile.readline().split()
        inFile.close()
    else:
        print("Path does not exist.  Check input file path.")
        return

if __name__ == '__main__':
    main()
