from interface import Interface
from classes import*


def print_initial_message():
    print('''
        Hello! I\'m your virtual assistant. Some words about how I can assist you:
        ''')

# @ParseError
# @KeyError


def main():
    interface = Interface()

    print_initial_message()

    while True:
        exit_point = '.'
        input_string = input(
            'Enter command to create, search, change, show or delete record. Print "." to break: ')

        if input_string == exit_point:
            print('Good bye!')
            break

        first_order_command = interface.parser.handle_first_order_commands(
            input_string)
        first_order_function = interface.first_order_commands_handler(
            first_order_command)

        if first_order_function() == exit_point:
            break


if __name__ == '__main__':
    main()


# 1) создаем интерфейс (в его конструкторе - адресная книга и парсер)
# 2) выводим приветственное сообщение
# 3) проверяем на введение точки (не нужно ли прерывать); если прерывание - сериализуем адресную книгу
# 4) вызываем парсер, в который передаем строку
# 5) парсер выявляет в строке и возвращает первую команду (кроме команды Hello!) с учетом некорректных резделителей;
#   вызывает ошибку, если команда не найдена
# 6) передаем команду в обработчик команд первого уровня
# 7) соответствующий метод просит либо ввести дополнительную команду и вызывает парсер, либо ввести аргументы,
#   создает объекты и передает в них аргументы.
