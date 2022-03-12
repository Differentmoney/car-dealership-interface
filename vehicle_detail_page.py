import login_page as lg
import add_vehicle_page as avp
import tkinter as tk
import add_sales_transaction as ast
import select_menu as sm
import sql_pool as sql
import search_vehicle_page as svp
from tkinter import *
from tkinter import ttk


import tkinter as tk

from tkinter import *
from tkinter import ttk

class VehicleDetailPage(object):

    def __init__(self, window, vehicle, role = None, customer = None):
        self.window = window
        self.window.config(bg = 'white')
        self.vehicle_detail_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.vehicle_detail_page.place(x = 0, y = 0)
        self.role = role
        self.vehicle = vehicle
        self.customer = customer
        self.create_frame()
        self.win2 = window

    def create_frame(self):
        #svp.SearchVehiclePage(self.window, self.role)
        tk.Label(self.vehicle_detail_page, text='Vehicle Detail:').place(x = 400, y = 50)
        btn_jump_to_select_menu = tk.Button(self.vehicle_detail_page, text='back to select menu', command=self.jump_select_menu)
        btn_jump_to_select_menu.place(x=400, y=700)
        win = Tk() 
        self.win2=win 
        # Set the size of the tkinter window    
        win.geometry("800x800")
        win.title("Vehicle Detail")
        # Create an object of Style widget
        style = ttk.Style()
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("Attributes Name", "Value",), show='headings', height=13)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Attributes Name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Value")

        attr_values = [["VIN", self.vehicle.vin],
                    ["Model", self.vehicle.model],
                    ["Model year", str(self.vehicle.model_year)],
                    ["Color",self.vehicle.color],
                    ["List price", str(self.vehicle.list_price)],
                    ["Vehicle Type", self.vehicle.type],
                    ["Description", self.vehicle.description]]
        carDetail = self.vehicle.detail.strip().split(',')                    
        if(self.vehicle.type == 'Car'):
            tem = ["Type Detail: Number of Doors",carDetail[0]]
            attr_values.append(tem)
        elif(self.vehicle.type == 'SUV'):
            attr_values.append(["Type Detail: Num Cupholders",carDetail[0]])
            attr_values.append(["Type Detail: Drive Train Type",carDetail[1]])
        elif(self.vehicle.type == 'Van'):
            if(carDetail[0] == "1"):
                attr_values.append(["Type Detail: Driver Side Door","Yes"])
            elif(carDetail[0] == "0"):
                attr_values.append(["Type Detail: Driver Side Door","No"])
        elif(self.vehicle.type == 'Convertible'):
            attr_values.append(["Type Detail: Back Seat Count",carDetail[0]])
            attr_values.append(["Type Detail: Roof Type",carDetail[1]])
        elif(self.vehicle.type == 'Truck'):
            attr_values.append(["Type Detail: Num Rear Axles",carDetail[0]])
            attr_values.append(["Type Detail: Capacity",carDetail[1]])
            if(len(carDetail) == 3):
                attr_values.append(["Type Detail: Cover Type",carDetail[2]])
        attr_values.append(["Manufacturer Name",self.vehicle.manufacturerName])
        if (self.role == "manager" or self.role == "owner"):
            attr_values.append(["Add date", self.vehicle.adddate])
            attr_values.append(["Inventory Clerk", sql.SearchVehicle.getUserName(sql.SearchVehicle.searchUserName(self.vehicle.vin))])
        if(self.role == "manager" or self.role == "owner" or self.role == "clerk"):
            attr_values.append(["Invoice Price", self.vehicle.invoice_price])
                
        for row in attr_values:
            tree.insert("", "end", values=(row[0], row[1]))
        tree.pack()

        result = sql.SearchVehicle.viewOneSell(self.vehicle.vin)
        didSold = False
        if(len(result)!= 0):
            didSold = True
        if(didSold):
            tree = ttk.Treeview(win, column=("vin", "soldPrice", "SoldDate"), show='headings', height=1)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="vin")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="soldPrice")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="SoldDate")
            Cid = ""
            # Insert the data in Treeview widget
            for row in result:
                Cid = row[1]
                tree.insert("", "end", values=(row[0], row[3], row[4]))
            tree.pack()

            result = sql.SearchVehicle.searchIndividual(str(Cid))
            if(len(result) == 0):
                result = sql.SearchVehicle.searchBusiness(str(Cid))
            tree = ttk.Treeview(win, column=("Customer Name", "Phone Number", "Email"), show='headings', height=1)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Customer Name")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Phone Number")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Email")
            
            # Insert the data in Treeview widget
            for row in result:
                tree.insert("", "end", values=(row[0], row[1], row[2]))
            tree.pack()

        completeRepair, openRepair = sql.SearchRepair.getRepairList(self.vehicle.vin)
        allRepair = completeRepair
        if (len(openRepair) !=0):
            allRepair.append(openRepair[0])

        if (len(allRepair) !=0):
            tree = ttk.Treeview(win, column=("Customer Name", "Service Writer", "Start Date", "Complete Date", "Labor Charge", "Parts Cost", "Total Cost"), show='headings', height=10)
            tree.column("# 1", anchor=CENTER, minwidth=0, width=120, stretch=True)
            tree.heading("# 1", text="Customer Name")
            tree.column("# 2", anchor=CENTER, minwidth=0, width=120, stretch=True)
            tree.heading("# 2", text="Service Writer")
            tree.column("# 3", anchor=CENTER, minwidth=0, width=90, stretch=True)
            tree.heading("# 3", text="Start Date")
            tree.column("# 4", anchor=CENTER, minwidth=0, width=90, stretch=True)
            tree.heading("# 4", text="Complete Date")
            tree.column("# 5", anchor=E, minwidth=0, width=80, stretch=True)
            tree.heading("# 5", text="Labor Charge")
            tree.column("# 6", anchor=E, minwidth=0, width=80, stretch=True)
            tree.heading("# 6", text="Parts Cost")
            tree.column("# 7", anchor=E, minwidth=0, width=80, stretch=True)
            tree.heading("# 7", text="Total Cost")

            for i in range(len(allRepair)):
                userName = sql.SearchVehicle.getUserName(allRepair[i].username)
                customerValue = sql.SearchVehicle.searchIndividual(allRepair[i].customerID)
                if (len(customerValue) == 0):
                    customerValue = sql.SearchVehicle.searchBusiness(allRepair[i].customerID)
                customerName = customerValue[0][0]
                partCost = 0
                if (len(allRepair[i].parts) !=0):
                    for part in allRepair[i].parts:
                        partCost = partCost + part.quantity * part.price
                totalCost = partCost + allRepair[i].laborcharge
                tree.insert("", "end", values=(customerName, userName, allRepair[i].startdate,
                                               allRepair[i].completedate, allRepair[i].laborcharge, round(partCost,2), round(totalCost,2)))
            tree.pack()

        btn_jump_to_login = tk.Button(win, text = 'back to login page', command = self.jump_to_login_page)
        btn_jump_to_login.place(x = 600, y = 700)
       
        if self.role != None : 
            btn_jump_to_select_menu = tk.Button(win, text = 'back to select menu', command = self.jump_to_select_menu)
            btn_jump_to_select_menu.place(x = 400, y = 700)
        
        if self.role in ['owner', 'clerk']:
            btn_add_more_vehicle = tk.Button(win, text = 'add more vehicles', command = self.jump_to_add_vehicle_page)
            btn_add_more_vehicle.place(x = 50, y = 700)
        

        if self.role in ['owner', 'salespeople'] and not didSold:
            btn_sell_vehicle = tk.Button(win, text = 'sell this vehicle', command = self.jump_to_add_sales_transaction)
            btn_sell_vehicle.place(x = 250, y = 700)        
   
        win.mainloop()

    def jump_to_login_page(self):
        lg.LoginPage.setUserID()
        self.vehicle_detail_page.destroy()
        if self.win2 != None:
            self.win2.destroy()
        lg.LoginPage(self.window)

    def jump_to_select_menu(self):
        if self.win2 != None:
            self.win2.destroy()
        self.vehicle_detail_page.destroy()
        sm.SelectMenu(self.window, self.role)

    def jump_select_menu(self):
        self.vehicle_detail_page.destroy()
        sm.SelectMenu(self.window, self.role)

    def jump_to_add_vehicle_page(self):
        if self.win2 != None:
            self.win2.destroy()
        self.vehicle_detail_page.destroy()
        avp.AddVehiclePage(self.window, self.role)

    def jump_to_add_sales_transaction(self):
        if self.win2 != None:
            self.win2.destroy()
        self.vehicle_detail_page.destroy()
        ast.AddSalesTransaction(self.window, self.role, vehicle = self.vehicle, customer = self.customer)