import tkinter.messagebox

class Utilities:
    @staticmethod
    def check_role(role):
        if (role == 'inventory_clerk'):
            print("this is a Inventory Clerk")
            return "clerk"
        elif (role == 'sales_person'):
            print("this is a Salesperson")
            return "salespeople"
        elif (role == 'service_writer'):
            print("this is a Service Writer")
            return "servicewriter"
        elif (role == 'manager'):
            print("This is a Manager")
            return "manager"
        elif (role == 'owner'):
            print("This is the Owner")
            return "owner"
        else:
            tkinter.messagebox.showinfo(title = 'message', message = 'invalid username or password')
            return "unknown user"

class DatabaseOp:
    def __init__(self):
        pass
    def addVehicleToVehicleTable(self):
        pass