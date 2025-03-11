class RichWord:
    def __init__(self, parola):
        self.parola = parola # this is a string
        self.corretta = None #this is a bool

    #@property
    #def corretta(self):
        # print("getter of parola called" )
        #return self.corretta

    #@corretta.setter
    #def corretta(self, boolValue):
        # print("setter of parola called" )
        #self.corretta = boolValue

    def __str__(self):
        return self.parola
