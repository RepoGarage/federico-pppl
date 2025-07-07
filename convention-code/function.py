from typing import List, Dict

def display_contacts_ascending(contacts: List[Dict]) -> None:
    """Display contacts sorted by name in ascending order."""
    contacts.sort(key=lambda x: x['name'])
    for idx, contact in enumerate(contacts, start = 1):
        print(f"{idx}. {contact['name']}")

def display_contacts_descending(contacts: List[Dict]) -> None:
    """Display contacts sorted by name in descending order."""
    contacts.sort(key=lambda x: x['name'], reverse=True)
    for idx, contact in enumerate(contacts, start = 1):
        print(f"{idx}. {contact['name']}")

def display_contact_names(contacts: List[Dict]) -> None:
    """Display list of contact names with option to return."""
    for idx, contact in enumerate(contacts, start = 1):
        print(f"{idx}. {contact['name']}")
    print("0. Back")
    print("===========================")

def display_contact_details(contacts: List[Dict], index: int) -> None:
    """Display details of a specific contact."""
    if 0 <= index < len(contacts):
        selected = contacts[index]
        print("===========================")
        print(f"Name    : {selected['name']}")
        print(f"Email   : {selected['email']}")
        print(f"Phone   : {selected['phone']}")
        print("===========================")
    else:
        print("===========================")
        print("Contact not found!")
        print("===========================")

def add_new_contact() -> Dict:
    """Add a new contact and return the contact dictionary."""
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    new_contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    print(f"{name} has been added successfully")
    return new_contact

def delete_contact(contacts: List[Dict]) -> None:
    """Delete a contact from the list."""
    for idx, contact in enumerate(contacts, start = 1):
        print(f"{idx}. {contact['name']}")
    print("===========================")
    user_choice = int(input("Which number do you want to delete? "))

    if 1 <= user_choice <= len(contacts):
        deleted = contacts.pop(user_choice - 1)
        print("===========================")
        print(f"{deleted['name']} has been deleted.")
    else:
        print("===========================")
        print("Contact not found!")

def search_contact(contacts: List[Dict]) -> None:
    """Search for a contact by name or phone number."""
    while True:
        print("===========================")
        print("1. Search by Name")
        print("2. Search by Number")
        print("0. Back")
        print("===========================")
        search_mode = int(input("Search mode: "))
        found = False
        
        if search_mode == 1:
            search_term = input("Search contact by name: ").lower()
            for contact in contacts:
                if search_term in contact['name'].lower():
                    print_contact_details(contact)
                    found = True
            
        elif search_mode == 2:
            search_term = input("Search contact by number: ")
            for contact in contacts:
                if search_term in contact['phone']:
                    print_contact_details(contact)
                    found = True
                    
        elif search_mode == 0:
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
            
        if not found:
            print("===========================")
            print("Contact not found")
            print("===========================")

def edit_contact(contacts: List[Dict]) -> None:
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']}")
     
    edit_choice = input("Which contact do you want to edit (enter name): ").lower()
    
    for idx, contact in enumerate(contacts, start = 1):
        if edit_choice == contact["name"].lower() or (edit_choice.isdigit() and int(edit_choice) == idx):

            old_name = contact["name"]
            old_email = contact["email"]
            old_phone = contact["phone"]
            
            print("\nPress Enter to skip and keep current value")
            print(f"Current Name: {old_name}")
            new_name = input("Enter New Name: ").strip()
            if new_name:
                contact["name"] = new_name
            else:
                contact["name"] = old_name
            
            print(f"Current Email: {old_email}")
            new_email = input("Enter New Email: ").strip()
            if new_email:
                contact["email"] = new_email
            else:
                contact["email"] = old_email
            
            print(f"Current Phone: {old_phone}")
            new_phone = input("Enter New Phone: ").strip()
            if new_phone:
                contact["phone"] = new_phone
            else:
                contact["phone"] = old_phone
            
            print("\nContact updated successfully:")
            print(f"Name  : {contact['name']}")
            print(f"Email : {contact['email']}")
            print(f"Phone : {contact['phone']}")
            return
            
    print("Contact not found.")

def print_contact_details(contact: Dict) -> None:
    """Helper function to print contact details."""
    print("===========================")
    print(f"Name    : {contact['name']}")
    print(f"Email   : {contact['email']}")
    print(f"Phone   : {contact['phone']}")