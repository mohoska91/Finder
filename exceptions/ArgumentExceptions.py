class NotEnoughArgumentException(Exception):

    def __init__(self):
        self.__message="NotEnough"

    def getMessage(self)->str:
        return self.__message
    pass



class SaveFileMissingException(NotEnoughArgumentException):

    def getMessage(self)->str:
        return "SaveFile "+super().getMessage()

    pass

class LogFileMissingException(NotEnoughArgumentException):

    def __str__(self):
       return 'LogFileMissingException '+super().__str__()

    def __repr__(self):
        return 'LogFileMissingException '+super().__repr__()


    def getMessage(self)->str:
        return self.__str__()+super().getMessage()

    pass

class DictionaryMissingException(NotEnoughArgumentException):

    def __str__(self):
        return 'DictionaryMissingException'+super().__str__()

    def __repr__(self):
        return 'DictionaryMissingException'+super().__repr__()


    def getMessage(self)->str:
        return self.__str__()+super().getMessage()

    pass