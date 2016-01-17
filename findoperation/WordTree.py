__author__ = 'mohika'


class Node:
    def __init__(self,char):
        self.__char=char
        self.__childs=dict()
        self.__wordEnd=False


    def getChilds(self)->dict:
        return self.__childs

    def getChar(self):
        return self.__char

    def getWordEnd(self):
        return self.__wordEnd

    def addChild(self,node):
        self.__childs[node.getChar()]=node

    def setWordEnd(self,wordEnd:bool):
        self.__wordEnd=wordEnd

    def getChildWithKey(self,key:str):
        return self.__childs.get(key)

class WordTree:

    def __init__(self):
        self.root = Node("")

    def addWord(self,string:str):
        self._addCharToTree(self.root,string,0)

    def _addCharToTree(self,parent:Node,word:str,index:int):
        child=parent.getChildWithKey(word[index])
        lastChar= (index == len(word)-1)

        if child is None:
            child= Node(word[index])
            parent.addChild(child)

        child.setWordEnd(lastChar)

        if not lastChar:
            self._addCharToTree(child,word,index+1)

    def writeTree(self):
        self.writeCharFromTree(self.root,"")

    def writeCharFromTree(self,node:Node,spaces:str):
        print(spaces+node.getChar())
        for char,iNode in node.getChilds().items() :
            self.writeCharFromTree(iNode,spaces+" ")

    def contain(self,word):
        return self.compareChars(self.root,word,0)

    def compareChars(self,parent:Node,word:str,index:int):
        child=parent.getChildWithKey(word[index])
        if child is None:
            return False
        else :
            if index is len(word)-1 :
                return child.getWordEnd()
            else :
                return self.compareChars(child,word,index+1)

    def addWords(self,listOfWords:list):
        for word in listOfWords:
            self.addWord(word)