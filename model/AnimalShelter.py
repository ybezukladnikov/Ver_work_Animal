from model.ReadWriteBD import ReadWriteBD
from model.Check import Check
from view.ViewConsole import ViewConsole



class AnimalShelter:
    name = "Golden Tiger"
    list_animal = []
    list_of_command = []

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

    def teach_animal(self):
        self.list_animal = self.ReadWriteBD.read_write_bd("SELECT All_animal.id, name_animal, Date_Birth, "
                                                          "kind_animal.kind_animal, "
                                                          "All_animal.Date_Arrival, Date_Departure, Sign_Departure "
                                                          "FROM All_animal "
                                                          "INNER JOIN kind_animal "
                                                          "ON All_animal.kind_animal=kind_animal.id "
                                                          "WHERE All_animal.Sign_Departure = 0", 'r')
        self.view.output_console("Which animal do you want to teach?", True)
        print()
        id_name_animal = Check().check_sel_id_animal(self.list_animal)
        id_command = Check().check_id_command()
        self.ReadWriteBD.read_write_bd(f"INSERT INTO `Connect_Command_animal` (id_animal, id_command) "
                                       f"VALUES ('{id_name_animal[0]}', '{id_command[0]}');", 'w')
        self.view.output_console(f"Great. Now \"{id_name_animal[1]}\" can \"{id_command[1]}\"", True)
        print()



