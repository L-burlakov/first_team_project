from classes import*
from parser import Parser
from decorators import errors_handler
from importlib.resources import path


class Interface:

    # automatically creates the AdressBook object by initialization of Interface object;
    # either create a new object or, if object was already created, restore it from the file
    def __init__(self):
        self.parser = Parser()
        with path('first_team_project', 'objects_copy.bin') as filepath:
            try:
                self.book = AddressBook().restore_from_file(filepath)
            except EOFError:
                self.book = AddressBook()

    # commands, that handle exit or continuing of bot-session

    def handle_hello(self):
        print('How can I help you?')

    def handle_exit(self):
        print('Good by!')
        return '.'

    @errors_handler
    def create_address(self):
        city = input('Please, give me city of a contact (optional): ')
        street = input('Please, give me street of a contact (optional): ')
        house_number = input(
            'Please, give me house_number of a contact (optional): ')
        flat_number = input(
            'Please, give me flat_number of a contact (optional): ')
        postal_code = input(
            'Please, give me postal_code of a contact (optional): ')
        address = Address(self.parcer.handle_addresses(f'''C:{city}, S:{street}, H:{house_number}, A:{flat_number}, 
                                                           PC:{postal_code}, End'''))
        return address

    # part of methods to handle records (second_order_methods)

    @errors_handler
    def add_phone_number(self, name: Name):
        phone = self.parser.handle_phone_numbers(
            input('Please, enter phone_number: '))
        self.book.data[name.value].add_phone(Phone(phone))
        print('New phone number was added!')

    @errors_handler
    def add_email(self, name: Name):
        email = self.parser.handle_emails(input('Please, enter email: '))
        self.book.data[name.value].add_email(Email(email))
        print('New email was added!')

    @errors_handler
    def change_phone_number(self, name: Name):
        old_phone = self.parser.handle_phone_numbers(
            input('Please, enter phone_number you want to change: '))
        new_phone = self.parser.handle_phone_numbers(
            input('Please, enter new phone_number: '))
        self.book.data[name.value].change_phone(
            Phone(old_phone), Phone(new_phone))
        print(f'Phone {old_phone} was removed with {new_phone}!')

    @errors_handler
    def change_email(self, name: Name):
        old_email = self.parser.handle_emails(
            input('Please, enter email you want to change: '))
        new_email = self.parser.handle_emails(
            input('Please, enter new email: '))
        self.book.data[name.value].change_email(
            Email(old_email), Email(new_email))
        print(f'Email {old_email} was removed with {new_email}!')

    @errors_handler
    def change_address(self, name: Name):
        address = self.create_address()
        self.book.data[name.value].change_address(address)
        print('Address was changed!')

    @errors_handler
    def change_birthday(self, name: Name):
        date = self.parser.handle_dates(input('Please, enter birthday date: '))
        self.book.data[name.value].change_birthday(Birthday(date))
        print('Birthday date was changed!')

    @errors_handler
    def delete_phone(self, name: Name):
        phone = self.parser.handle_phone_numbers(
            input('Please, enter phone_number: '))
        self.book.data[name.value].delete_phone(Phone(phone))
        print(f'Phone number {phone} was deleted!')

    @errors_handler
    def delete_email(self, name: Name):
        email = self.parser.handle_emails(input('Please, enter email: '))
        self.book.data[name.value].delete_email(Email(email))
        print(f'Email {email} was deleted!')

    @errors_handler
    def delete_birthday(self, name: Name):
        self.book.data[name.value].change_birthday(None)
        print('Birthday date was removed!')

    @errors_handler
    def delete_address(self, name: Name):
        self.book.data[name.value].change_address(None)
        print('Address was removed!')

    SECOND_ORDER_COMMANDS = {
        # common_commands
        'hello': handle_hello,
        'good_bye': handle_exit,
        'close': handle_exit,
        'exit': handle_exit,

        # commands to handle with Records
        'add_phone_number': add_phone_number,
        'add_email': add_email,
        'add_address': change_address,
        'add_birthday': change_birthday,
        'change_phone_number': change_phone_number,
        'change_email': change_email,
        'change_address': change_address,
        'change_birthday': change_birthday,
        'delete_phone': delete_phone,
        'delete_email': delete_email,
        'delete_birthday': delete_birthday,
        'delete_address': change_address
    }

    @errors_handler
    def second_order_commands_handler(self, command):
        return self.SECOND_ORDER_COMMANDS[command]

    # part of methods to handle address_book (first_order_methods)

    @errors_handler
    def add_record(self):
        name = Name(input('Please, give me name of new contact (necessary): '))
        birthday_date = Birthday(self.parser.handle_dates(
            input('Please, give me birthday date of new contact (optional): ')))
        address = self.create_address()
        record = Record(name, birthday_date, address)
        self.book.add_record(record)
        print('New record was created and added to the address book!')

    @errors_handler
    def get_record(self):
        name = Name(input('Please, enter name of contact: '))
        print(self.book.get_record(name))

    def search_record(self):
        string = input(
            'Please, enter the string, you want the records fields to match: ')
        print(self.book.search_records(string))

    @errors_handler
    def change_record(self):
        name = Name(input('Please, enter name of contact: '))
        string = input('''Enter command to change or delete record attributes (phone number, email, birthday date or address).
                          Or enter one of exit commands to break: ''')
        second_order_command = self.parser.handle_second_order_commands(string)
        second_order_function = self.second_order_commands_handler(
            second_order_command)
        if second_order_function(name) == '.':
            return '.'

    def show_records(self):
        n_records = input(
            'Please, specify, how many records are to be shown at once: ')
        n_pages = input(
            'Please, specify, how many pages of records are to be shown: ')
        for _ in range(n_pages):
            print(self.book.iterator(n_records))

    def records_with_birthday_soon(self):
        n_days = int(
            input('Please, specify the number of days till birthday: '))
        contacts = list(
            filter(lambda x: x.birthday and x.days_to_birthday() <= n_days, self.book.data))
        print(contacts)

    @errors_handler
    def delete_record(self):
        name = Name(input('Please, enter name of contact: '))
        self.book.delete_record(name)
        print(f'Contact with name {name} was deleted!')

    FIRST_ORDER_COMMANDS = {
        # common_commands
        'hello': handle_hello,
        'good_bye': handle_exit,
        'close': handle_exit,
        'exit': handle_exit,

        # commands to handle with AdressBook
        'add_record': add_record,
        'get_record': get_record,
        'search_records': search_record,
        'change_record': change_record,
        'show_records': show_records,
        'records_with_birthday_soon': records_with_birthday_soon,
        'delete_record': delete_record
    }

    @errors_handler
    def first_order_commands_handler(self, command):
        return self.FIRST_ORDER_COMMANDS[command]
