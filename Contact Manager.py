class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def display_contacts(self):
        print("\nContacts:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self, search_name):
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                print(f"Contact found - Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
                return
        print(f"No contact found with the name '{search_name}'.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            new_contact = Contact(name, phone, email)
            contact_manager.add_contact(new_contact)
        elif choice == '2':
            contact_manager.display_contacts()
        elif choice == '3':
            search_name = input("Enter the name to search: ")
            contact_manager.search_contact(search_name)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
