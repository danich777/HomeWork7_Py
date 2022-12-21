phone_book = []

def get_phone_book():
    global phone_book
    return phone_book


def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
        global phone_book
        phone_book.append(contact)

def contacts_edit(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите редактировать контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        new_name = input(f'Введите новое имя контакта {name}: ')
        if new_name:
            phone_book[id - 1][0] = new_name
        new_phone = input('Введите новый телефон контакта: ')
        if new_phone:
            phone_book[id - 1][1] = new_phone
        new_comment = input('Введите новый комментарий к контакту: ')
        if new_comment:
            phone_book[id - 1][2] = new_comment
    return False


def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False


def contacts_search(search_str):
    global phone_book
    for contact in phone_book:
        for word in contact:
            if search_str in word:
                print(*contact)
