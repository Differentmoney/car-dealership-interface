from tkinter import messagebox
import login_page as lg
import tkinter as tk
import entities.vehicle as ev
import entities.customer as ec
import customer_detail_page as cdp
import tkinter.messagebox
import select_menu as sm
import sql_pool as sp

class AddCustomerPage(object):

    def __init__(self, window, role = None, vehicle = None, vin = None):
        self.window = window
        self.window.config(bg = 'white')
        self.add_customer_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.add_customer_page.place(x = 0, y = 0)
        self.role = role
        self.vehicle = vehicle
        # customer properties
        self.customerID=tk.StringVar()
        self.phone_number = tk.StringVar()
        self.address = tk.StringVar()
        self.email = tk.StringVar()
        self.taxID = tk.StringVar()
        self.business_name = tk.StringVar()
        self.primary_contact_name = tk.StringVar()
        self.primary_contact_title = tk.StringVar()
        self.driver_license = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.vin = vin
        self.cid = tk.StringVar()
        self.create_frame()

    def create_frame(self):
        tk.Label(self.add_customer_page, text = 'Add Customer:').place(x = 400, y = 50)
        # General info
        tk.Label(self.add_customer_page, text = 'Phone Number: ').place(x = 200, y = 150)
        tk.Label(self.add_customer_page, text = 'Address: ').place(x = 200, y = 200)
        tk.Label(self.add_customer_page, text = 'Email: ').place(x = 200, y = 250)
        # individual only
        self.isIndividual = tk.IntVar()
        tk.Checkbutton(self.add_customer_page, text = 'Individual', variable = self.isIndividual).place(x = 200, y = 300)
        tk.Label(self.add_customer_page, text = 'Driver License: ').place(x = 200, y = 350)
        tk.Label(self.add_customer_page, text = 'First Name: ').place(x = 200, y = 400)
        tk.Label(self.add_customer_page, text = 'Last Name: ').place(x = 200, y = 450)
        # business only
        self.isBusiness = tk.IntVar()
        tk.Checkbutton(self.add_customer_page, text = 'Business', variable = self.isBusiness).place(x = 200, y = 500)
        tk.Label(self.add_customer_page, text = 'TaxID: ').place(x = 200, y = 550)
        tk.Label(self.add_customer_page, text = 'Business Name: ').place(x = 200, y = 600)
        tk.Label(self.add_customer_page, text = 'Primary Contact Name: ').place(x = 200, y = 650)
        tk.Label(self.add_customer_page, text = 'Primary Contact title: ').place(x = 200, y = 700)
        # General info entry
        tk.Entry(self.add_customer_page, textvariable = self.phone_number).place(x = 500, y = 150)
        tk.Entry(self.add_customer_page, textvariable = self.address).place(x = 500, y = 200)
        tk.Entry(self.add_customer_page, textvariable = self.email).place(x = 500, y = 250)
        # individual info entry
        tk.Entry(self.add_customer_page, textvariable = self.driver_license).place(x = 500, y = 350)
        tk.Entry(self.add_customer_page, textvariable = self.first_name).place(x = 500, y = 400)
        tk.Entry(self.add_customer_page, textvariable = self.last_name).place(x = 500, y = 450)
        # business info enty
        tk.Entry(self.add_customer_page, textvariable = self.taxID).place(x = 500, y = 550)
        tk.Entry(self.add_customer_page, textvariable = self.business_name).place(x = 500, y = 600)
        tk.Entry(self.add_customer_page, textvariable = self.primary_contact_name).place(x = 500, y = 650)
        tk.Entry(self.add_customer_page, textvariable = self.primary_contact_title).place(x = 500, y = 700)

        btn_add_customer = tk.Button(self.add_customer_page, text = 'Add', command = self.add_customer_and_jump_to_customer_detail)
        btn_add_customer.place(x = 300, y = 750)
        btn_jump_to_select_menu = tk.Button(self.add_customer_page, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 500, y = 750)
   
    def jump_to_login_page(self):
        self.add_customer_page.destroy()
        lg.LoginPage(self.window)
    
    def jump_to_select_menu(self):
        self.add_customer_page.destroy()
        sm.SelectMenu(self.window, self.role)

    def add_customer_and_jump_to_customer_detail(self):
        if (self.isIndividual.get() and self.isBusiness.get()) or (not self.isIndividual.get() and not self.isBusiness.get()):
            tkinter.messagebox.showinfo(title = 'message', message = 'you must check one and only one for Individual checkbox or Business checkbox')
            return
        if sp.Customer.check_driverslicense (self.driver_license.get()):
            tkinter.messagebox.showinfo ("Error!", "Customer exists", parent=self.window)
        elif self.isIndividual.get():
                customer = ec.Individual(
                                    self.phone_number.get(),
                                    self.address.get(),
                                    self.email.get(),
                                    self.driver_license.get(),
                                    self.first_name.get(),
                                    self.last_name.get())
        
        elif sp.Customer.check_taxid (self.taxID.get()):
            tkinter.messagebox.showinfo ("Error!", "Customer exists", parent=self.window)
        elif self.isBusiness.get():
            customer = ec.Business(
                                    self.phone_number.get(),
                                    self.address.get(),
                                    self.email.get(),
                                    self.taxID.get(),
                                    self.business_name.get(),
                                    self.primary_contact_name.get(),
                                    self.primary_contact_title.get())
 

        # individual
        if self.isIndividual.get() != 0:
            #driverlicensenumber, firstname, lastname
            if (customer.phone_number != '' and customer.address != '' and customer.email != '' and customer.driver_license != '' and customer.first_name != '' and customer.last_name != ''):
                id = sp.Customer.addIndivudal(self.phone_number.get(), self.address.get(), self.email.get(), self.driver_license.get(), self.first_name.get(), self.last_name.get())
                self.cid.set(id)
                        # if add vehicle successfully, jump to the detail page
                self.add_customer_page.destroy()
                cdp.CustomerDetailPage(self.window, 
                                    self.role, 
                                    customer, 
                                    self.vehicle,
                                    self.cid,
                                    self.vin)
            else:
                tkinter.messagebox.showinfo ("Error!", "Please fill out all fields", parent=self.window)
 

        else:
             #taxID, businessname, primarycontactname, primarycontacttitle
            if (customer.phone_number != '' and customer.address != '' and customer.email != '' and customer.taxID != '' and customer.business_name != '' and customer.primary_contact_name != '' and customer.primary_contact_title != ''):
                id = sp.Customer.addBuisness(self.phone_number.get(), self.address.get(), self.email.get(), self.taxID.get(), self.business_name.get(), self.primary_contact_name.get(), self.primary_contact_title.get())
                self.cid.set(id)
                        # if add vehicle successfully, jump to the detail page
                self.add_customer_page.destroy()
                cdp.CustomerDetailPage(self.window, 
                                    self.role, 
                                    customer, 
                                    self.vehicle,
                                    self.cid,
                                    self.vin)
            else:
                tkinter.messagebox.showinfo ("Error!", "Please fill out all fields", parent=self.window)


        pass