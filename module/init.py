from module.MenuClass import Menu
from module.GaussClass import Gauss
from module.GaussJordanClass import GaussJordan

menu = Menu(True)
gauss = Gauss(True)
gauss_jordan = GaussJordan(True)

def init():
    menu.main_menu()
