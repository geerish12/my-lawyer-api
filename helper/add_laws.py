import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service-account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# load from json file
import json
with open('data/constitution.json') as json_file:
    data = json.load(json_file)


root_ref = db.collection("constitution")
add_data_to_firestore(data, root_ref)