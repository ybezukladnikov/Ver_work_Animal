from model.ReadWriteBD import ReadWriteBD
from model.Check import Check
from view.ViewConsole import ViewConsole
import datetime
import random


class AnimalShelter:
    name = "Golden Tiger"
    list_animal = []
    list_of_command = []
    # list_toy_issued = []

    ReadWriteBD = ReadWriteBD()
    view = ViewConsole()

    def add_animal_inDB(self):
        new_animal = []
        name = Check().check_name_animal()
        birthday = Check().check_day_birth_animal()
        kind_animal = Check().check_kind_animal()
        for i in (name, birthday, kind_animal):
            new_animal.append(i)

        self.ReadWriteBD.read_write_bd(f"INSERT INTO `All_animal` (name_animal, Date_Birth, kind_animal) "
                                       f"VALUES ('{new_animal[0]}', '{new_animal[1]}', '{new_animal[2]}');", 'w')

        self.view.output_console("Animal added successfully.", True)

    def get_list_animal(self):
        self.list_animal = self.ReadWriteBD.read_write_bd("SELECT All_animal.id, name_animal, Date_Birth, "
                                                          "kind_animal.kind_animal, "
                                                          "All_animal.Date_Arrival, Date_Departure, Sign_Departure "
                                                          "FROM All_animal "
                                                          "INNER JOIN kind_animal "
                                                          "ON All_animal.kind_animal=kind_animal.id", 'r')


    def show_list_com_selected_animal(self):
        self.list_animal = self.ReadWriteBD.read_write_bd("SELECT All_animal.id, name_animal, Date_Birth, "
                                                          "kind_animal.kind_animal, "
                                                          "All_animal.Date_Arrival, Date_Departure, Sign_Departure "
                                                          "FROM All_animal "
                                                          "INNER JOIN kind_animal "
                                                          "ON All_animal.kind_animal=kind_animal.id", 'r')

        id_name_animal = Check().check_sel_id_animal(self.list_animal)
        self.list_of_command = self.ReadWriteBD.read_write_bd(f"SELECT Table_Command.name_command "
                                                             f"FROM Table_Command "
                                                             f"INNER JOIN Connect_Command_animal "
                                                             f"ON Table_Command.id=Connect_Command_animal.id_command "
                                                             f"WHERE id_animal = {id_name_animal[0]}", 'r')

        self.view.show_list_command(id_name_animal[1], self.list_of_command)


    # def give_toy(self):
    #     self.get_list_for_issue()
    #     if not len(self.list_for_issue) == 0:
    #         id_for_give = self.list_for_issue[0]['id']
    #         self.ReadWriteBD.read_write_bd(f"UPDATE `toys_for_delivery` "
    #                                        f"SET toy_issued = '1',"
    #                                        f"date_issue = '{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}'"
    #                                        f"WHERE id = '{id_for_give}';", 'w')
    #         self.view.output_console("Игрушка успешно выдана", True)
    #     else:
    #         self.view.output_console('Нет игрушек для выдачи', False)
    #
    # def play_toy(self):
    #     list_name_toy = []
    #     list_weights_toy = []
    #
    #     self.list_animal = self.ReadWriteBD.read_write_bd("SELECT * FROM `toys_in_shop` WHERE amount > 0 ", 'r')
    #     if len(self.list_animal) != 0:
    #         for row in self.list_animal:
    #             list_name_toy.append(row['title_toy'])
    #             list_weights_toy.append(row['frequency'])
    #
    #         name_won_toy = random.choices(list_name_toy, weights=list_weights_toy)[0]
    #         self.view.output_console(f"Поздравляем! Вы выиграли => {name_won_toy}", True)
    #
    #         for row in self.list_animal:
    #             if row['title_toy'] == name_won_toy:
    #                 new_amount = row['amount'] - 1
    #                 self.ReadWriteBD.read_write_bd(f"UPDATE `toys_in_shop` "
    #                                                f"SET amount = '{new_amount}'"
    #                                                f"WHERE title_toy = '{name_won_toy}';", 'w')
    #                 break
    #
    #         self.ReadWriteBD.read_write_bd(f"INSERT INTO `toys_for_delivery` (title_toy, date_of_winning) "
    #                                        f"VALUES ('{name_won_toy}', '{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}');",
    #                                        'w')
    #
    #
    #     else:
    #         self.view.output_console("В базе нет игрушек для розыгрыша", False)
    #
    # def get_list_toy_issued(self):
    #     self.list_toy_issued = self.ReadWriteBD.read_write_bd("SELECT *"
    #                                                           "FROM `toys_for_delivery`"
    #                                                           "WHERE toy_issued = 1", 'r')
    #
    # def change_frequency_toy(self):
    #     self.get_list_animal()
    #     self.view.show_animal_in_nursery(self.list_animal)
    #     number_toy = Check().check_number_toy(self.list_animal)
    #     new_frequency = Check().check_frequency_toy()
    #     self.ReadWriteBD.read_write_bd(f"UPDATE `toys_in_shop` "
    #                                    f"SET frequency = '{new_frequency}'"
    #                                    f"WHERE id = '{number_toy}';", 'w')
    #
    #
    #
    #
