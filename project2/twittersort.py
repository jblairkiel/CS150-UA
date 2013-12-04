from scanner import *
import sys

def main():
    
    tweet1 = sys.argv[1]
    tweet2 = sys.argv[2]

    print("Reading files...")
    longestTweet(scanMain(tweet1),scanMain(tweet2))
    print("Merging files...")
    merge(scanMain(tweet1),scanMain(tweet2))
    print("Writing files...")
    data(merge(scanMain(tweet1),scanMain(tweet2)))
    print("Files Written. Dislplaying 5 earliest tweeters and tweets")
    reverseTweets(merge(scanMain(tweet1),scanMain(tweet2)))

def scanMain(filename):

    s = Scanner(filename) 
    return scannerToArray(s)
    
def recordToArray(s):

    name = s.readtoken()
    if (name == ''):
        return ''
    name = name[1:]
    tweet = s.readstring()
    year = s.readint()
    month = s.readint()
    day = s.readint()
    time = s.readtoken()
    return [name,tweet,year,month,day,time]

def scannerToArray(s):
   
    table = []
    record = recordToArray(s)
    while (record != ""):
        table.append(record)
        record = recordToArray(s) 
    return table

def merge(array1,array2):
    array3 = []
    i = 0
    j = 0
    while (i < len(array1) and j < len(array2)):
        if (array1[i] < array2[j]):
            array3.append(array1[i])
            i = i+1
        else:
            array3.append(array2[j])
            j = j+1
    return array3 + array1[i:] + array2[j:] 

def longestTweet(array1,array2):

    if (len(array2)<len(array1)):
        print("tweet1.txt contained the most tweets with", len(array1),".")
    else:
        print("tweet2.txt contained the most tweets with", len(array2),".")

def data(mergedFile):

    out = open("output.txt","w")
    count = 0
    while (count != len(mergedFile)):
        for i in range(0, len(mergedFile), 1):
            a = mergedFile[i]
            handle = a[0] 
            tweet = a[1]
            year = a[2]
            month = a[3]
            day = a[4]
            time = a[5]  
            out.write(handle)
            out.write("\t")
            out.write(tweet)
            out.write("\t")
            out.write(repr(year)+ ' ')
            out.write(repr(month)+ ' ')
            out.write(repr(day)+ ' ')
            out.write((repr(time)[1:-1])+'\n')
            count = count +1 
    out.close()

def reverseTweets(mergedFile):
    
        a = list(reversed(mergedFile))
        for i in range(0,5,1):
            handle = a[i][0]
            tweet = a[i][1]
            topFive = repr(handle) + " " + repr(tweet)
            newtopFive = topFive.replace("'","")
            print(newtopFive) 
    
        
main()
