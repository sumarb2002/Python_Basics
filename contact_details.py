def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
   


def add_contact(contact_book):
    name = input("Enter name ")
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter phone number ")
    email = input("Enter Email ")
    address = input("Enter address ")
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

def view_contact(contact_book):
        name = input("Enter name ")
        if name in contact_book:
            print(f"Name: {name}")
            print(f"Phone: {contact_book[name]['phone']}")
            print(f"Email: {contact_book[name]['email']}")
            print(f"Address: {contact_book[name]['address']}")
        else:
            print("Contact not found!")    


def edit_contact(contact_book):
        name = input("Enter name ")
        if name in contact_book:
            phone = input("Enter phone number ")
            email = input("Enter Email ")
            address = input("Enter address ")
            if phone != '':
                contact_book[name]['phone'] = phone
            if email != '':
                contact_book[name]['email'] = email
            if address != '':
                contact_book[name]['address'] = address
            print("Contact updated successfully!")            
        else:
            print("Contact not found!")

def delete_contact(contact_book):
        name = input("Enter name ")
        if name in contact_book:
            del contact_book[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")  

def list_all_contacts(contact_book):
        # name = input()
        if len(contact_book.items()) != 0:
            for key,value in contact_book.items():
                print(f"Name: {key}")
                print(f"Phone: {contact_book[key]['phone']}")
                print(f"Email: {contact_book[key]['email']}")
                print(f"Address: {contact_book[key]['address']}\n")
        else:
            print("No contacts available.")

contact_book = {}
while True:
    display_menu()
    choice = input("Enter yourchoice")
    if choice == '1':
        add_contact(contact_book)
    elif choice == '2':
        view_contact(contact_book) 
    elif choice == '3':
        edit_contact(contact_book)        
    elif choice == '4':
        delete_contact(contact_book)
    elif choice == '5':
        list_all_contacts(contact_book) 
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")