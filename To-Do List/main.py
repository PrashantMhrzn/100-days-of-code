import db


CHOICES = '''1.Add a task
2.Delete a task
3.View all tasks
4.Exit
'''

def main():
    id = 0
    try:
        usr_inp = int(input(CHOICES))
    except ValueError as err:
        print(err)
    try:
        while usr_inp != 4:
            if usr_inp == 1:
                id += 1
                task = input('Enter a task on the to-do list: ')
                db.add_task(id, task)
            elif usr_inp == 2:
                usr_sel_id = int(input('Enter task id to be deleted: '))
                db.delete_task(usr_sel_id)
            elif usr_inp == 3:
                db.show_all()
            else:
                print('Enter choices between 1-4')
            try:
                usr_inp = int(input(CHOICES))
            except ValueError as err:
                print(err)
    except UnboundLocalError:
        pass

if __name__ == '__main__':
    main()