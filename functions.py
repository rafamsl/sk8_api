import shelve
class Trick():

    def __init__(self,name,corrects,total):
        self.name = name
        self.corrects = corrects
        self.total = total


    def stats(self):
        return self.name + " " + str(self.corrects) + "/" + str(self.total)

    def add(self,corrects,total):
        self.corrects += int(corrects)
        self.total += int(total)
        return self.stats()
    
    def clean(self):
        self.corrects = 0
        self.total = 0
        return self.stats()