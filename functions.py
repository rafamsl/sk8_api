import shelve
class Trick():

    def __init__(self,name,corrects,total):
        self.name = name
        self.corrects = int(corrects)
        self.total = int(total)


    def stats(self):
        return self.name + " " + str(self.corrects) + "/" + str(self.total)

    def add(self,corrects,total):
        self.corrects += int(corrects)
        self.total += int(total)
        return self
    
    def clean(self):
        self.corrects = 0
        self.total = 0
        return self

db = shelve.open('tricksdb')

print("Number of Records : " + str(len(db)))
print(list(db.keys()))

for key in db:
    print (key, '=>', db[key].stats())

# for key in db:
#     print (key, '=>', db[key])

# for key in db:
#     db[key] = db[key].add(3,7)

# for key in db:
#     print (key, '=>', db[key].stats())

db.close()