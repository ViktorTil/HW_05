from classes import AddressBook, Name, Phone, Record


commands = ["hello", ["good bye", "close", "exit", "bye", "esc", "q"], "add", "change", "phone", "show all"]
# phone_book = {"Vasya": "0505436565", "Lesya" : "0674231111"}
phone_book = AddressBook()


def error_with_func(arg):
    def input_error(func):
        def proc_error(*args):
            try:
               return func(*args)
            except IndexError:
                print(f'Добавьте все данные в команду {arg}')
            except ValueError:
                pass
        return proc_error
    return input_error


@error_with_func('add')  
def add_phone(cont):
    contact = cont.split(' ')        
    # for phone in phone_book:
            
    #     if phone.lower() == contact[1].lower():
    #         print(f'Контакт {contact[1]} уже есть в книге с номером {phone_book.get(phone)}')
    #         return True
                
    # phone_book[contact[1]] = contact[2]   
    # number_add = f'ok'
    name = Name(contact[1])
    phone = Phone(contact[2])
    rec = Record(name, phone)
    return phone_book.add_record(rec)
        
    # print(number_add)

        
@error_with_func('change')
def change(contact):
    chng_cont = contact.split(' ')
    number_chng = f'Нет контакта {chng_cont[1]} в Вашем списке'
    
    for phone in phone_book:
        
        if phone.lower() != chng_cont[1].lower():
            continue
        else:
            phone_book[phone] = chng_cont[2]
            number_chng = f'Контакт {chng_cont[1]} изменен'
    print(number_chng)


@error_with_func('phone')
def phone(contact):
    c_number=contact.split(" ")
    number = f'В ваших контактах отсутствует {c_number[1]}'
    for phone in phone_book:
        if c_number[1].lower() == phone.lower():
            number = f'{phone_book.get(phone)}'
    print(number)
    
    
def reply(command):
    bot=True
    operator=command.lower().split(" ")
    if command.lower() in commands[1]:
        print(answers[1])
        bot = False
    elif operator[0] in commands or command.lower() in commands:
        try:
            index_comm = commands.index(command.lower())
        except ValueError:
            index_comm = commands.index(operator[0])

        try:
            print(answers[index_comm](command))
        except:
            print(answers[index_comm])
    else:
        print(f'Введите правильную команду :{commands[0],commands[2:]} или {commands[1]} для выхода')
    return bot


def show_all(x):
    result = []
    for rec in phone_book.values():
        result.append(f'Name: {rec.name.value}, phone number {", ".join([p.value for p in rec.phones])}')
    return "\n".join(result)

answers = ["How can I help you?", "Good bye!",add_phone, change, phone, show_all]


def main():
    working_bot= True
    while working_bot:
        # print('->')
        command = input("->")
        working_bot = reply(command)
        
        
if __name__ == '__main__':
    main()
