import json
import os

contacts = {}

def load_contacts():
    global contacts
    try:
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
    except Exception as e:
        print(f"Error loading contacts: {e}")

def save_contacts():
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file)
    except Exception as e:
        print(f"Error saving contacts: {e}")
