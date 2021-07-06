# Password_Generator_Main.py
# Description: The main python file to execute the password generator: file
# imports the GUI.py file and imports WX python

import GUI
import wx


if __name__ == '__main__':
    app = wx.App()
    window = GUI.Window(None, 'Password Generator')
    app.MainLoop()
