import sys
# from exceptions.NotInitialisedException import NotInitialisedException
from exceptions.ArgumentExceptions import NotEnoughArgumentException,\
    LogFileMissingException,\
    DictionaryMissingException,\
    SaveFileMissingException
from findoperation.KeyFinder import KeyFinder



try:
    resultFilePath=None
    if len(sys.argv) == 4 :
        keyFinder=KeyFinder(sys.argv[1],sys.argv[2],sys.argv[3])
        keyFinder.buildTreeFromDictionary()
        keyFinder.searchInLog()
    else:
        if len(sys.argv) == 3 :
            raise SaveFileMissingException()
        if len(sys.argv) == 2 :
            raise DictionaryMissingException()
        if len(sys.argv) == 1 :
            raise LogFileMissingException()

except SaveFileMissingException as sme :
    sme.getMessage()
    resultFilePath="Result.txt"
    print(" I will save my work to: "+resultFilePath)
    keyFinder=KeyFinder(sys.argv[1],sys.argv[2],resultFilePath)
    keyFinder.buildTreeFromDictionary()
    keyFinder.searchInLog()
except NotEnoughArgumentException as neae:
    neae.getMessage()