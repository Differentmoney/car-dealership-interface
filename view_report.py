import login_page as lg
import tkinter as tk
import select_menu as sm
import sql_pool as sql

from tkinter import *
from tkinter import ttk

class ViewReport(object):

    def __init__(self, window, role):
        self.window = window
        self.window.config(bg = 'green')
        self.view_report= tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.view_report.place(x = 0, y = 0)
        self.role = role
        self.search_by = tk.StringVar()
        self.search_by.set("Sales by Color")
        self.create_frame()

    def create_frame(self):
        tk.Label(self.view_report, text='View Report').place(x = 400, y = 50)
        tk.Label(self.view_report, text='generate report by:').place(x = 300, y = 200)

        drop_down_menu = tk.OptionMenu(self.view_report, self.search_by, 'Sales by Color','Sales by Type','Sales by Manufacturer','Gross Customer Income', 'Below Cost Sales','Average Time In Inventory','Part Statistics', 'Repairs by Manufacturer/Type/Model','Monthly Sales')
        drop_down_menu.place(x = 500, y = 200)

        btn_generate_report = tk.Button(self.view_report, text = "generate report", command = self.generate_report)
        btn_generate_report.place(x = 400, y = 500)

        btn_jump_to_select_menu = tk.Button(self.view_report, text = 'back to select menu', command = self.jump_to_select_menu)
        btn_jump_to_select_menu.place(x = 200, y = 700)

        btn_jump_to_login = tk.Button(self.view_report, text = 'back to login page', command = self.jump_to_login_page)
        btn_jump_to_login.place(x = 500, y = 700)
   
    def jump_to_login_page(self):
        self.view_report.destroy()
        lg.LoginPage(self.window)
    
    def jump_to_select_menu(self):
        self.view_report.destroy()
        sm.SelectMenu(self.window, self.role)
    
    def generate_report(self):
        type = self.search_by.get()
        if type == 'Sales by Color':
            ViewReport.color_report(self, self.search_by.get())
        elif type == 'Sales by Type':
            ViewReport.type_report(self, self.search_by.get())
        elif type == 'Sales by Manufacturer':
            ViewReport.manufacturer_report(self, self.search_by.get())
        elif type == 'Gross Customer Income':
            ViewReport.gross_customer_income_report(self, self.search_by.get())
        elif type == 'Repairs by Manufacturer/Type/Model':
            ViewReport.repairs_report(self, self.search_by.get())
        elif type == 'Below Cost Sales':
            ViewReport.below_cost_sales_report(self, self.search_by.get())
        elif type == 'Average Time In Inventory':
            ViewReport.average_time_in_inventory_report(self, self.search_by.get())
        elif type == 'Part Statistics':
            ViewReport.parts_statistics_report(self, self.search_by.get())
        elif type == 'Monthly Sales':
            ViewReport.monthly_sales_report(self, self.search_by.get())
        else:
            print('error')

    # Generate sales by color report
    def color_report(self, rt):
        result = sql.Report.sales_by_color()
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("Vehicle Color", "month", "year", "alltime"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Vehicle Color")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="month")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="year")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="alltime")     
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
        tree.pack()
        win.mainloop()

    # Generate sales by type report
    def type_report(self, rt):
        result = sql.Report.sales_by_type()
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vehicleType", "month", "year", "alltime"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vehicleType")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="month")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="year")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="alltime")     
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
        tree.pack()
        win.mainloop()

    # Generate sales by manufacturer report
    def manufacturer_report(self, rt):
        result = sql.Report.sales_by_manufacturer()
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("manufacturer", "month", "year", "alltime"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="manufacturer")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="month")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="year")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="alltime")     
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
        tree.pack()
        win.mainloop()

    # Gross Customer Income report
    def gross_customer_income_report(self, rt):
        result = sql.Report.gross_customer_income()
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')
        def jump_to_drilldown(a):
            curItem = tree.focus()
            CID = tree.item(curItem, 'values')[4]
            ViewReport.gross_drilldown(CID)
            #ViewReport.gross_drilldown2(CID)


        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("customer name", "gross", "oldest", "newest", "id"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="customer name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="gross")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="oldest")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="newest")     
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="id")
        tree.bind("<ButtonRelease-1>", jump_to_drilldown)
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
        tree.pack()

        win.mainloop()   

    # Gross Sales by Customer drill down report     
    def gross_drilldown(CID):
        result1 = sql.Report.gross_drill1(CID)
        result2 = sql.Report.gross_drill2(CID)
        win = Tk()
        
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title('Customer Vehicle Sales/Repair')
        tk.Label(win, text='Vehicle sales').place(x = 50, y = 60)
        tk.Label(win, text='Vehicle repairs').place(x = 50, y = 440)

        # Vehicle sales section
        tree1 = ttk.Treeview(win, column=("sold date", "sold price", "vin", "model year", "manufacturer name", "model", "customer name"), show='headings', height=10)
        tree1.column("# 1", anchor=CENTER)
        tree1.heading("# 1", text="sold date")
        tree1.column("# 2", anchor=CENTER)
        tree1.heading("# 2", text="sold price")
        tree1.column("# 3", anchor=CENTER)
        tree1.heading("# 3", text="vin")
        tree1.column("# 4", anchor=CENTER)
        tree1.heading("# 4", text="model year")
        tree1.column("# 5", anchor=CENTER)
        tree1.heading("# 5", text="manufacturer name")
        tree1.column("# 6", anchor=CENTER)
        tree1.heading("# 6", text="model")
        tree1.column("# 7", anchor=CENTER)
        tree1.heading("# 7", text="customer name")
        # Insert the data in Treeview widget
        for row in result1:
            tree1.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        tree1.pack(expand=1)

        # Repair section
        tree2 = ttk.Treeview(win, column=("start date", "end date", "vin", "odometer", "part cost", "labor cost", "total cost", "service writer"), show='headings', height=10)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="start date")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="end date")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="vin")
        tree2.column("# 4", anchor=CENTER)
        tree2.heading("# 4", text="odometer")
        tree2.column("# 5", anchor=CENTER)
        tree2.heading("# 5", text="part cost")
        tree2.column("# 6", anchor=CENTER)
        tree2.heading("# 6", text="labor cost")
        tree2.column("# 7", anchor=CENTER)
        tree2.heading("# 7", text="total cost")
        tree2.column("# 8", anchor=CENTER)
        tree2.heading("# 8", text="service writer")
        # Insert the data in Treeview widget
        for row in result2:
            tree2.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        tree2.pack(expand=1)


        win.mainloop()

    # Generate Below Cost Sales report
    def below_cost_sales_report(self, rt):
        result = sql.Report.below_cost_sales()
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vin", "sell date", "sold price", "invoice price", "ratio", "customer name", "salesperson"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vin")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="sold date")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="sold price")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="invoice price")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="ratio")
        tree.column("# 6", anchor=CENTER)
        tree.heading("# 6", text=" customer name")
        tree.column("# 7", anchor=CENTER)
        tree.heading("# 7", text="salesperson")
        # Insert the data in Treeview widget
        id = 0
        for row in result:
            index = str(id)
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),  tags=(index))
            if(row[4] <= 0.95):
                tree.tag_configure(index, background='red')
            id += 1
        tree.pack()
        win.mainloop()


    # Generate Average Time in Inventory Report
    def average_time_in_inventory_report(self, rt):
        result = sql.Report.avg_time_in_inventory()
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vehicle type", "average days in inventory"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vehicle type")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="average days in inventory")
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1]))
        tree.pack()
        win.mainloop()

    # Generate Parts Statistics
    def parts_statistics_report(self, rt):
        result = sql.Report.part_statistics()
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vendor's name", "number of parts", "total dollar amount spent"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vendor's name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="number of parts")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="total dollar amount spent")

        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2]))
        tree.pack()
        win.mainloop()

    # Generate Repair Report
    def repairs_report(self, rt):
        result = sql.Report.repair_by()
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')

        def jump_to_drilldown(e):
            curItem = tree.focus()
            manufacturer = tree.item(curItem, 'values')[0]
            self.repair_drill1(manufacturer)

        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("manufacturer name", "number of repairs", "sum part cost", "labor cost", "total cost"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="manufacturer name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="number of repairs")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="sum part cost")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="labor cost")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="total cost")
        tree.bind('<ButtonRelease-1>', jump_to_drilldown)

        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
        tree.pack()
        win.mainloop()

    # drill down for repair vehicle type
    def repair_drill1(self, m):
        result = sql.Report.repair_drill_1(m)
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title(m + " Vehicle Type")
        # Create an object of Style widget
        style = ttk.Style()
        def jump_to_drilldown(e):
            curItem = tree.focus()
            vt = tree.item(curItem, 'values')[0]
            self.repair_drill2(m, vt)
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("vehicletype", "repair count", "part cost", "labor cost", "total cost"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="vehicletype")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="repair count")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="part cost")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="labor cost")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="total cost")
        tree.bind('<ButtonRelease-1>', jump_to_drilldown)
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
        tree.pack()
        win.mainloop()

    # drill down for repair vehicle type
    def repair_drill2(self, m, vt):
        result = sql.Report.repair_drill_2(m, vt)
        win = Tk()
        # Set the size of the tkinter window
        win.geometry("700x500")
        win.title(m + " " + vt + " models")
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("Model", "repair count","part cost", "labor cost", "total cost"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Model")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="repair count")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="part cost")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="labor cost")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="total cost")
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
        tree.pack()
        win.mainloop()



    # Generate Monthly Sales Report
    def monthly_sales_report(self, rt):
        result = sql.Report.monthly_report()
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("700x500")
        win.title(rt)
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("year", "month", "vehicles sold", "total sales", "net sales", "ratio"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="year")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="month")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="vehicles sold")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="total sales")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="net sales")
        tree.column("# 6", anchor=CENTER)
        tree.heading("# 6", text="ratio")


        # Jump to drill down report
        def jump_to_drilldown(a):
            curItem = tree.focus()
            year = tree.item(curItem, 'values')[0]
            month = tree.item(curItem, 'values')[1]
            self.month_report(year, month)

        tree.bind('<ButtonRelease-1>', jump_to_drilldown)
        # Insert the data in Treeview widget
        id = 0
        for row in result:
            index = str(id)
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]), tags=(index))
            if (row[5] <= 1.1):
                tree.tag_configure(index, background='red')
            if(row[5] >= 1.25):
                tree.tag_configure(index, background='green')
            id += 1
        tree.pack()

        win.mainloop()

    # monthly sales drill down report
    def month_report(self, year, month):
        result = sql.Report.monthly_report_drilldown(year, month)
        win = Tk()
        # Set the size of the tkinter window    
        win.geometry("700x500")
        win.title("Monthly Sales Drilldown Report")
        # Create an object of Style widget
        style = ttk.Style()
        #style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("first name", "last name", "vehicles sold", "total sales"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="first name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="last name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="vehicles sold")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="total sold")

        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3] ))
        tree.pack()

        win.mainloop()


