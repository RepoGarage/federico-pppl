import function

def main():
    """Main program for contact management system."""
    contacts = [
        {
            "name": "Mashu",
            "email": "federicomatthewpratamaa@gmail.com",
            "phone": "00000"
        },
        {
            "name": "Arthur",
            "email": "arthur@gmail.com",
            "phone": "2221112"
        },
        {
            "name": "Badut",
            "email": "anjingkaubadutbeban@gmail.com",
            "phone": "12121131"
        },
        {
            "name": "Jefferey",
            "email": "jeffereymonyet@gmail.com",
            "phone": "12345"
        }
    ]

    while True:
        print("===========================")
        print("# Menu")
        print("1. Contact List (Ascending)")
        print("2. Contact List (Descending)")
        print("3. Contact Details")
        print("4. Add Contact")
        print("5. Edit Contact")
        print("6. Delete Contact")
        print("7. Search Contact")
        print("0. Exit")
        print("===========================")

        try:
            menu = input("Choose menu: ")

            if menu == "0":
                break

            elif menu == "1":
                function.display_contacts_ascending(contacts)
                
            elif menu == "2":
                function.display_contacts_descending(contacts)

            elif menu == "3":
                while True:
                    function.display_contact_names(contacts)
                    contact_choice = input("Select Contact Number (0 to go back): ")
                    
                    if not contact_choice.isdigit():
                        print("Please enter a valid number!")
                        continue
                        
                    contact_number = int(contact_choice)
                    if contact_number == 0:
                        break
                    
                    function.display_contact_details(contacts, contact_number - 1)

            elif menu == "4":
                new_contact = function.add_new_contact()
                contacts.append(new_contact)
                
            elif menu == "5":
                function.edit_contact(contacts)

            elif menu == "6":
                function.delete_contact(contacts)

            elif menu == "7":
                function.search_contact(contacts)
            
            else:
                print("Please select a valid menu option (0-7)!")

        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
    print("Thank you for using the contact manager!")