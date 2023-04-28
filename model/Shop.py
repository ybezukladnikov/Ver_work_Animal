from model.ReadWriteBD import ReadWriteBD
from model.Check import Check
from view.ViewConsole import ViewConsole
import datetime
import random


class Shop:
    name = "Детский мир"
    list_toy = []
    list_for_issue = []
    list_toy_issued = []

    ReadWriteBD = ReadWriteBD()
    view = ViewConsole()

    def add_toy_inDB(self):
        new_toy = []
        name = Check().check_name_toy()
        amount_toy = Check().check_amount_toy()
        frequency = Check().check_frequency_toy()
        for i in (name, amount_toy, frequency):
            new_toy.append(i)

        self.ReadWriteBD.read_write_bd(f"INSERT INTO `toys_in_shop` (title_toy, amount, frequency) "
                                       f"VALUES ('{new_toy[0]}', '{new_toy[1]}', '{new_toy[2]}');", 'w')

        self.view.output_console("Игрушка успешно добавлена в базу", True)

    def get_list_toy(self):
        self.list_toy = self.ReadWriteBD.read_write_bd("SELECT * FROM `toys_in_shop`", 'r')

    def get_list_for_issue(self):
        self.list_for_issue = self.ReadWriteBD.read_write_bd("SELECT id, title_toy, date_of_winning "
                                                             "FROM `toys_for_delivery`"
                                                             "WHERE toy_issued = 0", 'r')

    def give_toy(self):
        self.get_list_for_issue()
        if not len(self.list_for_issue) == 0:
            id_for_give = self.list_for_issue[0]['id']
            self.ReadWriteBD.read_write_bd(f"UPDATE `toys_for_delivery` "
                                           f"SET toy_issued = '1',"
                                           f"date_issue = '{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}'"
                                           f"WHERE id = '{id_for_give}';", 'w')
            self.view.output_console("Игрушка успешно выдана", True)
        else:
            self.view.output_console('Нет игрушек для выдачи', False)

    def play_toy(self):
        list_name_toy = []
        list_weights_toy = []

        self.list_toy = self.ReadWriteBD.read_write_bd("SELECT * FROM `toys_in_shop` WHERE amount > 0 ", 'r')
        if len(self.list_toy) != 0:
            for row in self.list_toy:
                list_name_toy.append(row['title_toy'])
                list_weights_toy.append(row['frequency'])

            name_won_toy = random.choices(list_name_toy, weights=list_weights_toy)[0]
            self.view.output_console(f"Поздравляем! Вы выиграли => {name_won_toy}", True)

            for row in self.list_toy:
                if row['title_toy'] == name_won_toy:
                    new_amount = row['amount'] - 1
                    self.ReadWriteBD.read_write_bd(f"UPDATE `toys_in_shop` "
                                                   f"SET amount = '{new_amount}'"
                                                   f"WHERE title_toy = '{name_won_toy}';", 'w')
                    break

            self.ReadWriteBD.read_write_bd(f"INSERT INTO `toys_for_delivery` (title_toy, date_of_winning) "
                                           f"VALUES ('{name_won_toy}', '{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}');",
                                           'w')


        else:
            self.view.output_console("В базе нет игрушек для розыгрыша", False)

    def get_list_toy_issued(self):
        self.list_toy_issued = self.ReadWriteBD.read_write_bd("SELECT *"
                                                              "FROM `toys_for_delivery`"
                                                              "WHERE toy_issued = 1", 'r')

    def change_frequency_toy(self):
        self.get_list_toy()
        self.view.show_toys_in_shop(self.list_toy)
        number_toy = Check().check_number_toy(self.list_toy)
        new_frequency = Check().check_frequency_toy()
        self.ReadWriteBD.read_write_bd(f"UPDATE `toys_in_shop` "
                                       f"SET frequency = '{new_frequency}'"
                                       f"WHERE id = '{number_toy}';", 'w')




