import login_page as lg
import tkinter as tk
import search_repair_form as srf
import select_menu as sm
import add_customer_page as acp
import search_customer_page as scp
from sql_pool import Repair
from datetime import date as day


class AddRepairForm(object):

    def __init__(self, window, role, customer = None, cid = None, vin = None):
        self.window = window
        self.window.config(bg = 'white')
        self.add_repair_form = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.add_repair_form.place(x = 0, y = 0)
        self.role = role
        self.customer = customer
        self.parts = []
        self.cid = cid
        self.vin = vin
        self.create_frame()

    def create_frame(self):
        tk.Label(self.add_repair_form, text = 'Add repair form:').place(x = 400, y = 50)
        tk.Label(self.add_repair_form, text = 'Vechile Info:').place(x = 100, y = 100)

        btn_search_customer = tk.Button(self.add_repair_form, text = 'search customer', command = self.jump_to_search_customer)
        btn_search_customer.place(x = 500, y = 100)
        btn_add_customer = tk.Button(self.add_repair_form, text = 'add customer', command = self.jump_to_add_new_customer)
        btn_add_customer.place(x = 650, y = 100)

        tk.Label(self.add_repair_form, text = 'Vin: ').place(x = 100, y = 150)
        tk.Label(self.add_repair_form, text=self.vin).place(x=200, y=150, width=150)

        tk.Label(self.add_repair_form, text = 'CustomerID: ').place(x = 500, y = 150)
        tk.Label(self.add_repair_form, textvariable=self.cid).place(x=600, y=150, width = 30)

        tk.Label(self.add_repair_form, text = 'Repair Info:').place(x = 100, y = 250)
        
        tk.Label(self.add_repair_form, text = 'Start Date').place(x = 100, y = 300)
        self.start_date = tk.StringVar()
        # self.start_date.set(self.repair.start_date)
        tk.Label(self.add_repair_form, text = day.today()).place(x = 200, y = 300)      

        tk.Label(self.add_repair_form, text = 'Username').place(x = 500, y = 300)
        self.username = tk.StringVar()
        self.username.set(lg.LoginPage.userID)
        # self.username.set(self.repair.username)
        tk.Label(self.add_repair_form, textvariable=self.username).place(x=600, y=300, width=60)

        tk.Label(self.add_repair_form, text = 'Odometer').place(x = 100, y = 350)
        self.odometer= tk.StringVar()
        # self.odometer.set(self.repair.odometer)
        odometer_entry = tk.Entry(self.add_repair_form, textvariable = self.odometer)
        odometer_entry.place(x = 200, y = 350)

        tk.Label(self.add_repair_form, text = 'Labor Charge').place(x = 500, y = 350)
        self.labor_charge = tk.StringVar()
        # self.labor_charge.set(self.repair.labor_charge)
        labor_charge_entry = tk.Entry(self.add_repair_form, textvariable = self.labor_charge)
        labor_charge_entry.place(x = 600, y = 350)


        tk.Label(self.add_repair_form, text = 'Description').place(x = 100, y = 400)
        self.description = tk.StringVar()
        # self.description.set(self.repair.description)
        description_entry = tk.Entry(self.add_repair_form, textvariable = self.description)
        description_entry.place(x = 200, y = 400)

        self.cor_x_next, self.cor_y_next = 50, 450

        btn_add_parts = tk.Button(self.add_repair_form, text = 'add parts', command = self.add_parts)
        btn_add_parts.place(x = 100, y = 700)

        btn_add_parts = tk.Button(self.add_repair_form, text = 'create', command = self.create_repair_form)
        btn_add_parts.place(x = 250, y = 700)

        btn_jump_to_search_repair_page = tk.Button(self.add_repair_form, text = 'search repair page', command = self.jump_to_search_repair_page)
        btn_jump_to_search_repair_page.place(x = 400, y = 700)

        btn_jump_to_select_menu = tk.Button(self.add_repair_form, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 600, y = 700)
    
    def add_parts(self):

        tem = []
        tk.Label(self.add_repair_form, text = 'PartNumber').place(x = self.cor_x_next, y = self.cor_y_next)
        self.part_number = tk.StringVar()
        tem.append(self.part_number)
        part_number_entry = tk.Entry(self.add_repair_form, textvariable = self.part_number, width = 5)
        part_number_entry.place(x = self.cor_x_next + 100, y = self.cor_y_next)        
        tk.Label(self.add_repair_form, text = 'Quantity').place(x = self.cor_x_next + 200, y = self.cor_y_next)
        self.quantity = tk.StringVar()
        tem.append(self.quantity)
        quantity_entry = tk.Entry(self.add_repair_form, textvariable = self.quantity, width = 5)
        quantity_entry.place(x = self.cor_x_next + 300, y = self.cor_y_next) 
        tk.Label(self.add_repair_form, text = 'Price').place(x = self.cor_x_next + 400, y = self.cor_y_next)
        self.price = tk.StringVar()
        tem.append(self.price)
        price_entry = tk.Entry(self.add_repair_form, textvariable = self.price, width = 5)
        price_entry.place(x = self.cor_x_next + 450, y = self.cor_y_next) 
        tk.Label(self.add_repair_form, text = 'Vender Name').place(x = self.cor_x_next + 550, y = self.cor_y_next)
        self.vender_name = tk.StringVar()
        tem.append(self.vender_name)
        self.parts.append(tem)
        vender_name_entry = tk.Entry(self.add_repair_form, textvariable = self.vender_name, width = 5)
        vender_name_entry.place(x = self.cor_x_next + 650, y = self.cor_y_next)
        self.cor_x_next = self.cor_x_next
        self.cor_y_next = self.cor_y_next + 50
        print(self.cor_x_next, self.cor_y_next)

    def create_repair_form(self):
        #call create repair form 
        Repair.create_repair(self.vin, self.cid.get(), self.username.get(), self.description.get(), self.odometer.get(), self.labor_charge.get() )
        print("finished add repair ...")
        for ele in self.parts:
            if (ele[0].get()!="" and ele[1].get()!="" and ele[2].get()!="" and ele[3].get()!=""):
                Repair.add_part(self.vin,self.cid.get(), ele[0].get(), ele[1].get(), ele[2].get(), ele[3].get()) 
        self.jump_to_search_repair_page()

    def jump_to_search_repair_page(self):
        self.add_repair_form.destroy()
        srf.SearchRepairForm(self.window, self.role)

    def jump_to_login_page(self):
        lg.LoginPage.setUserID()
        self.add_repair_form.destroy()
        lg.LoginPage(self.window)
    
    def jump_to_select_menu(self):
        self.add_repair_form.destroy()
        sm.SelectMenu(self.window, self.role)
    
    def jump_to_add_new_customer(self):
        self.add_repair_form.destroy()
        acp.AddCustomerPage(self.window, self.role, None, self.vin)
    
    def jump_to_search_customer(self):
        self.add_repair_form.destroy()
        scp.SearchCustomerPage(self.window, self.role, None, self.vin)