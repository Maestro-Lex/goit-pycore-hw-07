'''
Модуль з описом команд бота
'''
from colorama import Fore


def help():
    '''
    Функція-помічник з інформацію про наявні команди
    '''
    return \
f"{Fore.LIGHTYELLOW_EX}    > {'help':15}{Fore.RESET}- show commands description\n\
{Fore.LIGHTYELLOW_EX}    > {'add':15}{Fore.RESET}- add contact (name, phone numbers)\n\
{Fore.LIGHTYELLOW_EX}    > {'change':15}{Fore.RESET}- change phone number of the contact (name, old phone number, new phone number)\n\
{Fore.LIGHTYELLOW_EX}    > {'phone':15}{Fore.RESET}- show the phone number of the contact (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'add-birthday':15}{Fore.RESET}- add the contact's birthday (date 'DD.MM.YYYY')\n\
{Fore.LIGHTYELLOW_EX}    > {'show-birthday':15}{Fore.RESET}- show the contact's birthday (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'birthdays':15}{Fore.RESET}- show the nearest 7-days birthdays list\n\
{Fore.LIGHTYELLOW_EX}    > {'del':15}{Fore.RESET}- remove the contact (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'all':15}{Fore.RESET}- show the contact list\n\
{Fore.LIGHTYELLOW_EX}    > {'load':15}{Fore.RESET}- load the contact list from a file (file-name)\n\
{Fore.LIGHTYELLOW_EX}    > {'save':15}{Fore.RESET}- save the contact list to a file (file-name)\n\
{Fore.LIGHTYELLOW_EX}    > {'close':15}{Fore.RESET}- close the Bot\n\
{Fore.LIGHTYELLOW_EX}    > {'exit':15}{Fore.RESET}- close the Bot"