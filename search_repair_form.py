import tkinter as tk
from tkinter import messagebox
import search_result_of_repair_form_list as srorfl
import select_menu as sm
import sql_pool as sp


class SearchRepairForm(object):

    def __init__(self, window, role):
        self.window = window
        self.window.config(bg = 'white')
        self.search_repair_form = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.search_repair_form.place(x = 0, y = 0)
        self.role = role
        self.vin = tk.StringVar()
        self.create_frame()

    def create_frame(self):

        tk.Label(self.search_repair_form, text='Search Repair Transaction:').place(x = 400, y = 50)

        tk.Label(self.search_repair_form, text = 'Please input VIN: ').place(x = 200, y = 100)
        tk.Entry(self.search_repair_form, textvariable = self.vin).place(x = 500, y = 100)

        btn_search_customer = tk.Button(self.search_repair_form, text = 'search', command = self.search_repair_form_result)
        btn_search_customer.place(x = 200, y = 600)

        btn_jump_to_select_menu = tk.Button(self.search_repair_form, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 600, y = 600)

    def search_repair_form_result(self):
        if self.vin.get() == "":
            messagebox.showerror("Error!", "Please enter a vehicle vin", parent=self.window)
        elif sp.SearchRepair.checkVin(self.vin.get()):
            messagebox.showinfo("Error!", "Sorry, this vehicle has not been sold yet or it is not in our database", parent=self.window)
        else:
            vehicle = sp.SearchRepair.getVheicle(self.vin.get())
            self.search_repair_form.destroy()
            complete_repair_form, on_going_repair_form = sp.SearchRepair.getRepairList(self.vin.get())
            srorfl.SearchResultOfRepairFormList(self.window, self.role, complete_repair_form, on_going_repair_form, vehicle)

    def jump_to_select_menu(self):
        self.search_repair_form.destroy()
        sm.SelectMenu(self.window, self.role)