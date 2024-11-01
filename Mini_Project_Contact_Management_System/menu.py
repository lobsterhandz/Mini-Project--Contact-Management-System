from actions import add_contact, edit_contact, delete_contact, search_contact, display_contacts, export_contacts, import_contacts



# Module: Menu Handling
def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

def handle_menu_choice(choice):
    try:
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System! Goodbye!")
            return False
        elif choice == '9':
            print("\nYou've found the secret menu! Hello Instructor! Keep up the amazing work, and thank you for helping us become better developers!\n")
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
    except Exception as e:
        print(f"An error occurred while handling your choice: {e}")
    return True