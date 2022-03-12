from datetime import date

import login_page as lg
import tkinter as tk
import entities.vehicle as ev
import select_menu as sm
import search_customer_page as scp
import search_vehicle_page as svp
import add_customer_page as acp
import select_menu as sm
import sql_pool as sp
import tkinter.messagebox
import login_page as lp

class AddSalesTransaction(object):

    def __init__(self, window, role, vehicle = None, customer = None):
        self.window = window
        self.window.config(bg = 'white')
        self.add_sales_transaction = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.add_sales_transaction.place(x = 0, y = 0)
        self.role = role
        self.vehicle = vehicle
        self.customer = customer
        # sale transaction infomation
        self.vin = tk.StringVar()
        if self.vehicle:
            self.vin.set(self.vehicle.vin)
        self.customerID = tk.StringVar()
        if self.customer:
            print("phone:  "+self.customer.phone_number)
            print("address:  "+self.customer.address)
            print("email:  "+self.customer.email)
            print(sp.AddSalesTransaction.getCustomerID(phone_number = self.customer.phone_number,
                                                       address = self.customer.address,
                                                       email = self.customer.email))
            customerID = str(sp.AddSalesTransaction.getCustomerID(phone_number = self.customer.phone_number,
                                                       address = self.customer.address,
                                                       email = self.customer.email))
            self.customerID.set(customerID)
        self.username = tk.StringVar()
        self.username.set(lp.LoginPage.userID)
        self.sold_price = tk.StringVar()
        # self.sold_price.set("5000")
        self.sold_date = tk.StringVar()
        # self.sold_date.set("2021-11-15")
        self.create_frame()

    def create_frame(self):

        tk.Label(self.add_sales_transaction, text='Sell vehicles:').place(x = 400, y = 50)

        tk.Label(self.add_sales_transaction, text = 'VIN: ').place(x = 200, y = 100)
        tk.Label(self.add_sales_transaction, text = 'CustomerID: ').place(x = 200, y = 150)
        tk.Label(self.add_sales_transaction, text = 'Username: ').place(x = 200, y = 200)
        tk.Label(self.add_sales_transaction, text = 'Sold Price:').place(x = 200, y = 250)
        # tk.Label(self.add_sales_transaction, text = 'Sold Date:').place(x = 200, y = 300)

        tk.Entry(self.add_sales_transaction, textvariable = self.vin).place(x = 500, y = 100)
        tk.Entry(self.add_sales_transaction, textvariable = self.customerID).place(x = 500, y = 150)
        tk.Entry(self.add_sales_transaction, textvariable = self.username).place(x = 500, y = 200)
        tk.Entry(self.add_sales_transaction, textvariable = self.sold_price).place(x = 500, y = 250)
        # tk.Entry(self.add_sales_transaction, textvariable = self.sold_date).place(x = 500, y = 300)
        self.sold_date.set(date.today())

        btn_search_customer = tk.Button(self.add_sales_transaction, text = 'search vehicle', command = self.jump_to_search_vehicle)
        btn_search_customer.place(x = 100, y = 500)
        btn_search_customer = tk.Button(self.add_sales_transaction, text = 'search customer', command = self.jump_to_search_customer)
        btn_search_customer.place(x = 300, y = 500)
        btn_add_customer = tk.Button(self.add_sales_transaction, text = 'add customer', command = self.jump_to_add_new_customer)
        btn_add_customer.place(x = 500, y = 500)

        btn_add_vehicle = tk.Button(self.add_sales_transaction, text = 'create sales transaction', command = self.create_sales_transaction)
        btn_add_vehicle.place(x = 300, y = 700)
        btn_jump_to_select_menu = tk.Button(self.add_sales_transaction, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 500, y = 700)

    def jump_to_search_vehicle(self):
        self.add_sales_transaction.destroy()
        svp.SearchVehiclePage(self.window, role = self.role, customer = self.customer)

    def jump_to_search_customer(self):
        self.add_sales_transaction.destroy()
        scp.SearchCustomerPage(self.window, self.role, self.vehicle)

    def jump_to_add_new_customer(self):
        self.add_sales_transaction.destroy()
        acp.AddCustomerPage(self.window, self.role, self.vehicle)

    def jump_to_login_page(self):
        self.add_sales_transaction.destroy()
        lg.LoginPage(self.window)

    def jump_to_select_menu(self):
        self.add_sales_transaction.destroy()
        sm.SelectMenu(self.window, self.role)

    def create_sales_transaction(self):
        if self.vehicle:
            if self.role == 'salespeople' and float(self.sold_price.get()) < 0.95 * self.vehicle.invoice_price:
                tkinter.messagebox.showinfo(title = 'message', message = "sold price can not below 95% of the invoice price")
                return
        else:
            tkinter.messagebox.showinfo(title = 'message', message = "Vehicle doesn't exist")

            return
        self.add_sales_transaction.destroy()
        try:
            sp.AddSalesTransaction.addSalesTransaction(vin = self.vin.get(),
                                                       customerID = self.customerID.get(),
                                                       username = self.username.get(),
                                                       sold_price = self.sold_price.get(),
                                                       sold_date = self.sold_date.get())
            tkinter.messagebox.showinfo(title = 'message', message = 'successfully create the sales transaction')
        except:
            tkinter.messagebox.showinfo(title = 'message', message = 'Sorry, we are unable to create the sales transaction')
        finally:
            sm.SelectMenu(self.window, self.role)