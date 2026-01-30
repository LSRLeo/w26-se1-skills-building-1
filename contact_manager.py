"""
Project:Contact Manager

User can add, list, and search the contacts json file with commands.
Contacts are sorted using dictionary and have phone number as the
unique key.

"""
import argparse
import json
CONTACTS = "contacts.json"

def load():
    try:
        with open(CONTACTS, "r") as f:
            texts = json.load(f)
            if not isinstance(texts, dict):
                texts = {} #return empty dict if file is empty or not a dictionary
            return texts
    except FileNotFoundError:
        return {} # Return empty dict if file does not exist
    except json.JSONDecodeError:
        return {} # Return empty dict if file is corrupted

def save_contacts(contacts):
    with open(CONTACTS, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, email, phone):
    contacts = load()
    if phone.strip() in contacts:
        print(f"Contact with phone number {phone.strip()} already exists.")
        return
    
    contacts[phone.strip()] = {"name": name.strip(), 
                                    "email": email.strip()}
    
    save_contacts(contacts)
    print(f"Contact {name.strip()} added successfully.")


def list_contacts():
    contacts = load()
    if not contacts:
        print("No contacts available.")
        return
    
    for phone, info in contacts.items():
        print(f"Phone: {phone}, Name: {info['name']}, Email: {info['email']}")


def search_contact(name):
    contact = load()
    name = name.strip().lower()

    for phone, info in contact.items():
        if name in info['name'].lower():
            print(f"Contact found - Phone: {phone}, Name: {info['name']}, Email: {info['email']}")
            return
    
    print(f"No contact found with the name {name}.")

def main():
    parser = argparse.ArgumentParser(description="Contact Manager")
    sub = parser.add_subparsers(dest="command", required=True)

    # Add contact command
    add_parser = sub.add_parser("add", help="Add a new contact")
    add_parser.add_argument("--name", required=True, help="Name of the contact")
    add_parser.add_argument("--email", required=True, help="Email of the contact")
    add_parser.add_argument("--phone", required=True, help="Phone number of the contact")

    # List contacts command
    list_parser = sub.add_parser("list", help="List all contacts")

    # Search contact command
    search_parser = sub.add_parser("search", help="Search for a contact")
    search_parser.add_argument("--name", required=True, help="Name of the contact to search for")

    args = parser.parse_args()


    if args.command == "add":
        add_contact(args.name, args.email, args.phone)
    elif args.command == "list":
        list_contacts()
    elif args.command == "search":
        search_contact(args.name)






if __name__ == "__main__":
    main()