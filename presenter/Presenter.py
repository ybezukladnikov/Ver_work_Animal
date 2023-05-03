from view.ViewConsole import ViewConsole
from model.AnimalShelter import AnimalShelter
from model.Check import Check
class Presenter:
    view = ViewConsole()
    nursery = AnimalShelter()
    def run(self):
        while True:
            self.view.output_console(f"Welcome to Our Animal Shelter \"{AnimalShelter().name}\"", True)
            self.view.show_main_menu()
            menu_item = Check().check_main_menu()
            match menu_item:
                case 0:
                    break
                case 1:
                    self.nursery.get_list_animal()
                    self.view.show_animal_in_nursery(self.nursery.list_animal)
                case 2:
                    self.nursery.add_animal_inDB()
                case 3:
                    self.nursery.show_list_com_selected_animal()

                # case 4:
                #     self.nursery.give_toy()
                # case 5:
                #     self.nursery.play_toy()
                # case 6:
                #     self.nursery.get_list_toy_issued()
                #     self.view.show_list_toy_issued(self.nursery.list_toy_issued)
                # case 7:
                #     self.nursery.change_frequency_toy()
                #
                #
                #
                #
