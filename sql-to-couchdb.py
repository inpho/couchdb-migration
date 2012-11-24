### This script is made to go through each of the inpho Entity objects in the current db
### and create an entry in the couchdb with each entities json object.

from inpho.model import *
import json
import couchdb

print "Connecting to server."
couch = couchdb.Server()

print "Creating database: inpho-db"
db = couch.create('inpho-db')

print "Loading all entity JSON objects into new database..."
print "This is going to take a while..."
entities = Session.query(Entity).all()
for entity in entities:
    index = 'inpho:' + str(entity.ID)
    db[index] = json.loads(entity.json())

print "Database filled successfully! :)"
