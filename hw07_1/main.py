from colorama import Fore, init
from classes import Record 
from AddressBook import AddressBook
import module as methods


def main():
    book = AddressBook()
    init() # Викликаємо метод init() бібліотеки colorama для коректної роботи
    print("\nWelcome to the assistant bot! Say 'hello' for greetings!")
    while True:
        user_input = input("Enter a command: ")
        # Перевіряємо наявність вводу і, якщо нічого не введено, повторюємо запит
        try:
            command, *args = methods.parse_input(user_input)
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Please, enter any command!{Fore.RESET}")
            continue
        # Обробка введеного запиту
        if command in ["close", "exit"]:
            print("Good bye!\n")
            break
        elif command == "hello":
            print("How can I help you? (Enter 'help' to see commands description)")
        elif command == "help":
            print(methods.help())
        elif command == "add":
            print(methods.add_contact(args, book))
        elif command == "change":
            print(methods.change_contact(args, book))
        elif command == "phone":
            print(f"{Fore.LIGHTBLUE_EX}{methods.show_phone(args, book)}{Fore.RESET}")
        elif command == "del":
            print(f"{Fore.LIGHTBLUE_EX}{methods.remove_contact(args, book)}{Fore.RESET}")    
        elif command == "all":
            print(f"{Fore.LIGHTBLUE_EX}{methods.show_all(book)}{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid command.{Fore.RESET}")


if __name__ == "__main__":
    main()