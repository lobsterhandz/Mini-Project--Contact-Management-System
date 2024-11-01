# Contact Management System

## Overview

This is a simple command-line Contact Management System written in Python. It allows users to add, edit, delete, search, display, export, and import contacts through a user-friendly CLI interface. The application stores contact information such as name, phone number, email, address, and additional notes in a persistent JSON file.

### Features:
- **Add a New Contact**: Add contact details including name, phone, email, address, and notes.
- **Edit an Existing Contact**: Update the contact information for an existing contact.
- **Delete a Contact**: Delete contact details permanently.
- **Search for a Contact**: Search for a contact by email address and display their details.
- **Display All Contacts**: Display the full list of saved contacts.
- **Export Contacts**: Export contact data to a CSV text file.
- **Import Contacts**: Import contacts from a CSV text file to the system.
- **Secret Menu**: Enter `9` as a choice for a surprise (Easter egg for instructors).

## How to Run the Application

1. **Clone the Repository**: If the source code is in a repository, clone it to your local machine.
2. **Navigate to the Project Folder**: Use your terminal to navigate to the folder containing the code.
3. **Run the Application**: Execute the `main.py` script using Python:
   ```
   python main.py
   ```

## How to Use

1. When you run the application, you will see a menu of options.
2. Choose an option by entering the corresponding number.
3. Follow the prompts to add, edit, delete, search, or display contacts.
4. To quit the application, enter `8`.
5. To access the secret Easter egg, enter `9` (note that this option is not shown in the menu).

### Example Usage:
- To add a new contact, choose option `1` and provide the requested information.
- To delete a contact, choose option `3` and enter the contact's email.
- To export all contacts to a CSV file, choose option `6` and specify the file name.

## Contact Data Structure
- **Name**: Contact's name.
- **Phone**: Contact's phone number (validated format).
- **Email**: Contact's email address (validated format).
- **Address**: Physical address of the contact.
- **Notes**: Additional notes or information.

## Error Handling
- The system includes error handling to manage scenarios such as incorrect phone or email formats, missing files during imports, or unexpected errors during operations.

## Dependencies
- **Python 3.x**
- Standard library modules: `json`, `os`, `re`

No additional packages are required beyond the Python standard library.

## Code Structure
- **Data Persistence**: Handles saving and loading contacts from `contacts.json`.
- **Input Validation**: Functions to validate phone numbers and emails.
- **Contact Management Actions**: Functions to add, edit, delete, search, display, import, and export contacts.
- **Menu Handling**: Functions to display the menu and handle user choices.

## Contributing
Feel free to contribute by forking the repository, making changes, and creating a pull request. Suggestions and improvements are always welcome.

## License
This project is licensed under the MIT License.

## Acknowledgments
Thank you to the instructors for providing valuable feedback and guidance throughout the development of this project.

### Easter Egg
To my instructor: You've found the secret menu! Keep up the amazing work, and thank you for helping us become better developers!

