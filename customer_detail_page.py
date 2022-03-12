import login_page as lg
import add_vehicle_page as avp
import tkinter as tk
import entities.vehicle as ev
import add_sales_transaction as ast
import add_repair_form as arf
import add_customer_page as acp
import select_menu as sm
import sql_pool as sp

class CustomerDetailPage(object):

    def __init__(self, window, role, customer, vehicle = None, cid = None, vin = None):
        self.window = window
        self.window.config(bg = 'white')
        self.customer_detail_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.customer_detail_page.place(x = 0, y = 0)
        self.role = role
        self.customer = customer
        self.vehicle = vehicle
        self.cid = cid
        self.vin = vin
        self.create_frame()

    def create_frame(self):
        tk.Label(self.customer_detail_page, text='Customer Detail:').place(x = 400, y = 50)

        tk.Label(self.customer_detail_page, text = 'Phone number: ' + self.customer.phone_number).place(x = 200, y = 150)
        tk.Label(self.customer_detail_page, text = 'Address: ' + self.customer.address).place(x = 200, y = 200)
        tk.Label(self.customer_detail_page, text = 'Email: ' + self.customer.email).place(x = 200, y = 250)

        self.__add_customer_specified_info()

        btn_add_more_customer = tk.Button(self.customer_detail_page, text = 'add more customer', command = self.jump_to_add_customer_page)
        btn_add_more_customer.place(x = 400, y = 500)

        if self.role in ['owner', 'servicewriter']:
            if self.vin is not None:
                btn_add_more_vehicle = tk.Button(self.customer_detail_page, text = 'add customer to new repair form', command = self.jump_to_add_repair_form)
                btn_add_more_vehicle.place(x = 50, y = 700)

        if self.role in ['owner', 'salespeople']:
            btn_sell_vehicle = tk.Button(self.customer_detail_page, text = 'add customer to sales transaction', command = self.jump_to_add_sales_transaction)
            btn_sell_vehicle.place(x = 300, y = 700)            

        btn_jump_to_select_menu = tk.Button(self.customer_detail_page, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 550, y = 700)

    def jump_to_add_customer_page(self):
        self.customer_detail_page.destroy()
        acp.AddCustomerPage(self.window, self.role, vehicle = self.vehicle)

    def jump_to_add_repair_form(self):
        self.customer_detail_page.destroy()
        arf.AddRepairForm(self.window, self.role, None, self.cid, self.vin)

    def jump_to_add_sales_transaction(self):
        self.customer_detail_page.destroy()
        ast.AddSalesTransaction(self.window, self.role, vehicle = self.vehicle, customer = self.customer)

    def jump_to_login_page(self):
        self.customer_detail_page.destroy()
        lg.LoginPage(self.window)
    
    def jump_to_select_menu(self):
        self.customer_detail_page.destroy()
        sm.SelectMenu(self.window, self.role)

    def __add_customer_specified_info(self):
        if self.customer.isBusiness:
            tk.Label(self.customer_detail_page, text = 'taxID: ' + self.customer.taxID).place(x = 200, y = 300)
            tk.Label(self.customer_detail_page, text = 'Business name: ' + self.customer.business_name).place(x = 200, y = 350)
            tk.Label(self.customer_detail_page, text = 'primary contact name: ' + self.customer.primary_contact_name).place(x = 200, y = 400)
            tk.Label(self.customer_detail_page, text = 'primary contact title: ' + self.customer.primary_contact_title).place(x = 200, y = 450)
        if self.customer.isIndividual:
            tk.Label(self.customer_detail_page, text = 'Driver license: ' + self.customer.driver_license).place(x = 200, y = 300)
            tk.Label(self.customer_detail_page, text = 'Frist name: ' + self.customer.first_name).place(x = 200, y = 350)
            tk.Label(self.customer_detail_page, text = 'Last name: ' + self.customer.last_name).place(x = 200, y = 400)