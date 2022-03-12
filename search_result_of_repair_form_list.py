from tkinter import messagebox, ttk
import tkinter as tk
import repairform_detail_page as rdp
import add_repair_form as arf
import select_menu as sm
from tkinter import *


class SearchResultOfRepairFormList(object):

    def __init__(self, window, role, complete_repair_form, on_going_repair_form, vehicle):
        self.window = window
        self.window.config(bg = 'white')
        self.search_result_of_repair_form_list = tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.search_result_of_repair_form_list.place(x = 0, y = 0)
        self.role = role
        self.vehicle = vehicle
        self.complete_repair_form = complete_repair_form
        self.on_going_repair_form = on_going_repair_form
        self.create_frame()


    # TODO: need redesign this function
    def __concatenate_repair_form_info(self, repair_form):
        return (" vin: " + repair_form.vin + " customer: " + str(repair_form.customerID) + " start date: " +
                repair_form.startdate + " complete date: " + repair_form.completedate)

    def create_frame(self):
        tk.Label(self.search_result_of_repair_form_list, text='Vehicle Detail:').place(x=400, y=50)

        tk.Label(self.search_result_of_repair_form_list, text='VIN: ' + self.vehicle.vin).place(x=200, y=100)
        tk.Label(self.search_result_of_repair_form_list, text='Model Name: ' + self.vehicle.model).place(x=600, y=100)
        tk.Label(self.search_result_of_repair_form_list, text='Model year: ' + str(self.vehicle.model_year)).place(x=200, y=150)
        tk.Label(self.search_result_of_repair_form_list, text='Color: ' + self.vehicle.color).place(x=600, y=150)
        tk.Label(self.search_result_of_repair_form_list, text='Vehicle Type: ' + self.vehicle.type).place(x=600, y=200)
        tk.Label(self.search_result_of_repair_form_list, text='Manufacturer: ' + self.vehicle.manufacturerName).place(x=200, y=200)
        tk.Label(self.search_result_of_repair_form_list, text='Repair List:').place(x = 400, y = 250)

        if len(self.on_going_repair_form) > 0:
            repair_info = self.__concatenate_repair_form_info(self.on_going_repair_form[0])
            btn_ongoing_info = tk.Button(self.search_result_of_repair_form_list, text = repair_info, command = self.jump_to_on_going_repair_form_detail)
            btn_ongoing_info.place(x = 200, y = 300)
        else:
            tk.Label(self.search_result_of_repair_form_list, text='No open repair exists, Please create a new one!').place(x=200, y=300)

        if self.role in ['servicewriter', 'owner']:
            btn_add_repair_form = tk.Button(self.search_result_of_repair_form_list, text = 'add repair', command = self.jump_to_add_repair_form_page)
            btn_add_repair_form.place(x = 300, y = 700)

        btn_jump_to_select_menu = tk.Button(self.search_result_of_repair_form_list, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 500, y = 700)

        if len(self.complete_repair_form) > 0:
            btn_repair_history = tk.Button(self.search_result_of_repair_form_list, text='Repair History',
                                           command=lambda: SearchResultOfRepairFormList.historicalRepair(self))
            btn_repair_history.place(x=200, y=350)
            # SearchResultOfRepairFormList.historicalRepair(self)

    def historicalRepair(self):
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title("Historical Repair")
        # Create an object of Style widget
        style = ttk.Style()

        # style.theme_use('clam')

        def onDoubleClick(e):
            item = tree.selection()[0]
            SearchResultOfRepairFormList.historicalRepairDetail(self, int(item[1:])-1)

        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("Vin", "CustomerID", "Start Date", "Completed Date"), show='headings',height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Vin")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="CustomerID")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Start Date")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Completed Date")
        tree.bind("<Double-1>", onDoubleClick)

        # Insert the data in Treeview widget
        for i in range(len(self.complete_repair_form)):
            tree.insert("", "end", values=(self.complete_repair_form[i].vin, self.complete_repair_form[i].customerID,
                                           self.complete_repair_form[i].startdate,
                                           self.complete_repair_form[i].completedate))
        tree.pack()
        win.mainloop()

    def historicalRepairDetail(self, item):
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title("Historical Repair Detail")
        # Create an object of Style widget
        style = ttk.Style()

        tree = ttk.Treeview(win, column=("Repair Items", "Details"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Repair Items")
        tree.column("# 2", anchor=CENTER, )
        tree.heading("# 2", text="Details")

        tree.insert("", "end", values=("Vin", self.complete_repair_form[item].vin))
        tree.insert("", "end", values=("CustomerID", self.complete_repair_form[item].customerID))
        tree.insert("", "end", values=("Start Date", self.complete_repair_form[item].startdate))
        tree.insert("", "end", values=("Odometer", self.complete_repair_form[item].odometer))
        tree.insert("", "end", values=("Labor Charge", self.complete_repair_form[item].laborcharge))
        tree.insert("", "end", values=("Description", self.complete_repair_form[item].description))
        tree.insert("", "end", values=("Completed Date", self.complete_repair_form[item].completedate))
        tree.pack()

        # # Add a Treeview widget
        tree1 = ttk.Treeview(win, column=("Part Number", "Quantity", "Price", "Vendor Name"), show='headings', height=10)
        tree1.column("# 1", anchor=CENTER)
        tree1.heading("# 1", text="Part Number")
        tree1.column("# 2", anchor=CENTER)
        tree1.heading("# 2", text="Quantity")
        tree1.column("# 3", anchor=CENTER)
        tree1.heading("# 3", text="Price")
        tree1.column("# 4", anchor=CENTER)
        tree1.heading("# 4", text="Vendor Name")

        # # Insert the data in Treeview widget
        for i in range(len(self.complete_repair_form[item].parts)):
            tree1.insert("", "end", values=(self.complete_repair_form[item].parts[i].partnumber,
                                           self.complete_repair_form[item].parts[i].quantity,
                                           self.complete_repair_form[item].parts[i].price,
                                           self.complete_repair_form[item].parts[i].vendorname))
        tree1.pack()
        win.mainloop()

    def jump_to_repair_form_detail(self, index):
        self.search_result_of_repair_form_list.destroy()
        rdp.RepairformDetailPage(self.window, self.role, self.complete_repair_form[index])

    def jump_to_on_going_repair_form_detail(self):
        self.search_result_of_repair_form_list.destroy()
        rdp.RepairformDetailPage(self.window, self.role, self.on_going_repair_form[0])

    def jump_to_add_repair_form_page(self):
        if self.on_going_repair_form:
            messagebox.showerror("Error!", "An open repair exists, please close it first", parent=self.window)
        else:
            self.search_result_of_repair_form_list.destroy()
            arf.AddRepairForm(self.window, self.role, None, None, self.vehicle.vin)
    
    def jump_to_select_menu(self):
        self.search_result_of_repair_form_list.destroy()
        sm.SelectMenu(self.window, self.role)