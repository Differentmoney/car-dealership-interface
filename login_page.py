import search_vehicle_page as svp
import select_menu as sm
import tkinter as tk
import utilities as ut
import sql_pool as sql

class LoginPage(object):
    userID = ""
    def __init__(self, window):
        self.window = window
        self.window.config(bg='white')
        self.login_page = tk.Frame(self.window, bg = 'white', height = 400, width = 400)
        self.login_page.place(x = 300, y = 200)
        self.user_name = tk.StringVar()
        self.user_password = tk.StringVar()

        self.user_name.set('roland')
        self.user_password.set('roland')

        tk.Label(self.login_page, text='User name: ').place(x = 0, y = 0)
        user_name_entry = tk.Entry(self.login_page, textvariable = self.user_name)
        user_name_entry.place(x = 100, y = 0)        
        tk.Label(self.login_page, text = 'Password: ').place(x = 0, y = 50)
        user_pwd_entry = tk.Entry(self.login_page, textvariable = self.user_password)
        user_pwd_entry.place(x = 100, y = 50)


        btn_log_in = tk.Button(self.login_page, text='Log In', command = self.jump_to_select_menu)
        btn_log_in.place(x = 150, y = 150)

        btn_search_vehicle = tk.Button(self.login_page, text = 'Search Vehicle', command = self.jump_to_search_vehicle_page)
        btn_search_vehicle.place(x = 0, y = 150)
    
    def jump_to_select_menu(self):
        # Set current user's Username 
        LoginPage.userID = self.user_name.get()
        # Verify user name and password then retrieves role
        login = sql.login.validation(self.user_name.get(), self.user_password.get())
        user_role = ut.Utilities.check_role(login)
        # output current user name and role
        if user_role == 'unknown user':
            return
        # Check if user is valid 
        for role in ['clerk','salespeople','servicewriter','manager','owner']:
            if (user_role == role):
                self.login_page.destroy()
                sm.SelectMenu(self.window, user_role)
                return


    def jump_to_search_vehicle_page(self):
        self.login_page.destroy()
        svp.SearchVehiclePage(self.window)

    @staticmethod
    def setUserID():
        LoginPage.userID = ""


    




