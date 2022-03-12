import tkinter as tk
import utilities as ut
import login_page as lg
import search_vehicle_page as svp
import add_vehicle_page as avp
import add_sales_transaction as ast
import search_repair_form as srf
import add_repair_form as arf
import search_sales_transaction as sst
import view_report as vr
import view_inventory as vi
import add_repair_form as arf

class SelectMenu(object):
    def __init__(self, window, role):
        self.window = window
        self.window.config(bg='green')
        self.select_menu = tk.Frame(self.window, bg = 'white', height = 400, width = 400)
        self.select_menu.place(x = 300, y = 200)
        self.role = role
        self.__create_select_menu()

    def __create_select_menu(self):
        if self.role in ['clerk','owner']:
            # TODO: create add_vehicles_page button
            btn_add_vehicle = tk.Button(self.select_menu, text='Add Vehicle', command = self.jump_to_add_vehicle_page)
            btn_add_vehicle.pack()
        if self.role in ['salespeople','owner','manager', 'clerk', 'servicewriter']:
            # TODO: create search_vehicle_page(different role versions) button
            btn_search_vehicle = tk.Button(self.select_menu, text='Search Vehicle', command = self.jump_to_search_vehicle_page)
            btn_search_vehicle.pack()
        if self.role in ['salespeople','owner']:
            # TODO: create add_sales_transaction button
            btn_add_sales_transaction = tk.Button(self.select_menu, text='Add Sales Transaction', command = self.jump_to_add_sales_transaction)
            btn_add_sales_transaction.pack()
        if self.role in ['servicewriter','owner','manager']:
            # TODO: create search_repair_form(different role versions) button
            btn_search_repair_form = tk.Button(self.select_menu, text='Search Repair Transaction', command = self.jump_to_search_repair_form)
            btn_search_repair_form.pack()

        if self.role in ['manager','owner']:
            # TODO: create view_report_button
            btn_view_report= tk.Button(self.select_menu, text='View Report', command = self.jump_to_view_report)
            btn_view_report.pack()

        btn_jump_to_login = tk.Button(self.select_menu, text = 'back to login page', command = self.jump_to_login_page)
        btn_jump_to_login.pack()

    def jump_to_search_vehicle_page(self):
        self.select_menu.destroy()
        svp.SearchVehiclePage(self.window, self.role)

    def jump_to_add_vehicle_page(self):
        self.select_menu.destroy()
        avp.AddVehiclePage(self.window, self.role)
    
    def jump_to_add_sales_transaction(self):
        self.select_menu.destroy()
        ast.AddSalesTransaction(self.window, self.role)

    def jump_to_search_repair_form(self):
        self.select_menu.destroy()
        srf.SearchRepairForm(self.window, self.role)

    def jump_to_view_inventory(self):
        self.select_menu.destroy()
        vi.ViewInventory(self.window, self.role)

    def jump_to_view_report(self):
        self.select_menu.destroy()
        vr.ViewReport(self.window, self.role)

    def jump_to_login_page(self):
        self.select_menu.destroy()
        lg.LoginPage(self.window)