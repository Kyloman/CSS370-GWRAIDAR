#Class description
#Admin makes the parsing request on this page, and the log file would get parsed and generate the WvW Encounter object.

#Required interface
#LogFile getLogFile()

#Parameters
# 1. LogFile: Log File is required to know which file to parse.

class LogParserPage:
    
    def parseLog(LogFile file):
        pass

    # passes in the wvw encounter log file and filters out wvw data
    def logFilter():
        pass