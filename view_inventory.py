import login_page as lg
import tkinter as tk
import sql_pool as sql
import tkinter as tk

from tkinter import *
from tkinter import ttk

class ViewInventory(object):

    def __init__(self, window, role):
        self.window = window
        self.window.config(bg = 'blue')
        self.view_inventory = tk.Frame(self.window)
        self.view_inventory.pack()
        self.role = role
        self.create_frame()

    def create_frame(self):
        btn_jump_to_login = tk.Button(self.view_inventory, text = 'back to login page', command = self.jump_to_login_page)
        btn_jump_to_login.pack()

        result = sql.SearchVehicle.viewAvaliable()
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("800x800")
        win.title("View Inventory")
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vin", "model", "model year", "add date"), show='headings', height=30)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vin")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="model")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="model year")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="add date")


        # Jump to drill down report
        def jump_to_drilldown(a):
            curItem = tree.focus()
            vin = tree.item(curItem, 'values')[0]
            self.month_report(vin)
            

        tree.bind('<ButtonRelease-1>', jump_to_drilldown)
        # Insert the data in Treeview widget
        id = 0
        for row in result:
            index = str(id)
            tree.insert("", "end", values=(row[0], row[1], row[2], row[7]), tags=(index))
            id += 1
        tree.pack()

        win.mainloop()

    def sell_report(self,vin):
        print("in sell")
        result = sql.SearchVehicle.viewOneSell(vin)
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("800x200")
        win.title(str(vin) + "Sell Info")
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vin", "soldPrice", "SoldDate"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vin")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="soldPrice")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="SoldDate")
        
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[3], row[4]))
        tree.pack()

        win.mainloop()
   

    def month_report(self, vin):
        result = sql.SearchVehicle.viewOneAvaliable(vin)
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("800x800")
        win.title(str(vin) + "Basic Info")
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vin", "model", "model year", "invoice price", "list price", "description", "username", "add date", "vehicle color", "vehicle type", "vehicle detail", "manufacture name"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vin")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="model")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="model year")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="invoice price")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="list price")
        tree.column("# 6", anchor=CENTER)
        tree.heading("# 6", text="description")
        tree.column("# 7", anchor=CENTER)
        tree.heading("# 7", text="username")
        tree.column("# 8", anchor=CENTER)
        tree.heading("# 8", text="add date")
        tree.column("# 9", anchor=CENTER)
        tree.heading("# 9", text="vehicle color")
        tree.column("# 10", anchor=CENTER)
        tree.heading("# 10", text="vehicle type")
        tree.column("# 11", anchor=CENTER)
        tree.heading("# 11", text="vehicle detail")
        tree.column("# 12", anchor=CENTER)
        tree.heading("# 12", text="manufacture name")


        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8],row[9],row[10],row[11]))
        tree.pack()

        result = sql.SearchVehicle.viewOneSell(vin)
        didSold = False
        if(len(result)!= 0):
            didSold = True
        if(didSold):
            tree = ttk.Treeview(win, column=("vin", "soldPrice", "SoldDate"), show='headings', height=5)
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
            
            print(Cid)
            result = sql.SearchVehicle.searchIndividual(str(Cid))
            if(len(result) == 0):
                result = sql.SearchVehicle.searchBusiness(str(Cid))
            tree = ttk.Treeview(win, column=("Customer Name", "Phone Number", "Email"), show='headings', height=5)
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

            result = sql.SearchVehicle.searchIndividual(str(Cid))   
            if(len(result) == 0):
                result = sql.SearchVehicle.searchBusiness(str(Cid))
            tree = ttk.Treeview(win, column=("Customer Name", "Phone Number", "Email"), show='headings', height=5)
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


        win.mainloop()
   
    def jump_to_login_page(self):
        self.view_inventory.destroy()
        lg.LoginPage(self.window)