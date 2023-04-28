# from view.ViewConsole import ViewConsole
# from model.Shop import Shop
# from model.Check import Check
# class Presenter:
#     view = ViewConsole()
#     shop = Shop()
#     def run(self):
#         while True:
#             self.view.output_console(f"Магазин игрушек {Shop().name}",True)
#             self.view.show_main_menu()
#             menu_item = Check().check_main_menu()
#             match menu_item:
#                 case 0:
#                     break
#                 case 1:
#                     self.shop.get_list_toy()
#                     self.view.show_toys_in_shop(self.shop.list_toy)
#                 case 2:
#                     self.shop.add_toy_inDB()
#                 case 3:
#                     self.shop.get_list_for_issue()
#                     self.view.show_list_for_issue(self.shop.list_for_issue)
#                 case 4:
#                     self.shop.give_toy()
#                 case 5:
#                     self.shop.play_toy()
#                 case 6:
#                     self.shop.get_list_toy_issued()
#                     self.view.show_list_toy_issued(self.shop.list_toy_issued)
#                 case 7:
#                     self.shop.change_frequency_toy()
#
#


