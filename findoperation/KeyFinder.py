from fileoperation.FileReader import FileReader
from fileoperation.FileWriter import FileWriter
from findoperation.WordTree import WordTree
import os

class KeyFinder:

    def __init__(self,logPath:str,dictPath:str,savePath):
        self._logPath=logPath
        self._dictPath=dictPath
        self._savePath=savePath
        self._wordTree=WordTree()


    def buildTreeFromDictionary(self):
        fileReader=FileReader()
        fileReader.initialize(self._dictPath)
        line=fileReader.lineRead()
        while line is not '':
            line=line.rstrip()
            self._wordTree.addWord(line)
            line=fileReader.lineRead()

    def searchInLog(self):
        fileReader=FileReader()
        fileReader.initialize(self._logPath)
        fileWriter=FileWriter()
        fileWriter.initialize(self._savePath)
        line=fileReader.lineRead()
        while line is not '':
            line=line.rstrip()
            keyInLine=False
            listOfLogWords=line.split(" ")
            i=0
            while i < len(listOfLogWords) and not keyInLine:
                keyInLine=self._wordTree.contain(listOfLogWords[i])
                i+=1
            if keyInLine:
                fileWriter.writeToFile(line)
            line=fileReader.lineRead()