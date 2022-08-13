from fastapi import FastAPI
from functions import Trick
import shelve
import json
app = FastAPI()

#command to start API: uvicorn main:app --reload

@app.get("/trick/{trick_name}")
def trick_stats(trick_name):
    db = shelve.open('tricksdb')
    if trick_name in db.keys():
        object = db[trick_name].stats()
    else:
        object = "Trick not found"
    db.close()
    return object

@app.post("/new_trick/{trick_name}")
def create_trick(trick_name):
    db = shelve.open('tricksdb')
    if trick_name not in db.keys():
        trick = Trick(trick_name,0,0)
        db[trick_name] = trick
        object = trick_name + " created"
    else:
        object = trick_name + " already exists"
    db.close()
    return object


@app.put("/clean_trick/{trick_name}")
def create_trick(trick_name):
    db = shelve.open('tricksdb')
    if trick_name in db.keys():
        object = db[trick_name].clean()
    else:
        object = "Trick not found"
    db.close()
    return object


@app.post("/add_session/{trick_name}")
def add_session(trick_name,corrects,total):

    object = "Trick not found"
    
    db = shelve.open('tricksdb')
    if trick_name in db.keys():
        db[trick_name] = db[trick_name].add(corrects,total)
        object = db[trick_name].stats()
    else:
        trick = Trick(trick_name,corrects,total)
        db[trick_name] = trick
        object = "Trick not found - Creating new one"
    
    db.close()
    return object
    
   