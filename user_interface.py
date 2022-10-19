import export as cr



print('\nВас приветствует телефонная книга')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Найти номер по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись.')
        print('6. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            print(cr.retrive())

        elif n == 2:
            search = input('Введите фамилию: ')
            print(cr.retrive(surname=search))

        elif n == 3:
            search = input('Введите имя: ')
            print(cr.retrive(name=search))

        elif n == 4:
            search = input('Введите номер  телефона: ')
            print(cr.retrive(number=search))

        elif n == 5:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            email = input('Введите электронную почту: ')
            cr.create(name, surname, number, email)

        elif n == 6:
            print('Спасибо за работу!')
            break

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)