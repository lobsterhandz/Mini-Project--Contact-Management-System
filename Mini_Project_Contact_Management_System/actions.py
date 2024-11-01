from data import contacts, save_contacts
from validation import validate_phone, validate_email

def add_contact():
    try:
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        while not validate_phone(phone):
            print("Invalid phone number format. Please enter a valid phone number.")
            phone = input("Enter the phone number: ")
        
        email = input("Enter the email: ")
        while not validate_email(email):
            print("Invalid email format. Please enter a valid email.")
            email = input("Enter the email: ")

        address = input("Enter the address: ")
        notes = input("Enter additional notes: ")
        contacts[email] = {'name': name, 'phone': phone, 'address': address, 'notes': notes}
        save_contacts()
        print(f"Contact for {name} added!")
    except Exception as e:
        print(f"Error adding contact: {e}")


def edit_contact():
    try:
        identifier = input("Enter the email of the contact to edit: ")
        if identifier in contacts:
            print(f"Editing contact for {contacts[identifier]['name']}. Leave blank if no change needed.")
            new_name = input(f"Enter the new name (current: {contacts[identifier]['name']}): ")
            new_phone = input(f"Enter the new phone number (current: {contacts[identifier]['phone']}): ")
            if new_phone and not validate_phone(new_phone):
                print("Invalid phone number format. No changes made to the phone number.")
            elif new_phone:
                contacts[identifier]['phone'] = new_phone

            new_email = input(f"Enter the new email (current: {identifier}): ")
            if new_email and not validate_email(new_email):
                print("Invalid email format. No changes made to the email.")
            elif new_email:
                contacts[new_email] = contacts.pop(identifier)
                identifier = new_email

            new_address = input(f"Enter the new address (current: {contacts[identifier]['address']}): ")
            new_notes = input(f"Enter the new notes (current: {contacts[identifier]['notes']}): ")
            if new_name:
                contacts[identifier]['name'] = new_name
            if new_address:
                contacts[identifier]['address'] = new_address
            if new_notes:
                contacts[identifier]['notes'] = new_notes
            save_contacts()
            print(f"Contact for {contacts[identifier]['name']} updated!")
        else:
            print(f"Contact not found.")
    except Exception as e:
        print(f"Error editing contact: {e}")


def delete_contact():
    try:
        identifier = input("Enter the email of the contact to delete: ")
        if identifier in contacts:
            del contacts[identifier]
            save_contacts()
            print(f"Contact deleted!")
        else:
            print(f"Contact not found.")
    except Exception as e:
        print(f"Error deleting contact: {e}")


def search_contact():
    try:
        identifier = input("Enter the email of the contact to search for: ")
        if identifier in contacts:
            info = contacts[identifier]
            print(f"Contact for {info['name']}: Phone: {info['phone']}, Email: {identifier}, Address: {info['address']}, Notes: {info['notes']}")
        else:
            print(f"Contact not found.")
    except Exception as e:
        print(f"Error searching contact: {e}")


def display_contacts():
    try:
        if contacts:
            print("All Contacts:")
            for identifier, info in contacts.items():
                print(f"{info['name']}: Phone: {info['phone']}, Email: {identifier}, Address: {info['address']}, Notes: {info['notes']}")
        else:
            print("No contacts found.")
    except Exception as e:
        print(f"Error displaying contacts: {e}")


def export_contacts():
    file_name = input("Enter the file name to export contacts to: ")
    try:
        with open(file_name, "w") as file:
            for identifier, info in contacts.items():
                file.write(f"{info['name']},{info['phone']},{identifier},{info['address']},{info['notes']}\n")
        print(f"Contacts exported to {file_name}!")
    except Exception as e:
        print(f"Failed to export contacts: {e}")
    finally:
        print("Export operation completed.")


def import_contacts():
    file_name = input("Enter the file name to import contacts from: ")
    try:
        with open(file_name, "r") as file:
            for line in file:
                name, phone, email, address, notes = line.strip().split(",")
                if validate_phone(phone) and validate_email(email):
                    contacts[email] = {'name': name, 'phone': phone, 'address': address, 'notes': notes}
                else:
                    print(f"Invalid data format for contact {name}. Skipping.")
        save_contacts()
        print(f"Contacts imported from {file_name}!")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"Failed to import contacts: {e}")
    finally:
        print("Import operation completed.")
