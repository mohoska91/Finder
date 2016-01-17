from exceptions.NotInitialisedException import NotInitialisedException

class FileReader:

    def __init__(self):
        self.file = None
        self.__path = None

    def __del__(self):
        if self.file is not None:
            self.file.close()

    def initialize(self,path:str)->bool:

        try:
            self.__path=path
            self.file = open(self.__path,'r')
            return True
        except IOError:
            print(str(IOError)+" in FileReader")
            return False

    def reInitialize(self,path:str)->bool:
        if self.file is not None:
            self.file.close()
        self.initialize(path)

    def listFromFile(self)->str:
        if self.file is None:
            raise NotInitialisedException
        try:
             for line in self.file:
                yield line
        except IOError:
              print(str(IOError)+" in FileReader")


    def lineRead(self)->str:
        if self.file is None:
            raise NotInitialisedException

        return self.file.readline()