class Contact:
     def __init__(self, name, surname, lastname, number):
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.number = number

     def get_name(sels):
          return self.name

     def get_surname(sels):
          return self.surname

     def get_lastname(sels):
          return self.lastname

     def get_number(sels):
          return self.number

class Phone_book:
     def __init__(self, book):
          self.book = book

     def add_contact(self, contact):
          new_contact = [contact.name, contact.surname, contact.lastname]
          self.book[contact.number] = new_contact

     def find_contacts_by_name(self, name):
          res_values = list(filter(lambda x: name in x, self.book.values()))
          res = {i: self.book[i] for i in self.book.keys() if self.book[i] in res_values}
          return res

     def find_contacts_by_sername(self, sername):
          res_values = list(filter(lambda x: sername in x, self.book.values()))
          res = {i: self.book[i] for i in self.book.keys() if self.book[i] in res_values}
          return res

     def find_contacts_by_lastname(self, lastname):
          res_values = list(filter(lambda x: lastname in x, self.book.values()))
          res = {i: self.book[i] for i in self.book.keys() if self.book[i] in res_values}
          return res
     def change_name(self, number):
          self.book[number][0] = input('Введите новое имя: ')

     def change_sername(self, number):
          self.book[number][1] = input('Введите новую фамилию: ')

     def change_lastname(self, number):
          self.book[number][2] =input('Введите новое отчество: ')

def write_again():
    book_file = open(r'book.txt', 'w')
    for i in phone_book.book:
        book_file.write(f'{i}: {phone_book.book[i]}\n')
    book_file.close()

menu = ['1: Добавить контакт', '2: Удалить контакт', '3: Найти контакт по имени',
        '4: Найти контакт по фамилии', '5: Найти контакт по отчеству', '6: Вывести данные о контакте по номеру',
        '7: Вывести все контакты', '8: Обновить книгу', '9: Изменить контакт', '10: завершить работу']

phone_book = Phone_book({'56789': ['n', 's', 'ln'], '456': ['fdg', 'dfsg', 'gh']})
id_comand = 1
while True:
    print('Возможные команды: ')
    print('\n'.join(menu))
    k = int(input('Введите номер команды: '))
    if id_comand == 1:
        write_again()
    if k == 1:
        p, n, s, ln = input('введите номер: '), input('введите имя: '), input('введите фамилию: '), input('введите отчество: ')
        con = Contact(n, s, ln, p)
        phone_book.add_contact(con)
        book_file = open(r'book.txt', 'a')
        book_file.write(f'{p}: {phone_book.book[p]}\n')
        book_file.close()
    elif k == 2:
        p = input('введите номер: ')
        if p in phone_book.book:
            del phone_book.book[p]
        else:
            print('Контакт отсутствует')
        write_again()
        id_comand += 1
    elif k == 3:
        print(phone_book.find_contacts_by_name(input('Введите имя: ')))
        id_comand += 1
    elif k == 4:
        print(phone_book.find_contacts_by_sername(input('Введите фамилию: ')))
        id_comand += 1
    elif k == 5:
        print(phone_book.find_contacts_by_lastname(input('Введите отчество: ')))
        id_comand += 1
    elif k == 6:
        number = input('Введите номер телефона: ')
        print('\nКонтакт:')
        if number not in phone_book.book:
            print('Отсутствует')
        else:
            print(f'Номер телефона: {number}')
            print(f'Фамилия: {phone_book.book[number][1]}')
            print(f'Имя: {phone_book.book[number][0]}')
            print(f'Отчество: {phone_book.book[number][2]}')
        id_comand += 1
    elif k == 7:
        for i in phone_book.book.keys():
            print(f'\n*****\nКонтакт: {i}\nФамилия: {phone_book.book[i][1]}\nИмя: {phone_book.book[i][0]}\n'
                  f'Отчество: {phone_book.book[i][2]}\n*****')
        id_comand += 1
    elif k == 8:
        write_again()
        id_comand += 1
    elif k == 9:
        print('Что вы хотите изменить? (введите номер команды):')
        k = int(input('1: имя\n2:фамилия\n3:отчество\n'))
        if k == 1:
            phone_book.change_name(input('Введите номер телефона:\n'))
        elif k == 2:
            phone_book.change_sername(input('Введите номер телефона:\n'))
        elif k == 3:
            phone_book.change_lastname(input('Введите номер телефона:\n'))
        else:
            print('Команда отсутствует. Повторите попытку.')
        write_again()
        id_comand += 1
    elif k == 10:
        print('__Завершение работы__')
        id_comand = 1
        break
    else:
        print('Команда отсутствует. Повторите попытку.')
    print()
