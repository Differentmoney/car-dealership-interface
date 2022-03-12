from tkinter import messagebox, ttk
import tkinter as tk
import add_repair_form as arf
import search_repair_form as srf
import select_menu as sm
import sql_pool as sp
from tkinter import *


class RepairformDetailPage(object):

    def __init__(self, window, role, repair):
        self.window = window
        self.window.config(bg = 'white')
        self.repairform_detail_page = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.repairform_detail_page.place(x = 0, y = 0)
        self.role = role
        self.repair = repair
        self.parts = []
        self.partList = []
        self.create_frame()


    def create_frame(self):
        tk.Label(self.repairform_detail_page, text = 'Repair Form Detail:').place(x = 400, y = 50)

        tk.Label(self.repairform_detail_page, text = 'Vin: ').place(x = 100, y = 100)
        tk.Label(self.repairform_detail_page, text=self.repair.vin).place(x=200, y=100)

        tk.Label(self.repairform_detail_page, text = 'CustomerID: ').place(x = 500, y = 100)
        tk.Label(self.repairform_detail_page, text=self.repair.customerID).place(x=600, y=100)
        
        tk.Label(self.repairform_detail_page, text = 'Start Date').place(x = 100, y = 150)
        tk.Label(self.repairform_detail_page, text=self.repair.startdate).place(x=200, y=150)

        tk.Label(self.repairform_detail_page, text = 'Odometer').place(x = 500, y = 150)
        tk.Label(self.repairform_detail_page, text=self.repair.odometer).place(x=600, y=150)

        tk.Label(self.repairform_detail_page, text = 'Labor Charge').place(x = 100, y = 200)
        self.laborcharge = tk.DoubleVar()
        self.laborcharge.set(self.repair.laborcharge)
        labor_charge_entry = tk.Entry(self.repairform_detail_page, textvariable = self.laborcharge)
        labor_charge_entry.place(x = 200, y = 200)

        tk.Label(self.repairform_detail_page, text = 'Description').place(x = 500, y = 200)
        tk.Label(self.repairform_detail_page, text=self.repair.description).place(x=600, y=200)

        btn_repair_history = tk.Button(self.repairform_detail_page, text='View Parts Added',
                                       command=lambda: RepairformDetailPage.viewPartsAdded(self))
        btn_repair_history.place(x=300, y=250)

        self.cor_x_next, self.cor_y_next = 50, 300

        if self.repair.completedate == 'None':
            if self.role != 'manager':
                self.btn_add_parts = tk.Button(self.repairform_detail_page, text = 'Add Parts', command = self.jump_to_add_repair_form)
                self.btn_add_parts = tk.Button(self.repairform_detail_page, text='add a new part', command=self.add_parts)
                self.btn_add_parts.place(x=100, y=250)

                self.btn_save_parts = tk.Button(self.repairform_detail_page, text = 'save part', command = self.save_parts)
                self.btn_save_parts.place(x = 100, y = 700)
                self.btn_save_parts['state'] = 'disabled'

                self.btn_update = tk.Button(self.repairform_detail_page, text = 'update', command = self.update_repair_form)
                self.btn_update.place(x = 250, y = 700)

                self.btn_complete = tk.Button(self.repairform_detail_page, text = 'complete', command = self.complete_repair_form)
                self.btn_complete.place(x = 400, y = 700)

        btn_jump_to_select_menu = tk.Button(self.repairform_detail_page, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 600, y = 700)
    
    def add_parts(self):
        tk.Label(self.repairform_detail_page, text = 'PartNumber').place(x = self.cor_x_next, y = self.cor_y_next)
        self.part_number = tk.StringVar()
        part_number_entry = tk.Entry(self.repairform_detail_page, textvariable = self.part_number, width = 5)
        part_number_entry.place(x = self.cor_x_next + 100, y = self.cor_y_next)
        tk.Label(self.repairform_detail_page, text = 'Quantity').place(x = self.cor_x_next + 200, y = self.cor_y_next)
        self.quantity = tk.IntVar()
        quantity_entry = tk.Entry(self.repairform_detail_page, textvariable = self.quantity, width = 5)
        quantity_entry.place(x = self.cor_x_next + 300, y = self.cor_y_next) 
        tk.Label(self.repairform_detail_page, text = 'Price').place(x = self.cor_x_next + 400, y = self.cor_y_next)
        self.price = tk.DoubleVar()
        price_entry = tk.Entry(self.repairform_detail_page, textvariable = self.price, width = 5)
        price_entry.place(x = self.cor_x_next + 450, y = self.cor_y_next) 
        tk.Label(self.repairform_detail_page, text = 'Vender Name').place(x = self.cor_x_next + 550, y = self.cor_y_next)
        self.vender_name = tk.StringVar()
        vender_name_entry = tk.Entry(self.repairform_detail_page, textvariable = self.vender_name, width = 5)
        vender_name_entry.place(x = self.cor_x_next + 650, y = self.cor_y_next)
        self.btn_add_parts['state'] = 'disabled'
        self.btn_save_parts['state'] = 'normal'
        self.btn_update['state'] = 'disabled'
        self.btn_complete['state'] = 'disabled'
        self.cor_x_next = self.cor_x_next
        self.cor_y_next = self.cor_y_next + 50

    
    def jump_to_add_repair_form(self):
        self.repairform_detail_page.destroy()
        arf.AddRepairForm(self.window, self.role)

    def update_repair_form(self):
        if self.laborcharge.get() < self.repair.laborcharge and self.role != "owner":
            messagebox.showerror("Errors", "The update to labor charges cannot be less than previous value", parent=self.window)
        else:
            sp.SearchRepair.updateLaborCharge(self.repair.vin, self.repair.customerID, self.repair.startdate, self.laborcharge.get())
            try:
                sp.SearchRepair.addNewParts(self.repair.vin, self.repair.customerID, self.repair.startdate, self.partList)
            except Exception:
                pass
            messagebox.showinfo("Succeed", "The repair is updated successfully", parent=self.window)
            self.repairform_detail_page.destroy()
            srf.SearchRepairForm(self.window, self.role)

    def complete_repair_form(self):
        if self.laborcharge.get() < self.repair.laborcharge:
            messagebox.showerror("Errors", "The update to labor charges cannot be less than previous value", parent=self.window)
        else:
            sp.SearchRepair.updateLaborCharge(self.repair.vin, self.repair.customerID, self.repair.startdate, self.laborcharge.get())
            try:
                sp.SearchRepair.addNewParts(self.repair.vin, self.repair.customerID, self.repair.startdate, self.partList)
            except Exception:
                pass
            sp.SearchRepair.completeRepair(self.repair.vin, self.repair.customerID, self.repair.startdate)
            messagebox.showinfo("Succeed", "The repair is completed successfully", parent=self.window)
            self.repairform_detail_page.destroy()
            srf.SearchRepairForm(self.window, self.role)

    def viewPartsAdded(self):
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("800x800")
        win.title("Parts Added")
        # Create an object of Style widget

        tree = ttk.Treeview(win, column=("PartNumber", "Quantity", "Price", "Vendor Name"), show='headings',height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="PartNumber")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Price")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Vendor Name")

        for i in range(len(self.repair.parts)):
            tree.insert("", "end", values=(self.repair.parts[i].partnumber, self.repair.parts[i].quantity,
                                           self.repair.parts[i].price, self.repair.parts[i].vendorname))
        tree.pack()
        win.mainloop()

    def save_parts(self):
        if (self.part_number.get() == 'None' or self.quantity.get() == 0 or self.price.get() == 0 or
                self.vender_name.get() == 'None'):
            messagebox.showerror("Errors", "Please check information entered, the input should not be empty", parent=self.window)
        else:
            self.parts = [self.part_number.get(), self.quantity.get(), self.price.get(), self.vender_name.get()]
            self.partList.append(self.parts)
            self.btn_add_parts['state'] = 'normal'
            self.btn_save_parts['state'] = 'disabled'
            self.btn_update['state'] = 'normal'
            self.btn_complete['state'] = 'normal'
        return self.partList
    
    def jump_to_select_menu(self):
        self.repairform_detail_page.destroy()
        sm.SelectMenu(self.window, self.role)