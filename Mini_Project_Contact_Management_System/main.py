# main.py
from data import save_contacts, load_contacts
from validation import validate_phone, validate_email
from actions import add_contact, edit_contact, delete_contact, search_contact, display_contacts, export_contacts, import_contacts
from menu import display_menu, handle_menu_choice

def main():
    running = True
    while running:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        running = handle_menu_choice(choice)

if __name__ == "__main__":
    main()