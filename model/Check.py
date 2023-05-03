import time

from model.ReadWriteBD import ReadWriteBD
from view.ViewConsole import ViewConsole


class Check:
    my_view = ViewConsole()

    def check_main_menu(self):
        while True:
            try:
                num = int(self.my_view.input_console('Input number item, which want to exicute: '))
                if 0 <= num <= 3:
                    break
                else:
                    self.my_view.output_console('There is no item menu! Try again.', False)
                    continue
            except ValueError:
                self.my_view.output_console('You input no correct item menu! Try again.', False)

        return num

    def check_name_animal(self):
        while True:
            name = self.my_view.input_console('Input name of animal (Max length 15 symbol): ')

            if len(name) > 15 or len(name) == 0:
                self.my_view.output_console('length is not correct', False)
                continue
            # flag = False
            # for row in ReadWriteBD().read_write_bd("SELECT * FROM `toys_in_shop`", 'r'):
            #     if name == row['title_toy']:
            #         flag = True
            # if flag:
            #     self.my_view.output_console('Такое имя уже есть в базе', False)
            #     continue

            break
        return name

    #

    def check_day_birth_animal(self):
        while True:
            date = self.my_view.input_console('Input the animal s birthday (Format yyyy-mm-dd): ')
            try:
                valid_date = time.strptime(date, '%Y-%m-%d')
                break

            except ValueError:
                self.my_view.output_console('You input not correct date. Try again.', False)

        return date


    def check_sel_id_animal(self, list_animal):
        id_name = []
        while True:
            self.my_view.show_animal_in_nursery(list_animal)
            num = self.my_view.input_console('Input ID animal(only number): ')
            try:
                num_correct = int(num)
                flag = True
                for row in list_animal:
                    if num_correct == row['id']:
                        id_name.append(num_correct)
                        id_name.append(row['name_animal'])
                        flag = False
                if flag:
                    self.my_view.output_console('There is no such ID in the database', False)
                    continue
                else:
                    break

            except ValueError:
                self.my_view.output_console('You input no correct number! Try again.', False)

        return id_name


    # def check_amount_toy(self):
    #     while True:
    #         try:
    #             num = int(self.my_view.input_console('Введите количество игрушек: '))
    #             if num >= 0:
    #                 break
    #             else:
    #                 self.my_view.output_console('Число не может быть отрицательным', False)
    #                 continue
    #         except ValueError:
    #             self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)
    #
    #     return num
    #
    def check_kind_animal(self):
        dict_kind_animal = ReadWriteBD().read_write_bd("SELECT * FROM `kind_animal`", 'r')
        length = len(dict_kind_animal)
        while True:
            self.my_view.output_console('List available kind of animal.', True)
            for enum, row in enumerate(dict_kind_animal):
                print(f"{enum + 1} - {row['kind_animal']}")
            num = self.my_view.input_console('Input kind of animal(only number): ')

            try:
                num_correct = int(num)
                if 0 < num_correct < length:
                    break
                else:
                    self.my_view.output_console(f'The number must be between 1 and {length}', False)
                    continue
            except ValueError:
                self.my_view.output_console('You input no correct number! Try again.', False)

        return num

    # def check_frequency_toy(self):
    #     while True:
    #         try:
    #             num = int(self.my_view.input_console('Введите частоту выпадения игрушки: '))
    #             if 0< num < 100:
    #                 break
    #             else:
    #                 self.my_view.output_console('Число должно быть в диапозоне от 0 до 100', False)
    #                 continue
    #         except ValueError:
    #             self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)
    #
    #     return num
    #
    # def check_number_toy(self, data):
    #     count_toy = len(data)
    #     while True:
    #         try:
    #             num = int(self.my_view.input_console('Введите номер игрушки для изменения частоты: '))
    #             if 0< num <= count_toy:
    #                 break
    #             else:
    #                 self.my_view.output_console('Игрушка с таким номером отсутствует', False)
    #                 continue
    #         except ValueError:
    #             self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)
    #
    #     return num
