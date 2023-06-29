from collections import UserDict
from faker import Faker
from faker.providers import phone_number


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.name] = record

    def del_record(self, record):
        self.data.pop(record.name.name)
    
class Field:
    pass

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
        

class Record:
    
    def __init__(self, name: Name, phone: Phone = None):
        self.phones = []
        self.name = name
        if phone:
                self.phones.append(phone)
           
    def add_phone(self, phone: Phone):
            self.phones.append(phone)   
   
    def change_phone(self, value : Phone):
        self.phones.clear()
        self.phones.append(value)
        
    def del_phone(self):
        self.phones.clear()

address_book = AddressBook()   
answers = ["How can I help you?", "Good bye!"]
commands = ["hello", ["good bye", "close", "exit", "bye", "esc", "q"], "add", "change", "phone", "del", "kill", "show all"]

def proverka( a, n):
    command = a.split(" ")
    m = len(command)
    if m >= n:
        try :
            return command[1].capitalize(), command[2]
        except IndexError:
            return command[1].capitalize() , None
        

def reply(command):
    
    bot=True
    operator=command.lower().split(" ")
    
    if command.lower() in commands[1]:
        print(answers[1])
        bot = False
    
    elif command.lower() == commands[0]:
        print(answers[0])
        
    elif command.lower() == "show all" :
        show_all()
        
    elif operator[0] == "add":
        
        try :
            name, phone = proverka(command, 2)
            if name in address_book.keys():
                if phone:
                    address_book.get(name).add_phone(Phone(phone))
                    print(f"Телефон с номером \033[34m{phone}\033[0m добавлен к контакту \033[34m{name}\033[0m")
                else:
                    print(f'Для добавления номера к контакту \033[34m{name}\033[0m добавьте в команду телефон')    
            else:
                if phone:
                    record = Record(Name(name), Phone(phone))
                    address_book.add_record(record)
                    print(f"Контакт \033[34m{name}\033[0m с номером \033[34m{phone}\033[0m добавлен в вашу книгу")
                else:
                    record = Record(Name(name))
                    address_book.add_record(record)
                    print(f"Контакт \033[34m{name}\033[0m добавлен в вашу книгу")
        except TypeError:
            print(f"Добавьте имя в команду \033[34madd\033[0m по шаблону: \033[34m<add [name] [*phone]>\033[0m")
        
    elif operator[0] == "change":
        
        try:
            name, phone = proverka(command, 3)
            
            if name in address_book.keys():
                address_book.get(name).change_phone(Phone(phone))
                print(f"Номер телефона контакта \033[34m{name}\033[0m изменен на номер: \033[34m{phone}\033[0m")
            else:
                print(f"В вашей книге отсутствует контакт с именем \033[31m{name}\033[0m")
            
        except TypeError:
            print(f"Введите правильно команду \033[34mchange\033[0m по шаблону : \033[34m<change [name] [phone]>\033[0m")
    
    elif operator [0] == "phone":
        
        try:
            name = operator[1].capitalize() 
            
            if name in address_book.keys():
                name_phones = address_book.get(name)
                print(f'Имя: \033[34m{name}\033[0m, телефон(ы): \033[34m{", ".join(list(value.phone for value in name_phones.phones))}\033[0m')
        
            else:
                print(f"Не могу дать номер несуществующего контакта \033[31m{name}\033[0m из вашей книги")
        except IndexError:
            print(f"Введите правильно команду \033[34mphone\033[0m по шаблону : \033[34m<phone [name]>\033[0m ")
        
    elif  operator[0] == "del":
        
        try:
            name = operator[1].capitalize() 
            
            if name in address_book.keys():
                address_book.get(name).del_phone()
                print(f"Номер телефона контакта \033[34m{name}\033[0m удален")
            else:
                print(f"Не могу удалить номер несуществующего контакта \033[31m{name}\033[0m из вашей книги")
        except IndexError:
            print(f"Введите правильно команду \033[34mdel\033[0m по шаблону : \033[34m<del [name]>\033[0m ")
    
    elif  operator[0] == "kill":
        
        try:
            name = operator[1].capitalize() 
            
            if name in address_book.keys():
                address_book.del_record(address_book.get(name))
                print(f"Контакт \033[34m{name}\033[0m удален из вашей книги")
            else:
                print(f"Не могу удалить несуществующий контакт \033[31m{name}\033[0m из вашей книги")
        except IndexError:
            print(f"Введите правильно команду \033[34mdel\033[0m по шаблону : \033[34m<kill [name]>\033[0m ")
         
    else:
        print(f'Введите правильную команду :\033[34m{commands[0]}, {" ,".join(commands[2:])}\033[0m или \033[34m{", ".join(commands[1])}\033[0m для выхода')
    return bot

def show_all():
    print(f'На данный момент в вашей телефонной книге есть следующие контакты:')
    for name, phone in address_book.items():
        print(f'Имя: \033[34m{name}\033[0m, телефон(ы): \033[34m{", ".join(list(value.phone for value in phone.phones))}\033[0m')



def upload_address_book():
    fake = Faker()
    fake.add_provider(phone_number)
    Faker.seed(1)

    for i in range(3):
        name = Name(fake.first_name())
        phone = Phone(fake.phone_number())
        record = Record(name, phone)
        address_book.add_record(record)


def main():
    working_bot= True
    upload_address_book()
    while working_bot:
        command = input('->')
        working_bot = reply(command)
        
if __name__ == '__main__':
    main()
