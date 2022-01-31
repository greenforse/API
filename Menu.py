from MenuItem import MenuItem
from SimpleMenu import SimpleMenuItem
import Command


class Menu(MenuItem):
    def __init__(self, title, number, is_submenu=False):
        super().__init__(number, title)
        # self.title=title
        # self.number=number
        self.startup_command = None
        self.before_select_command = None
        self.tear_down_command = None
        self.item = []
        self.run = True
        self.is_submenu = is_submenu

    def set_startup_command(self, command):
        self.startup_command = command

    def set_before_select_command(self, command):
        self.before_select_command = command

    def set_tear_down_command(self, command):
        self.tear_down_command = command

    def printMenu(self):
        for i in range(len(self.item)):
            print(f"{i + 1}. {self.item[i].get_title()}")
            print()
        if not self.is_submenu:
            print(f"{len(self.item) + 1}. Выход")
        else:
            print(f"{len(self.item) + 1}. Назад")

    def additem(self, number, title, command):
        item = SimpleMenuItem(number, title, command)
        self.item.append(item)
        # return item

    def addSubMenu(self, title, number):
        subMenu = Menu(title, number, True)
        self.item.append(subMenu)
        return subMenu

    def select(self):
        self.run = True
        n = int(input("Введите пункт меню: ")) - 1
        while n > len(self.item) or n < 0:
            n = int(input("Введите пункт меню: ")) - 1
        if n == (len(self.item)):
            # if self.is_submenu== False:
            self.run = False
        else:
            self.item[n].execute()
        return n

    def execute(self):
        if self.startup_command is not None:
            self.startup_command()
        self.run = True
        while self.run:
            if self.before_select_command is not None:
                self.before_select_command()
            self.printMenu()
            self.select()
        if self.tear_down_command is not None:
            self.tear_down_command()
    # def get_title(self):
    #    return self.title
    # def test():
    #    print("ТЕСТ")
