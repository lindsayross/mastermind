from flask import jsonify
from cloudant import Cloudant
import os, json

def get_doc(db, document):
    doc = [doc for doc in list(map(lambda doc: doc, db)) if document in doc][0]
    return doc[document]

def get_users(db):
    users = get_doc(db, 'users')
    return users
    

def get_user(db, user_id):
    users = get_users(db)
    for user in users:
        if user['_id'] == user_id:
            return user
    return {}

def put_user(db, user):
    data = {'users': user}
    #  db.create_document(data)
    return user

def get_matches(db, user_id):
    properties = get_doc(db, 'properties')
    matches = []
    return properties
#  def update_user(db, user_id, update):
#      doc = get_doc(db)
#      user = [u for u in doc if u['id'] == user_id]
#      for key in update.keys():
#          user[key] = update[key]
#      print(user)
