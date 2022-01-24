
import psycopg2

from Edit_context import Edit_context
from Menu import Menu


def listUsers():
    cur.execute("SELECT* FROM users")
    data = cur.fetchall()
    print("id Login admin")
    for user in data:
        print(user[0], user[1], user[3])


def deleteUser():
    listUsers()
    id=int(input("Введите ид пользователя для удаления: "))
    cur.execute(f"DELETE FROM Users WHERE id = {id}")

def editLogin():
    newLogin= input("Введите новый логин")
    id = Edit_context().student[0][0]
    cur.execute(f"UPDATE Users SET login = {newLogin} WHERE id={id};")
    conn.commit()

def SelectStudentCommand():
    listUsers()
    select = False
    while select == False :
        selectNumber = int(input("Введите номер пользователя"))
        try:
            cur.execute(f"Select* FROM Users WHERE id = {selectNumber} ;")
            data = cur.fetchall()
            Edit_context().student = data
            select = True
        except : print("Такого пользователя нет")

def ShowSelectCommand():
  print (Edit_context().student)

def DeselectStudentCommand():
  Edit_context().student=None

def editPassword():
    newPasword= input("Введите новый пароль")
    id = Edit_context().student[0][0]
    cur.execute(f"UPDATE Users SET password = {newPasword} WHERE id={id};")
    conn.commit()


def addUser():
    id = int(input("id: "))
    login = str(input("Введите login: "))
    password = input("Введите password: ")
    admin = input("Администратор? 1-да 2 - нет ")
    if admin == 1:
        isAdmin = True
    else:
        isAdmin = False
    cur.execute(f"INSERT INTO Users (id,login, password, is_admin) VALUES ({id},{login}, {password}, {isAdmin});")
    conn.commit()


def ShowSelectCommand():
    print(Edit_context().student)

with psycopg2.connect(
        host="192.168.56.101",
        port=5432,
        database="Playground",
        user='playground',
        password='playground') as conn:
    cur = conn.cursor()
    login = input("Введите логин")
    password = input("Введите пароль")
    sql = "SELECT* FROM users WHERE login=%s AND password = %s"
    cur.execute(sql, [login, password])
    data = cur.fetchall()
    if len(data) == 1:
        print("Вы авторизовались")
        print(data)
        if data[0][3]:
            print("Вы админ")
            glavnoeMenu = Menu("Главное меню", 0)
            glavnoeMenu.additem(1, "Список пользователя", listUsers)
            AddStud = glavnoeMenu.additem(2, "Добавить пользователя", addUser)
            glavnoeMenu.additem(3, "Удалить пользователя", deleteUser)
            ###
            editStudents = glavnoeMenu.addSubMenu("Редактировать студента", 4)
            editStudents.set_startup_command(SelectStudentCommand)
            editStudents.set_before_select_command(ShowSelectCommand)
            editStudents.set_tear_down_command(DeselectStudentCommand)
            editStudents.additem(1, "Изменить логин", editLogin)
            editStudents.additem(2, "Изменить пароль", editPassword)
            glavnoeMenu.execute()
    else:
        print("Неправильный логин или пароль")
