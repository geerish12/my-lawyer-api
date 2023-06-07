import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("service-account.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Load data from JSON file with explicit character encoding
with open('data/constitution2.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Iterate over the data and add documents to Firestore
for article, content in data.items():
    doc_ref = db.collection("constitutions").document(article)
    doc_ref.set({
        "information": content
    })
    print("Added: " + article)