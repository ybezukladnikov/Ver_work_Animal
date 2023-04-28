from model.ReadWriteBD import ReadWriteBD
from view.ViewConsole import ViewConsole


class Check:
    my_view = ViewConsole()
    def check_main_menu(self):
        while True:
            try:
                num = int(self.my_view.input_console('Введите номер пункта, который хотите выполнить: '))
                if 0 <= num <= 7:
                    break
                else:
                    self.my_view.output_console('Такого пункта меню нет! Попробуйте снова.', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num

    def check_name_toy(self):
        while True:
            name = self.my_view.input_console('Введите название игрушки (до 15 символов): ')

            if len(name)>15 or len(name)==0:
                self.my_view.output_console('Неверная длина названия', False)
                continue
            flag = False
            for row in ReadWriteBD().read_write_bd("SELECT * FROM `toys_in_shop`", 'r'):
                if name == row['title_toy']:
                    flag = True
            if flag:
                self.my_view.output_console('Такое имя уже есть в базе', False)
                continue

            break
        return name

    def check_amount_toy(self):
        while True:
            try:
                num = int(self.my_view.input_console('Введите количество игрушек: '))
                if num >= 0:
                    break
                else:
                    self.my_view.output_console('Число не может быть отрицательным', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num

    def check_frequency_toy(self):
        while True:
            try:
                num = int(self.my_view.input_console('Введите частоту выпадения игрушки: '))
                if 0< num < 100:
                    break
                else:
                    self.my_view.output_console('Число должно быть в диапозоне от 0 до 100', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num

    def check_number_toy(self, data):
        count_toy = len(data)
        while True:
            try:
                num = int(self.my_view.input_console('Введите номер игрушки для изменения частоты: '))
                if 0< num <= count_toy:
                    break
                else:
                    self.my_view.output_console('Игрушка с таким номером отсутствует', False)
                    continue
            except ValueError:
                self.my_view.output_console('Вы ввели некорректное число! Попробуйте снова.', False)

        return num








