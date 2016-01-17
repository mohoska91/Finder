from exceptions.NotInitialisedException import NotInitialisedException


class FileWriter:

    def __init__(self):
        self.__savePath = None
        self.__file = None

    def __del__(self):
        if self.file is not None:
            self.file.close()

    def initialize(self,path:str,append=True):

        try:
            self.__savePath=path
            mode='a'

            if append is not True:
                mode='w'

            self.file = open(self.__savePath,mode)
            return True
        except IOError:
            print(str(IOError)+" in FileWriter")
            return False



    def writeToFile(self,toWrite:str):
        if self.file is None:
            raise NotInitialisedException
        print(toWrite,file=self.file)
