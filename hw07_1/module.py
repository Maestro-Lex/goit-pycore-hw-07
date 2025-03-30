'''
Модуль, який містить всі наші методи для бота
'''
from colorama import Fore
from AddressBook import AddressBook
from classes import Record 


def parse_input(user_input: str) -> list:
    '''
    Парсер команд
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower() # Робимо введення команд нечутливим до регистру
    return cmd, *args

def help():
    '''
    Функція-помічник з інформацію про наявні команди
    '''
    return \
f"{Fore.LIGHTYELLOW_EX}    > {'help':15}{Fore.RESET}- show commands description\n\
{Fore.LIGHTYELLOW_EX}    > {'add':15}{Fore.RESET}- add contact (name, phone numbers)\n\
{Fore.LIGHTYELLOW_EX}    > {'change':15}{Fore.RESET}- change phone number of the contact (name, old phone number, new phone number)\n\
{Fore.LIGHTYELLOW_EX}    > {'phone':15}{Fore.RESET}- show the phone number of the contact (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'del':15}{Fore.RESET}- remove the contact (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'all':15}{Fore.RESET}- show the contact list\n\
{Fore.LIGHTYELLOW_EX}    > {'close':15}{Fore.RESET}- close the Bot\n\
{Fore.LIGHTYELLOW_EX}    > {'exit':15}{Fore.RESET}- close the Bot"

def input_error(func):
    '''
    Функція-декоратор для обробки помилок команд.
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)        
        except ValueError:
            return f"{Fore.LIGHTRED_EX}ERROR: Give me name and valid phone, please.{Fore.RESET}"            
        except KeyError:
            return f"{Fore.LIGHTRED_EX}ERROR: There is no such user!{Fore.RESET}"     
        except IndexError:
            return f"{Fore.LIGHTRED_EX}ERROR: Enter user name.{Fore.RESET}"
    return inner

@input_error
def add_contact(args: list, book: AddressBook):
    '''
    Команда додання імені та номерів до списку контактів 
    '''
    name, *phones = args
    # Приводимо введене ім'я до уніфікованого вигляду
    name = name.lower().capitalize().strip(",")
    # Не через book.find(name), бо за відсутності запису при його доданні 
    # ще повертає й повідомлення про його відсутність
    record = book.data.get(name)
    # Якщо запис відсутній, то створюємо його
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    # Якщо не введено жодного номеру, то викликаємо помилку
    if not phones:
        raise ValueError
    # Заносимо до запису всі введені телефони та формуємо повідомлення у разі повторення деяких з них
    for phone in phones:
        # Водночас викликаємо метод add_phone та передаємо те, що він повертає до змінної 
        # add_phone_message (або None або повідомлення)
        add_phone_message = record.add_phone(phone.strip(","))
        if add_phone_message:
            message += f"\n{add_phone_message}"
    return f"{Fore.LIGHTGREEN_EX}{message}{Fore.RESET}"

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    '''
    Команда зміни старого номеру телефону за ім'ям контакту на новий
    '''
    name, *phones = args
    # Приводимо введене ім'я до уніфікованого вигляду
    name = name.lower().capitalize().strip(",")
    # Робимо пошук запису у книзі та повертаємо його за наявності. Інакше викликаємо помилку
    record = book.find(name)
    if record is None:
        raise KeyError
    # Перевіряємо, що введено не менше двох валідних номерів телефону - старого та нового
    if len(phones) < 2:
        print(f"{Fore.LIGHTYELLOW_EX}INFO:{Fore.RESET} There are must be 2 phone numbers for change!")
        raise ValueError
    # Якщо старий номер телефону знайдено у записі контакту, 
    # то замінюємо його на новий. Інакше викликаємо помилку
    if record.find_phone(phones[0]):
        record.edit_phone(phones[0], phones[1])
        return f"{Fore.LIGHTGREEN_EX}Contact updated.{Fore.RESET}"
    else:
        raise ValueError

@input_error
def show_phone(args: list, book: AddressBook) -> str:
    '''
    Команда, що виводить номер телефону за ім'ям контакту, у разі його наявності
    '''
    # Приводимо введене ім'я до уніфікованого вигляду
    name = args[0].lower().capitalize().strip(",")
    # Повертаємо знайдені номери телефонів
    return '; '.join(p.value for p in book.find(name).phones)

@input_error
def remove_contact(args: list, book: AddressBook) -> str:
    '''
    Команда, що видаляє контакт за ім'ям користувача, у разі його наявності
    '''
    book.delete(args[0].lower().capitalize().strip(","))
    return f"{Fore.LIGHTGREEN_EX}Contact deleted.{Fore.RESET}"

def show_all(book: AddressBook) -> str:
    '''
    Команда виводу всього списку контактів із сортуванням за ім'ям користувача у вигляді таблиці
    '''
    contacts_list_str = f"|{'name':^15}|{'phone number':^17}|\n-----------------------------------\n"   
    for name, record in sorted(book.data.items()):
        phone_values_list = [p.value for p in record.phones]
        contacts_list_str += f"|{name:<15}|{'|\n|               |'.join(phone_values_list):<17}|\n"
    if not book:
        return f"{Fore.LIGHTRED_EX}Contact list is empty!{Fore.RESET}"
    return contacts_list_str