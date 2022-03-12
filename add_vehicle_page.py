from datetime import date
from tkinter import messagebox
import login_page as lg
import tkinter as tk
import entities.vehicle as ev
import vehicle_detail_page as vdp
import select_menu as sm
import sql_pool as sp


class AddVehiclePage(object):

    def __init__(self, window, role):
        self.window = window
        self.window.config(bg = 'white')
        self.add_vehicle_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.add_vehicle_page.place(x = 0, y = 0)
        self.role = role
        self.vin = tk.StringVar()
        self.model = tk.StringVar()
        self.model_year = tk.StringVar()
        self.invoice_price = tk.StringVar()
        self.description = tk.StringVar()
        self.vehicle_type = tk.StringVar()
        self.type_detail = tk.StringVar()
        self.manufacturer = tk.StringVar()
        self.vehicle_color_op = tk.StringVar()
        self.vehicle_color = tk.StringVar()
        self.Rooftype = tk.StringVar()
        self.Backseatcount = tk.StringVar()
        self.Cargocapacity = tk.StringVar()
        self.Cargocovertype = tk.StringVar()
        self.Numberofrearaxles = tk.StringVar()
        self.hasdriversidebackdoor = tk.StringVar()
        self.Drivertraintype = tk.StringVar()
        self.Numberofcupholders = tk.StringVar()
        self.Numberofdoors = tk.StringVar()
        self.colorList = []
        self.create_frame()

    def create_frame(self):
        tk.Label(self.add_vehicle_page, text='Add vehicles:').place(x = 400, y = 50)

        tk.Label(self.add_vehicle_page, text = 'VIN:').place(x = 200, y = 100)
        tk.Label(self.add_vehicle_page, text = 'Model:').place(x = 200, y = 150)
        tk.Label(self.add_vehicle_page, text = 'Model year:').place(x = 200, y = 200)
        tk.Label(self.add_vehicle_page, text = 'Invoice price:').place(x = 200, y = 250)
        tk.Label(self.add_vehicle_page, text = 'Description').place(x = 200, y = 300)
        tk.Label(self.add_vehicle_page, text = 'Vehicle type:').place(x = 200, y = 350)
        tk.Label(self.add_vehicle_page, text = 'Type detail:').place(x=200, y=400)
        tk.Label(self.add_vehicle_page, text = 'Manufacturer:').place(x = 200, y = 450)
        tk.Label(self.add_vehicle_page, text = 'Color:').place(x = 200, y = 500)

        tk.Entry(self.add_vehicle_page, textvariable = self.vin).place(x = 500, y = 100)
        tk.Entry(self.add_vehicle_page, textvariable = self.model).place(x = 500, y = 150)
        tk.Entry(self.add_vehicle_page, textvariable = self.model_year).place(x = 500, y = 200)
        tk.Entry(self.add_vehicle_page, textvariable = self.invoice_price).place(x = 500, y = 250)
        tk.Entry(self.add_vehicle_page, textvariable = self.description).place(x = 500, y = 300)

        drop_down_menu_vehicletype = tk.OptionMenu(self.add_vehicle_page, self.vehicle_type, *self.generate_vehicle_type_list(), command=self.vehicle_type_detail)
        drop_down_menu_vehicletype.place(x=500, y=350)

        drop_down_menu_manufacturer = tk.OptionMenu(self.add_vehicle_page, self.manufacturer, *self.generate_manufacturer_list())
        drop_down_menu_manufacturer.place(x = 500, y = 450)

        drop_down_menu_color = tk.OptionMenu(self.add_vehicle_page, self.vehicle_color_op, *self.generate_color_list())
        drop_down_menu_color.place(x = 300, y = 500)
        
        btn_add_color = tk.Button(self.add_vehicle_page, text = 'add', command = self.add_color)
        btn_add_color.place(x = 400, y = 500)
        tk.Entry(self.add_vehicle_page, textvariable = self.vehicle_color).place(x = 500, y = 500)

        btn_add_vehicle = tk.Button(self.add_vehicle_page, text = 'Add', command = self.add_vehicle_and_jump_to_vehicle_detail)
        btn_add_vehicle.place(x = 300, y = 700)
        btn_jump_to_select_menu = tk.Button(self.add_vehicle_page, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 500, y = 700)

    def jump_to_select_menu(self):
        self.add_vehicle_page.destroy()
        sm.SelectMenu(self.window, self.role)

    def add_vehicle_and_jump_to_vehicle_detail(self):
        if (self.vin.get() == "" or self.model.get() == "" or self.model_year.get() == "" or
                self.invoice_price.get() == "" or self.manufacturer.get() == "" or
                self.vehicle_type.get() == "" or self.vehicle_color.get() == ""):
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        elif not AddVehiclePage.validateInput(self):
            messagebox.showerror("Error!", "Plese validate the input of Model Year and Invoice price", parent=self.window)
        elif not AddVehiclePage.validateVehicleTypeDetail(self):
            messagebox.showerror("Error!", "Please check vehicle type detail input", parent=self.window)
        elif sp.AddVehicle.checkVin(self.vin.get()):
            messagebox.showerror("Error!", "Vehicle exists", parent=self.window)
        else:
            vehicle = ev.Vehicle(self.vin.get(),
                                 self.model.get(),
                                 self.model_year.get(),
                                 self.vehicle_color.get(),
                                 self.invoice_price.get(),
                                 str(float(self.invoice_price.get()) * 1.25),
                                 self.description.get(),
                                 self.vehicle_type.get(),
                                 self.type_detail.get(),
                                 self.manufacturer.get(),
                                 date.today())
            manufacturerID = sp.AddVehicle.getManufacturerID(self.manufacturer.get())
            sp.AddVehicle.addVehicleType(self.vehicle_type.get(), self.type_detail.get())
            sp.AddVehicle.addVehicle(self.vin.get(), self.model.get(), self.model_year.get(), self.invoice_price.get(),
                                     self.description.get(), lg.LoginPage.userID, manufacturerID, date.today())
            sp.AddVehicle.addVehicleColorList(self.vin.get(), self.colorList)
            self.add_vehicle_page.destroy()
            vdp.VehicleDetailPage(self.window, vehicle, self.role)

    def generate_color_list(self):
        return sp.AddVehicle.retrieveColor()
    
    def generate_manufacturer_list(self):
        return sp.AddVehicle.retrieveManufacturer()

    def generate_vehicle_type_list(self):
        return ['Car', 'SUV', 'Convertible', 'Van', 'Truck']
    
    def add_color(self):
        if self.vehicle_color_op.get() == "":
            messagebox.showerror("Error!", "Please select a color", parent=self.window)
        elif len(self.colorList) == 0 and self.vehicle_color_op.get() != "":
            self.colorList.append(self.vehicle_color_op.get())
            self.vehicle_color.set(self.colorList[0])
        elif AddVehiclePage.checkDuplicateColor(self):
            messagebox.showerror("Error!", "Duplicate colors selected for a vehicle", parent=self.window)
        else:
            self.colorList.append(self.vehicle_color_op.get())
            self.vehicle_color.set(AddVehiclePage.colorString(self))

    def checkDuplicateColor(self):
        for i in range(len(self.colorList)):
            if self.colorList[i] == self.vehicle_color_op.get():
                return True
        return False

    def colorString(self):
        colorString = ""
        for i in range(len(self.colorList)):
            colorString = self.colorList[i] + "; " + colorString
        return colorString

    def vehicle_type_detail(self, event):
        if self.vehicle_type.get() == 'Car':
            tk.Label(self.add_vehicle_page, bg="green", width=600).place(x=300, y=400)
            tk.Label(self.add_vehicle_page, text='Number of doors:').place(x=300, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Numberofdoors, width=5).place(x=500, y=400)
        elif self.vehicle_type.get() == 'Convertible':
            tk.Label(self.add_vehicle_page, bg="green", width=600).place(x=300, y=400)
            tk.Label(self.add_vehicle_page, text='Roof type:').place(x=300, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Rooftype, width=5).place(x=400, y=400)
            tk.Label(self.add_vehicle_page, text='Back seat count:').place(x=450, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Backseatcount, width=5).place(x=550, y=400)
        elif self.vehicle_type.get() == 'Truck':
            tk.Label(self.add_vehicle_page, bg="green", width=600).place(x=300, y=400)
            tk.Label(self.add_vehicle_page, text='Cargo capacity:').place(x=300, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Cargocapacity, width=5).place(x=400, y=400)
            tk.Label(self.add_vehicle_page, text='Cargo cover type:').place(x=450, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Cargocovertype, width=5).place(x=550, y=400)
            tk.Label(self.add_vehicle_page, text='Number of rear axles:').place(x=600, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Numberofrearaxles, width=5).place(x=750, y=400)
        elif self.vehicle_type.get() == 'Van':
            tk.Label(self.add_vehicle_page, bg="green", width=600).place(x=300, y=400)
            tk.Label(self.add_vehicle_page, text='has driver\' side back door:').place(x=300, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.hasdriversidebackdoor, width=5).place(x=500, y=400)
        elif self.vehicle_type.get() == 'SUV':
            tk.Label(self.add_vehicle_page, bg="green", width=600).place(x=300, y=400)
            tk.Label(self.add_vehicle_page, text='Drivertrain type:').place(x=300, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Drivertraintype, width=5).place(x=400, y=400)
            tk.Label(self.add_vehicle_page, text='Number of cupholders:').place(x=450, y=400)
            tk.Entry(self.add_vehicle_page, textvariable=self.Numberofcupholders, width=5).place(x=600, y=400)

    def validateInput(self):
        try:
            if int(self.model_year.get()) >= 1000 and int(self.model_year.get()) <= 2022 and float(self.invoice_price.get()) > 0:
                return True
        except Exception:
            return False

    def validateVehicleTypeDetail(self):
        if self.vehicle_type.get() == 'Car':
            try:
                if int(self.Numberofdoors.get()) > 0:
                    self.type_detail.set(self.Numberofdoors.get())
            except Exception:
                pass
        if self.vehicle_type.get() == 'SUV':
            try:
                if int(self.Numberofcupholders.get()) > 0:
                    self.type_detail.set(self.Drivertraintype.get() + "," + self.Numberofcupholders.get())
            except Exception:
                pass
        if self.vehicle_type.get() == 'Convertible':
            try:
                if int(self.Backseatcount.get()) > 0:
                    self.type_detail.set(self.Rooftype.get() + "," + self.Backseatcount.get())
            except Exception:
                pass
        if self.vehicle_type.get() == 'Van':
            self.type_detail.set(self.hasdriversidebackdoor.get())
        if self.vehicle_type.get() == 'Truck':
            try:
                if int(self.Cargocapacity.get()) > 0 and int(self.Numberofrearaxles.get()) > 0:
                    str = ""
                    str += self.Cargocapacity.get() + "," + self.Numberofrearaxles.get()
                    if(len(self.Cargocovertype.get()) != 0 ):
                        str +=  "," + self.Cargocovertype.get()
                    self.type_detail.set(str)
            except Exception:
                pass
        if self.type_detail.get() == "":
            return False
        else:
            return True
