from model.Menu import Menu
from prettytable import PrettyTable
from colorama import init, Fore, Back


init(autoreset=True)

class ViewConsole:

    def show_animal_in_nursery(self, data):
        mytable = PrettyTable()
        mytable.field_names = ["ID", "Name of animal", "Date of Birth", "Kind of animal",
                               "Date of Arrival", "Date of Departure", "Sign Departure"]
        if len(data) == 0:
            self.output_console("There are no animal in AnimalShelter", False)
        else:
            for row in data:
                mytable.add_row([row['id'],
                                 row['name_animal'],
                                 row['Date_Birth'],
                                 row['kind_animal'],
                                 row['Date_Arrival'],
                                 row['Date_Departure'],
                                 # row['Sign_Departure']])
                                 'Out' if row['Sign_Departure'] == b'\x01' else 'In'])
            self.output_console("Animal in AnimalShelter:", True)
            print(mytable)

    def show_list_command(self, name, list_com):
        if len(list_com) == 0:
            self.output_console(f"An animal named \"{name}\" still can't do anything", False)
            print()
        else:
            self.output_console(f"An animal named \"{name}\" can do:", True)
            print()
            for enum, row in enumerate(list_com):
                print(enum + 1, row['name_command'])
            print()

    def show_available_command(self, data):
        mytable = PrettyTable()
        mytable.field_names = ["ID", "Name of command"]
        if len(data) == 0:
            self.output_console("There are no command", False)
        else:
            for row in data:
                mytable.add_row([row['id'], row['name_command']])

            self.output_console("List available command.:", True)
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

