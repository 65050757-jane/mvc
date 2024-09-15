# from model import DataStorage, MilkProductionData
from view.view import MainView
import tkinter as tk


class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = MainView(self.root, self)
        self.main_view.create_window()
        self.root.mainloop()
 
class GoatController:
    pass

class CowController:
    pass


if __name__ == '__main__':
    controller = MainController()
    