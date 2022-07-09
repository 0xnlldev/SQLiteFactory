import SQLiteFactory
import random

DB = SQLiteFactory.Factory() # SQLiteFactory good import

def test():
    print('| Table Create and add values \ ')

    data = []                       # Data List Create
    id = random.randint(1000,9999)  # random id
    data.append(id)
    name    = input('Name    : ')
    data.append(name)               # Append 'name'
    surname = input('Surname : ')
    data.append(surname)            # Append 'surname'
    mail    = input('Mail    : ')
    data.append(mail)               # Append 'mail'

    DB.connect('test.db') # Import .db path and connect (e.g: Database/Users/users.db)
    DB.tableCreate(table_name='users', tableContents=['id INT','name TEXT','surname TEXT','mail TEXT']) # table_name = String | tableContents = List
    DB.addValues(table_name='users', values=data) #Add values type List

    print('\nAll Users;')
    table = DB.getTable(table_name='users') #table get all content
    for data in table:
        print(f'Id: {data[0]}\nName: {data[1]}\nSurname: {data[2]}\nMail: {data[3]}')

    print('\n\n| Delete User \ ')
    selectid = input('The user id you want to delete: ')
    DB.deleteData(table_name='users',where=f'id = {selectid}')
    print(f'ID: {selectid} delete!')

    print('\n\nAll Users;')
    table = DB.getTable(table_name='users')  # table get all content
    for data in table:
        print(f'Id: {data[0]}\nName: {data[1]}\nSurname: {data[2]}\nMail: {data[3]}')


    #users_table = DB.cur.execute('SELECT * FROM users').fetchall()

    DB.close() #close the DB

if __name__ == '__main__':
    test()
