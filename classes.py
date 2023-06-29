from collections import UserDict


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        return f"Contact {record.name.value} add successful"

    def del_record(self, record):
        self.data.pop(record.name.name)


class Field:
    def __init__(self, value) -> None:
         self.value = value


class Name(Field):
    ...


class Phone(Field):
    ...
        

class Record:
    
    def __init__(self, name: Name, phone: Phone=None):
        self.phones = []
        self.name = name
        if phone:
                self.phones.append(phone)
           
    def add_phone(self, phone: Phone):
            self.phones.append(phone)   
   
    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for index, phone in enumerate(self.phones):
            if phone.value == new_phone:
                self.phones.pop(index)
                self.add_phone(new_phone)
                return f"Change phone {old_phone.value} to {new_phone.value}"
        return f"No phone {old_phone.value} for contact {self.name.value}"

    # def del_phone(self):
    #     self.phones.clear()