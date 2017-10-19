import os
import sys
import argparse
import time
import errno

class pointOfSale:
    #Recieved help from interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html

    #makeChange uses DP to find the minimum number of coins needed to make change
    #It follows a bottom-up approach, which means it calculates the minCoins
    # needed to make change for 1 cent, the minCoins needed to make change for
    # 2 amount, etc. all the way up to the minCoins needed to make change for
    # "change" amount.
    #Parameters
    #   coinList: a list of coin denominations in increasing order
    #   change: the initial and final amount for which to make change
    #   minCoinsForThisAmount: the minimum quantity of coins needed to make
    #    change for the current "amount"
    #   usedCoins: a list indicating how many of each coin denomination used
    #    to make change
    def makeChange(self, coinList, A, minCoinsForThisAmount, usedCoins):
        #Create a list--count--containing how many amount it takes to create
        # change for an amount equal to the current index of count
        for amount in range(A+1):
            #print("amount is: " + str(amount))

            coinCount = amount
            newCoin = 1
            #for each coin in coinList that is less than or equal to the current
            # amount
            n = 0
            #for coin in coinList if coin <= amount:
            for coinValue in [coin for coin in coinList if coin <= amount]:
                #if the min quantity of coins needed to make (amount-coinValue)+1 cents is
                # less than the current coinCount, then
                #   update coinCount to be the current min quantity for that 
                #    amount'
                #   update newCoin to coinValue to look at the next coin in the list of
                #    coin denominations
                ##coinList[coin]
                #print("coinValue is: " + str(coinValue))
                #print("n is: " + str(n))

                if minCoinsForThisAmount[amount - coinValue] + 1 < coinCount:

                    coinCount = minCoinsForThisAmount[amount - coinValue] + 1
                    #print("Updating usedCoins[n]")
                    usedCoins[amount] = n
                    #print("usedCoins is: "+str(usedCoins))
                    #newCoin = coinValue  
                n += 1
            #update minCoinsForThisAmount at the current cent index to be coinCount, which is either:
            #   the current cent index OR
            #   one more than the current amount (see line coinCount = minCoinsForThisAmount[amount-j]+1
            minCoinsForThisAmount[amount] = coinCount
            #print("minCoinsForThisAmount is: " + str(minCoinsForThisAmount))
            #print("usedCoins is: "+str(usedCoins))
            #print("\n\n")

            #update usedCoins at the current cent intext to be newCoin
            #   newCoin will be:
            #       1 OR
            #       coinValue
            #usedCoins[amount] = newCoin
        return minCoinsForThisAmount, usedCoins


    #printUsedCoins prints to change.txt
    #   the coinList used on the first line,
    #   the change for which change is given on the second line,
    #   and finally the quantity of each coin value used to make said change
    def printUsedCoins(self, coinList, change, minCoins, usedCoins):
        #print("In printUsedCoins")
        coin = change
        total = 0
        k = 0
        coinQty = [0] * len(coinList)
        with open("change.txt", "a") as file2:
            file2.write(str(coinList) + "\n")
            file2.write(str(change) + "\n") #Use this many of each: ")
            #file2.write("usedCoins: " + str(usedCoins) + "\n")
            temp = change
            while temp > 0:
                coinQty[usedCoins[temp]] += 1
                temp = temp - coinList[usedCoins[temp]]
            #print("coinQty is: " + str(coinQty))
            file2.write(str(coinQty))
            #while total < change:   #0 < 10
            #    while k in range(len(usedCoins)):
            #        total = total + usedCoins[k] * coinList[k]
                    
            #        print(" ")
                #file2.write(k)
                


            # while coin > 0:
            #     coinQty.insert(coin, usedCoins[coin])
            #     thisCoin = usedCoins[coin]
            #     coin = coin - thisCoin

                #thisCoin = usedCoins[coin]
                #file2.write(str(thisCoin) + " ") 
                #coin = coin - thisCoin
            #file2.write("Uses this many of each coin: " + str(coinQty))
            file2.write("\n" + str(minCoins[change]) + "\n")
            #file2.write("\n\n")
            #file2.write("END OF RUN\n\n")
        #file2.close()

class fileHandler:
    #Thanks to Matt at https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
    def silentRemove(self, filename):
        try:
            os.remove(filename)
        except OSError as error:
            if error.errno != errno.ENOENT: #if the error is something other than "no such file or directory" raise it
                raise

def main():
    parser = argparse.ArgumentParser(description="Use makeChange to identify the smallest number of coins needed to make change for a given change.  Results will be stored in change.txt.")
    parser.add_argument(default="amount.txt", nargs="?", dest="datafile", action="store", help="A path to the file containing coin values and an change on alternating lines.  Will default to change.txt if not provided.")
    args = parser.parse_args(sys.argv[1:])
    path = args.datafile
    print("Input file is: " + path)
    if(os.path.exists(path)):
        #delete any previously existing data
        #fileHandler.silentRemove("change.txt") #TODO pass fileHandler, not str
        i = 0
        coinList = [] #coinList = emptyList
        coinsUsed = []
        chavUsedCoin = []
        with open(path, "r") as file1:
            for line in file1.readlines(): #not at end of file
                i += 1 #we want i to start at 1
                #DEBUG
                #print("i is: " + str(i))
                #print("line is: " + str(line))
                #DEBUG
                if(i%2 == 1): # if i%2=1, odd line
                    #print("**i is odd: " + str(i))
                    #read first line and store in coinList
                    coinListStrArr = line.split()
                    #print("coinListStrArr is: " + str(coinListStrArr))
                    j = 0
                    for c in coinListStrArr: #.split(" "):
                        coinList.append(int(c))
                        coinsUsed.append(-1) ##
                        j += 1
                    #coinsUsed.append(-1)
                    #DEBUG
                    #print("coinList is: " + str(coinList) + "\n\n")
                    #print("*len(coinList) is: " + str(len(coinList)))
                    #DEBUG
                else: #even line
                    #print("**i is even: " + str(i))
                    #read second line and store in change
                    changeStrArr = line.split()
                    change = int(changeStrArr[0])
                    #initialize coinsUsed to all amount in the quantity "change"
                    #coinsUsed.insert(0, change)
                    #DEBUG
                    #print("change is: " + str(change))
                    #print("**len(coinList) is: " + str(len(coinList)))
                    #DEBUG
                    if(len(coinList) > 0): #if we have everything, call DP function
                        #DEBUG
                        #print("coinList is: " + str(coinList))
                        #print("change is: " + str(change))
                        #DEBUG
                        cashier = pointOfSale()
                        minCoins = []
                        for x in range(change): #all but index of "change"
                            #minCoins.append(0)
                            minCoins.append(change*100) ##
                            chavUsedCoin.append(0)
                        minCoins.append(change*100)
                        chavUsedCoin.append(0)
                        #DEBUG
                        #print("minCoins before DP is: " + str(minCoins))
                        #print("coinsUsed before DP is: " + str(coinsUsed))
                        #print("\n")
                        #DEBUG
                        minCoinsNeeded, usedCoins = cashier.makeChange(coinList, change, minCoins, chavUsedCoin)
                        cashier.printUsedCoins(coinList, change, minCoinsNeeded, usedCoins) 
                        #DEBUG
                        #print("minCoinsNeeded is: " + str(minCoinsNeeded))
                        #print("usedCoins is: " + str(usedCoins))
                        #print("\n")
                        #DEBUG 
                    coinList = [] #coinList = emptyList
                    coinsUsed = []
        file1.close()
    else:
        print("Path does not exist.  Check input file path.")
        return

if __name__ == '__main__':
    main()
