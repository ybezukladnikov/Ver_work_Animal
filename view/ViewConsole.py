from model.Menu import Menu
from prettytable import PrettyTable
from colorama import init, Fore, Back


init(autoreset=True)

class ViewConsole:

    def show_toys_in_shop(self, data):
        mytable = PrettyTable()
        mytable.field_names = ["ID", "Название игрушки", "Количество", "Частота выпадения"]
        if len(data) == 0:
            self.output_console("В базе нет игрушек", False)
        else:
            for row in data:
                mytable.add_row([row['id'], row['title_toy'], row['amount'], row['frequency']])
            self.output_console("В базе есть следующие игрушки:", True)
            print(mytable)


    def show_list_for_issue(self, data):
        mytable = PrettyTable()
        mytable.field_names = ["ID", "Название игрушки", "Дата выигрыша"]
        if len(data) == 0:
            self.output_console("Список выдачи пуст", False)
        else:
            for num, row in enumerate(data):
                mytable.add_row([num+1, row['title_toy'], row['date_of_winning']])
            self.output_console("Игрушки к выдаче:", True)
            print(mytable)

    def show_list_toy_issued(self, data):
        mytable = PrettyTable()
        mytable.field_names = ["ID", "Название игрушки", "Дата выигрыша", "Дата выдачи"]
        if len(data) == 0:
            self.output_console("Все игрушки выданы", False)
        else:
            for num, row in enumerate(data):
                mytable.add_row([num+1, row['title_toy'], row['date_of_winning'], row['date_issue']])
            self.output_console("Список выданных игрушек:", True)
            print(mytable)



    def show_main_menu(self):

        for operNum, operDesc in Menu().MENU_ITEMS.items():
            print(f"{operNum}. {operDesc}")


    def input_console(self,text):
        input_text = input(Fore.CYAN + text)
        return input_text

    def output_console(self, text, flag):
        if flag:
            print(Back.GREEN + Fore.BLACK + text)
        else:
            print(Back.RED + Fore.BLACK + text)







