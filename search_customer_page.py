import login_page as lg
import tkinter as tk
import entities.vehicle as ev
import select_menu as sm
import entities.customer as ec
import tkinter.messagebox
import customer_detail_page as cdp
import sql_pool as sp

class SearchCustomerPage(object):

    def __init__(self, window, role, vehicle = None, vin = None):
        self.window = window
        self.window.config(bg = 'white')
        self.search_customer_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.search_customer_page.place(x = 0, y = 0)
        self.role = role
        self.vehicle = vehicle
        self.vin = vin
        # sale transaction infomation
        self.taxID_or_driver_license = tk.StringVar()
        self.taxID = tk.StringVar()
        self.driver_license = tk.StringVar()
        self.cid = tk.StringVar()
        self.create_frame()

    def create_frame(self):

        tk.Label(self.search_customer_page, text='Search Customer:').place(x = 400, y = 50)

        tk.Label(self.search_customer_page, text = 'Please input either tax ID or driver license: ').place(x = 200, y = 100)
        tk.Label(self.search_customer_page, text = 'Search by driver license: ').place(x = 200, y = 150)
        tk.Entry(self.search_customer_page, textvariable = self.driver_license).place(x = 500, y = 150)
        tk.Label(self.search_customer_page, text = 'Search by tax ID: ').place(x = 200, y = 200)
        tk.Entry(self.search_customer_page, textvariable = self.taxID).place(x = 500, y = 200)

        btn_search_customer = tk.Button(self.search_customer_page, text = 'search', command = self.search_customer_result)
        btn_search_customer.place(x = 300, y = 500)

        btn_jump_to_select_menu = tk.Button(self.search_customer_page, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 300, y = 700)

    def search_customer_result(self):
        # if we did not find the customer, pop out a error messagebox
        # otherwise, we will jump to that customer detail page

        if self.taxID.get() == '' and self.driver_license.get() == '':
            tk.messagebox.showinfo('Error', 'Please input either tax ID or driver license')
        elif self.taxID.get() != '' and self.driver_license.get() != '':
            tk.messagebox.showinfo('Error', 'Please fill out either tax ID or driver license, not both')
        elif self.driver_license.get() != '':
            detail = sp.SearchCustomer.search_by_driverlicensenumber(self.driver_license.get())
            # Check if customer exists
            if len(detail) == 0:
                tkinter.messagebox.showinfo('Error', 'No such customer')
            else:
                customer = ec.Individual(
                    phone_number = detail[0][2],
                    address = detail[0][1],
                    email = detail[0][0],
                    driver_license = detail[0][3],
                    first_name = detail[0][4],
                    last_name = detail[0][5])    
                self.cid.set(detail[0][6])               
                # Leave current page
                self.search_customer_page.destroy()
                cdp.CustomerDetailPage(self.window, self.role, customer, self.vehicle, self.cid, self.vin)
                return 

 
        elif self.taxID.get() != '':
            detail = sp.SearchCustomer.search_by_TaxID(self.taxID.get())
            #Check if taxID exists
            if len(detail) == 0:
                tkinter.messagebox.showinfo('Error', 'No such customer')
            else:
                customer = ec.Business(
                    phone_number = detail[0][2],
                    address = detail[0][1],
                    email = detail[0][0],
                    taxID = detail[0][3],
                    business_name = detail[0][4],
                    primary_contact_name = detail[0][5],
                    primary_contact_title = detail[0][6])
                self.cid.set(detail[0][7])
                # Leave current page
                self.search_customer_page.destroy()
                cdp.CustomerDetailPage(self.window, self.role, customer, self.vehicle, self.cid, self.vin)
                return     
        else:
            tkinter.messagebox.showinfo(title = 'message', message = 'Sorry, we did not find this customer')

    def jump_to_login_page(self):
        self.search_customer_page.destroy()
        lg.LoginPage(self.window)
    
    def jump_to_select_menu(self):
        self.search_customer_page.destroy()
        sm.SelectMenu(self.window, self.role)
