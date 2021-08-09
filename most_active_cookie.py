import sys
from collections import Counter
"""
Finds the most active cookie(s) (the most visited cookie) from a file log and prints 
them to stdout. If there is a tie, then all cookies that have max occurences is printed.
"""
class mostActiveCookie(object):
    """
    Parses the command line for the file name and the target date. If they are not present or the 
    command line arguments are not formatted correctly, exit with an error message.
    """
    def parseCommandLine(self):
        try:   
            logFileName = sys.argv[1]
            targetDate = sys.argv[3]
            return logFileName, targetDate
        except:
            print("Unexpected Error: Log file and date required")
            sys.exit(1)

    """
    Parses the file for any dates that are the same as the target date and stores them in a counter.
    Return counter after parsing the entire file. If the file name is invalid, exit with an error message
    """
    def parseFile(self, logFileName, targetDate):
        activeCookies = Counter()
        try:
            with open(logFileName) as logFile:
                for line in logFile:
                    if targetDate in line:
                        parsedLine = line.split(",",1)
                        cookie = parsedLine[0]
                        activeCookies[cookie] += 1
            return activeCookies
        except:
            print("Unexpected Error: \"{}\" doesn't exist.".format(logFileName))
            sys.exit(1)
            
    #Finds the most active cookie(s) and adds them to a list to be printed to stdout
    def findMostActiveCookie(self):
        logFileName, targetDate = self.parseCommandLine()               #Get the file name and target date
        activeCookies = self.parseFile(logFileName, targetDate)         #Parse the file and return a counter of all the cookies that were visited on the target date
        if not activeCookies:
            print("No active cookies on targetted date.")
            return   
        cookieVisits = list(activeCookies.values())                     #Create a list of just the number of visits of each cookie
        maxVisits = max(cookieVisits)                                   #Find the max amount of visits
        maxVisitCount = cookieVisits.count(maxVisits)                   #Count the number of cookies that have the amount of max visits
        mostActiveCookies = activeCookies.most_common(maxVisitCount)    #Create a list of all the cookies that have max visits 
        for cookie in mostActiveCookies:
            print(cookie[0])

mostActiveCookie().findMostActiveCookie()