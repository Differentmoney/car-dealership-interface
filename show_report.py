from tkinter import *
from tkinter import ttk
import tkinter as tk
import login_page as lg
import sql_pool as sql

class ShowReport(object):

    def __init__(self, window, report_type, role):
        self.window = window
        self.window.config(bg = 'green')
        self.show_report= tk.Frame(self.window, bg = 'green', height = 800, width = 800)
        self.show_report.place(x = 0, y = 0)
        self.role = role
        self.rt = report_type
        self.search_by = tk.StringVar()
        self.search_by.set("Color")
        self.create_frame()

    def create_frame(self):
        #tk.Label(self.show_report, text= self.rt).place(x = 400, y = 50)

        result = sql.Report.sales_by_color()

        win = Tk()
        # Set the size of the tkinter window
        win.geometry("800x800")
        win.title(self.rt)

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("color", "month", "year", "alltime"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="color")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="month")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="year")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="alltime")
        
        # Insert the data in Treeview widget
        for row in result:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))


        tree.pack()

        win.mainloop()


  

    