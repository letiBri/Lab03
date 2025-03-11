class Dictionary:
    def __init__(self):
        self.dict = [] #lista di tutte le parole del dizionario

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            y = file.read()
            self.dict = y.split("\n")

    def printAll(self):
        pass


    #@property
    #def dict(self):
        #return self.dict
