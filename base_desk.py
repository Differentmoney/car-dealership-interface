import tkinter as tk
import login_page as lp

class BaseWindow(object):
    def __init__(self, window):
        self.window = window
        self.window.config()
        self.window.title('Jaunty Jalopies')
        self.window.geometry('800x800')
        lp.LoginPage(self.window)

if __name__ == '__main__':
    root = tk.Tk()
    bw = BaseWindow(root)
    bw.window.mainloop()