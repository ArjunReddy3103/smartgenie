# firebase.py
import firebase_admin
from firebase_admin import credentials, firestore
import os

firebase_app = None

def init_firebase():
    global firebase_app
    if not firebase_app:
        cred_path = os.path.join(os.getcwd(), "fire_base_key.json")
        cred = credentials.Certificate(cred_path)
        firebase_app = firebase_admin.initialize_app(cred)
    return firestore.client()
