from fastapi import FastAPI
import json
app = FastAPI()


@app.get("/trick/{trick_name}")
def trick_stats(trick_name):
    f = open('tricks.json')
    data = json.load(f)
    f.close()
    for item in data:
        if trick_name in item:
            for key in item:
                correct = item[key]["corrects"]
                total = item[key]["total"]
                return key + " " + str(correct) + "/" + str(total)
    return "Trick not found"

@app.get("/new_trick/{trick_name}")
def create_trick(trick_name):
    dic = {trick_name: {"corrects" : 0, "total" : 0}}
    f = open('tricks.json', "r")
    data = json.load(f)
    f.close()
    for item in data:
        if trick_name in item:
            return f"{trick_name} already exists"
    data.append(dic)
    f = open('tricks.json', 'w')
    json.dump(data,f)
    f.close()
    return f"{trick_name} saved"

@app.get("/delete_trick/{trick_name}")
def create_trick(trick_name):
    f = open('tricks.json', "r")
    data = json.load(f)
    f.close()
    for item in data:
        if trick_name in item:
            data.remove(item)
    f = open('tricks.json', 'w')
    json.dump(data,f)
    f.close()
    return f"{trick_name} deleted"

@app.get("/add_session/{trick_name}")
def add_session(trick_name,corrects,total):
    object = "Trick not found"
    f = open('tricks.json', "r")
    data = json.load(f)
    f.close()
    for item in data:
        if trick_name in item:
            for key in item:
                item[key]["corrects"] += int(corrects)
                item[key]["total"] += int(total)
                object = trick_name + " updated! New stats = " + str(item[key]["corrects"]) + "/" + str(item[key]["total"])
            
    f = open('tricks.json', 'w')
    json.dump(data,f)
    f.close()
    return object
    


