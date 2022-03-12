import login_page as lg
import tkinter as tk

class SearchSalesTransaction(object):

    def __init__(self, window, role):
        self.window = window
        self.window.config(bg = 'blue')
        self.search_sales_transaction = tk.Frame(self.window)
        self.search_sales_transaction.pack()
        self.role = role
        self.create_frame()

    def create_frame(self):
        btn_jump_to_login = tk.Button(self.search_sales_transaction, text = 'back to login page', command = self.jump_to_login_page)
        btn_jump_to_login.pack()
   
    def jump_to_login_page(self):
        self.search_sales_transaction.destroy()
        lg.LoginPage(self.window)