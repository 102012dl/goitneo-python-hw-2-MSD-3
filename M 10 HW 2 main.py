\ GoIT Модуль 10

\ Домашнє завдання 02 

\ Завдання №1


def input_error(func):
    """Decorator to handle ValueError, IndexError, and KeyError."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Index out of range. Please enter valid input."
        except KeyError:
            return "Key not found. Please try again."
    return inner

@input_error
def add_contact(args, contacts):
    """Add a contact to the contacts dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def delete_contact(name, contacts):
    """Delete a contact from the contacts dictionary."""
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    else:
        return "Contact not found. Please enter a valid name."

@input_error
def find_contact(name, contacts):
    """Find and return a contact from the contacts dictionary."""
    if name in contacts:
        return f"Contact found - {contacts[name]}"
    else:
        return "Contact not found. Please enter a valid name."

@input_error
def list_contacts(contacts):
    """List all contacts in the contacts dictionary."""
    if contacts:
        contact_list = ', '.join([f"{name}: {phone}" for name, phone in contacts.items()])
        return f"Contacts: {contact_list}"
    else:
        return "No contacts available."

contacts = {}

while True:
    command = input("Enter command: ")
    if command == "add":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        print(add_contact((name, phone), contacts))
    elif command == "delete":
        name = input("Enter name to delete: ")
        print(delete_contact(name, contacts))
    elif command == "find":
        name = input("Enter name to find: ")
        print(find_contact(name, contacts))
    elif command == "list":
        print(list_contacts(contacts))
    else:
        print("Invalid command. Please try again.")




\ Завдання №2 


from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Testing functionality
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
