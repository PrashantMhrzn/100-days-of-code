import db

CHOICES = '''1.Add contact
2.delete contact
3.view a contact
4.view all contacts
5.exit
'''


def main():
    print('****Welcome to contact management system****')
    try:
        usr_inp = int(input(CHOICES))
    except ValueError as err:
        print(err)

    try:
        while usr_inp != 5:
            if usr_inp == 1:
                first = input('Enter first name: ')
                last = input('Enter last name: ')
                number = input('Enter number: ')
                db.add_contact(first, last, number)
            elif usr_inp == 2:
                first = input('Enter first name: ')
                last = input('Enter last name: ')
                db.delete_contact(first, last)
            elif usr_inp == 3:
                first = input('Enter first name: ')
                db.view_contact(first)
            elif usr_inp == 4:
                db.view_all()
            else:
                print('Enter between 1-5 only!')
            try:
                usr_inp = int(input(CHOICES))
            except ValueError as err:
                usr_inp = 5
                print(err)
    except UnboundLocalError:
        pass


if __name__ == '__main__':
    main()
