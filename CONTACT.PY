class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("NO CONTACTS FOUND.")
            return
        print("\nCONTACT LIST:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        found_contacts = [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone]
        if found_contacts:
            print("\nSEARCH RESULTS:")
            for contact in found_contacts:
                print(f"{contact.name} - {contact.phone}")
        else:
            print("NO CONTACTS FOUND MATCHING THE QUERY.")

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            print("CONTACT UPDATED SUCCESSFULLY.")
        else:
            print("INVALID INDEX. CONTACT NOT FOUND.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("CONTACT DELETED SUCCESSFULLY.")
        else:
            print("INVALID INDEX. CONTACT NOT FOUND.")

def main():
    manager = ContactManager()

    while True:
        print("\nCONTACT MANAGEMENT SYSTEM")
        print("1. ADD CONTACT")
        print("2. VIEW CONTACTS")
        print("3. SEARCH CONTACT")
        print("4. UPDATE CONTACT")
        print("5. DELETE CONTACT")
        print("6. EXIT")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(Contact(name, phone, email, address))
            print("CONTACT  ADDED SUCCESSFULLY.")
        
        elif choice == '2':
            manager.view_contacts()
        
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(manager.contacts):
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                manager.update_contact(index, Contact(name, phone, email, address))
            else:
                print("INVALID INDEX. CONTACT NOT FOUND.")
        
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: ")) - 1
            manager.delete_contact(index)
        
        elif choice == '6':
            print("EXITING THE CONTACT MANAGMENT SYSTEM.")
            break
        
        else:
            print("INVALID CHOICE. PLEASE SELECT A VALID OPTION.")

if __name__ == "__main__":
    main()
