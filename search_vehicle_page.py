import sql_pool as sp
from sql_pool import SearchVehicle
import login_page as lg
import tkinter as tk
import entities.vehicle as ev
import tkinter.messagebox
import select_menu as sm
import vehicle_detail_page as vd

from tkinter import *
from tkinter import ttk

class SearchVehiclePage(object):

    def __init__(self, window, role = None, customer = None):
        self.window = window
        self.win2 = window
        self.window.config(bg = 'white')
        self.search_vehicle_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.search_vehicle_page.place(x = 0, y = 0)
        self.role = role
        self.customer = customer
        self.total_avail_num_vehicle = str(SearchVehicle.avaliable_car_num()) # need query from data base
        self.vin = tk.StringVar()
        self.vin.set('')
        self.vehicle_type = tk.StringVar()
        self.vehicle_type.set('')
        self.manufacturer = tk.StringVar()
        self.manufacturer.set('')
        self.model_year = tk.StringVar()
        self.model_year.set('')
        self.vehicle_color_op = tk.StringVar()
        self.vehicle_color_op.set('')
        self.vehicle_color = tk.StringVar()
        self.vehicle_color.set('')
        self.list_price_greater_than = tk.StringVar()
        self.list_price_greater_than.set('')
        self.list_price_less_than = tk.StringVar()
        self.list_price_less_than.set('')
        self.keywords = tk.StringVar()
        self.keywords.set('')
        self.criteria = tk.StringVar()
        self.create_frame()

    def create_frame(self):
        tk.Label(self.search_vehicle_page, text='Total number of available vehicles: ' + self.total_avail_num_vehicle).place(x = 300, y = 100)
        tk.Label(self.search_vehicle_page, text = 'Vehicle type:').place(x = 200, y = 200)
        tk.Label(self.search_vehicle_page, text = 'Manufacturer:').place(x = 200, y = 250)
        tk.Label(self.search_vehicle_page, text = 'Model year:').place(x = 200, y = 300)
        tk.Label(self.search_vehicle_page, text = 'Color:').place(x = 200, y = 350)
        tk.Label(self.search_vehicle_page, text = 'List price greater than').place(x = 200, y = 400)
        tk.Label(self.search_vehicle_page, text = 'List price less than').place(x = 200, y = 450)
        tk.Label(self.search_vehicle_page, text = 'Keywords').place(x = 200, y = 500)

        if lg.LoginPage.userID != "":
            tk.Label(self.search_vehicle_page, text='Vin:').place(x = 200, y = 150)
            tk.Entry(self.search_vehicle_page, textvariable=self.vin).place(x=500, y=150)

        drop_down_menu_vehicletype = tk.OptionMenu(self.search_vehicle_page, self.vehicle_type, *self.generate_vehicle_type_list())
        drop_down_menu_vehicletype.place(x=500, y=200)

        drop_down_menu_manufacturer = tk.OptionMenu(self.search_vehicle_page, self.manufacturer, *self.generate_manufacturer_list())
        drop_down_menu_manufacturer.place(x = 500, y = 250)
        
        if(self.role == "manager" or self.role  == "owner"):
            tk.Label(self.search_vehicle_page, text = 'Vehicle Search Criteria').place(x = 200, y = 550)
            drop_down_menu_vehicletype = tk.OptionMenu(self.search_vehicle_page, self.criteria, *["sold vehicles","unsold vehicles","all vehicles"])
            drop_down_menu_vehicletype.place(x=400, y=550)
        self.criteria.set("unsold vehicles")
        
        tk.Entry(self.search_vehicle_page, textvariable = self.model_year).place(x = 500, y = 300)
        
        drop_down_menu_color = tk.OptionMenu(self.search_vehicle_page, self.vehicle_color_op, *self.generate_color_list())
        drop_down_menu_color.place(x = 300, y = 350)        
        btn_add_color = tk.Button(self.search_vehicle_page, text = 'add', command = self.add_color)
        btn_add_color.place(x = 400, y = 350)
        tk.Entry(self.search_vehicle_page, textvariable = self.vehicle_color).place(x = 500, y = 350)



        tk.Entry(self.search_vehicle_page, textvariable = self.list_price_greater_than).place(x = 500, y = 400)
        tk.Entry(self.search_vehicle_page, textvariable = self.list_price_less_than).place(x = 500, y = 450)
        tk.Entry(self.search_vehicle_page, textvariable = self.keywords).place(x = 500, y = 500)

        btn_jump_to_search_result = tk.Button(self.search_vehicle_page, text = 'Search', command = self.jump_to_search_vehicle_result)
        btn_jump_to_search_result.place(x = 200, y = 700)

        btn_jump_to_login = tk.Button(self.search_vehicle_page, text = 'back to login page', command = self.jump_to_login_page)
        btn_jump_to_login.place(x = 600, y = 700)
   
        if self.role:
            btn_jump_to_select_menu = tk.Button(self.search_vehicle_page, text = 'back to select menu', command = self.jump_to_select_menu)
            btn_jump_to_select_menu.place(x = 400, y = 700)

    def jump_to_login_page(self):
        lg.LoginPage.setUserID()
        self.search_vehicle_page.destroy()
        lg.LoginPage(self.window)
    
    # pop up button
    def jump_login(self):
        if self.win2 != None:
            self.win2.destroy()
        lg.LoginPage.setUserID()
        self.search_vehicle_page.destroy()
        lg.LoginPage(self.window)

    def jump_to_search_vehicle(self):
        if self.win2 != None:
            self.win2.destroy()
        self.search_vehicle_page.destroy()
        SearchVehiclePage(self.window, self.role, self.customer)
    
    def jump_to_select_menu(self):
        self.search_vehicle_page.destroy()
        sm.SelectMenu(self.window, self.role)

    # pop up button
    def jump_select_menu(self):
        self.search_vehicle_page.destroy()
        if self.win2 != None:
            self.win2.destroy()
        sm.SelectMenu(self.window, self.role)

    def jump_to_search_vehicle_result(self):
        # mock data, need actually implementation with databse
        cars = self.__find_cars()
        if cars:
            # self.search_vehicle_page.destroy()
            self.vehicle_list(cars)

    # all logic need rewrite
    def __find_cars(self):
        print("type: " + self.vehicle_type.get().strip() + "\n")
        ans = SearchVehicle.search(self.criteria.get().strip(),self.vin.get().strip(),self.vehicle_type.get().strip(),self.manufacturer.get().strip(),self.model_year.get().strip(),self.vehicle_color.get().strip(),self.list_price_greater_than.get().strip(),self.list_price_less_than.get().strip(),self.keywords.get().strip())

        if(len(ans) == 0):
            tkinter.messagebox.showinfo(title = 'message', message = 'Sorry, it looks like we don’t have that in stock!')
            return None
        else:
            car_list = []
            for each in ans:
                car_list.append(ev.Vehicle(vin = each[0],
                        model = each[1],
                        model_year = each[2],
                        color = each[6],
                        list_price = each[3],
                        invoice_price= each[4],
                        description = each[5],
                        type = each[7],
                        detail = each[8],
                        manufacturerName = each[9]))
            return car_list

    # Show list of vehicles
    def vehicle_list(self, result):
        win = Tk()
        self.win2 = win
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title("Vehicle List")
        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')
        
        def jump_to_drilldown(a):
            curItem = tree.focus()
            vin = tree.item(curItem, 'values')[0]
            ans = SearchVehicle.search(self.criteria.get().strip(),vin, "", "", "", "", "", "", "")
            for each in ans:
                vehicle = ev.Vehicle(vin = each[0],
                            model = each[1],
                            model_year = each[2],
                            color = each[6],
                            list_price = each[3],
                            invoice_price= each[4],
                            description = each[5],
                            type = each[7],
                            detail = each[8],
                        manufacturerName = each[9], 
                        adddate = each[10])
            self.win2.destroy()
            self.search_vehicle_page.destroy()
            vd.VehicleDetailPage(self.window, vehicle, self.role, self.customer)  

        btn_jump_to_search_result = tk.Button(win, text = 'Search page', command = self.jump_to_search_vehicle)
        btn_jump_to_search_result.place(x = 200, y = 700)

        btn_jump_to_login = tk.Button(win, text = 'back to login page', command = self.jump_login)
        btn_jump_to_login.place(x = 600, y = 700)

        if self.role:
            btn_jump_to_select_menu = tk.Button(win, text = 'back to select menu', command = self.jump_select_menu)
            btn_jump_to_select_menu.place(x = 400, y = 700)
    

        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vin", "model", "model year", "list price"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vin")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="model")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="model year")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="list price")
        tree.bind("<ButtonRelease-1>", jump_to_drilldown)
        # Insert the data in Treeview widget
        for Vehicle in result:
            tree.insert("", "end", values=(Vehicle.vin, Vehicle.model, Vehicle.model_year, Vehicle.list_price))
        tree.pack()

        win.mainloop()   


    def generate_vehicle_type_list(self):
        return ['car', 'suv', 'convertible', 'van', 'truck']

    def generate_color_list(self):
        return sp.AddVehicle.retrieveColor()

    def generate_manufacturer_list(self):
        return sp.AddVehicle.retrieveManufacturer()

    def add_color(self):
        if self.vehicle_color.get():
            self.vehicle_color.set(self.vehicle_color.get() + ' , ' + self.vehicle_color_op.get())
        elif self.vehicle_color_op.get():
            self.vehicle_color.set(self.vehicle_color_op.get())