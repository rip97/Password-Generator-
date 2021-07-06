# Description: The GUI.py file create the user interface of the password generator process.
# This file imports the wx class along with the Generator_Class to generate the password

import wx
import Generator_Class


class Window (wx.Frame):

    # global object and variables
    __generator = Generator_Class.PasswordGenerator()
    __userSelection = ['']*3

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1206,550))
        self.SetBackgroundColour(wx.Colour(0,80,100))

        img = wx.Image('key.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, img, pos=(0,0))


        messageTitle = wx.StaticText(self, pos=(400,268), size=(200,20), label="PASSWORD GENERATOR")
        font = wx.Font(18, wx.DEFAULT, wx.SLANT, wx.BOLD)
        messageTitle.SetFont(font)
        messageTitle.SetForegroundColour(wx.Colour(0, 80, 100))
        messageTitle.SetBackgroundColour(wx.Colour(255,255,255))

        userInstructs = 'Instructions:\n'\
                        'This password generator uses a selection of three words from categories\n'\
                        'to form a password. A three digit number will also be placed at the end of\n'\
                        'your password.\n'\
                        'To form a password, do the following:\n'\
                        'Step 1: Select a category from the first drop down menu.\n'\
                        'Step 2: Select a category from the second drop down menu.\n'\
                        'Step 3: Select a category from the third drop down menu.\n'\
                        'Step 4: Press "Generate Password" button.'

        instructions = wx.StaticText(self, pos=(0,300), size=(500,200),label=userInstructs)
        font2 = wx.Font(14, wx.DEFAULT,wx.NORMAL,wx.NORMAL)
        instructions.SetFont(font2)
        instructions.SetBackgroundColour(wx.Colour(255,255,255))

        title1 = wx.StaticText(self, pos=(640,315), size=(120,20), label="Selection One")
        tile1Font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title1.SetFont(tile1Font)
        title1.SetBackgroundColour(wx.Colour(255,255,255))
        title1.SetForegroundColour(wx.Colour(0, 80, 100))

        title2 = wx.StaticText(self, pos=(830, 315), size=(120, 20), label="Selection Two")
        tile2Font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title2.SetFont(tile2Font)
        title2.SetBackgroundColour(wx.Colour(255, 255, 255))
        title2.SetForegroundColour(wx.Colour(0, 80, 100))

        title3 = wx.StaticText(self, pos=(1030, 315), size=(135, 20), label="Selection Three")
        tile3Font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title3.SetFont(tile3Font)
        title3.SetBackgroundColour(wx.Colour(255, 255, 255))
        title3.SetForegroundColour(wx.Colour(0, 80, 100))

        self.__choice1 = wx.Choice(self, pos=(640,340), size=(120, 100), choices=self.__generator.GetKeys())
        self.__choice2 = wx.Choice(self, pos=(830,340), size=(120,100), choices=self.__generator.GetKeys())
        self.__choice3 = wx.Choice(self, pos=(1030, 340), size=(135,100), choices=self.__generator.GetKeys())

        self.__choice1.Bind(wx.EVT_CHOICE, self.selectChoice1)
        self.__choice2.Bind(wx.EVT_CHOICE, self.selectChoice2)
        self.__choice3.Bind(wx.EVT_CHOICE, self.selectChoice3)

        generateBttn = wx.Button(self, pos=(620,470), size=(120,30), label="Generate Password")
        generateBttn.Bind(wx.EVT_BUTTON, self.generate)

        exitButton = wx.Button(self, pos=(1090,470), size=(100,30), label="Exit")
        exitButton.Bind(wx.EVT_BUTTON, self.exit)

        self.Center()
        self.Show()

    # functions to get input from selection boxes and set the categories of the
    # the generator class. Sections must first be passed into a global list
    def selectChoice1(self, event):
        _selection = self.__choice1.GetStringSelection()
        self.__userSelection[0] = _selection

    def selectChoice2(self, event):
        _selection = self.__choice2.GetStringSelection()
        self.__userSelection[1] = _selection

    def selectChoice3(self, event):
        _selection = self.__choice3.GetStringSelection()
        self.__userSelection[2] = _selection

    # button event to validate users sections and create the password
    def generate(self, event):
        self.__generator.SetCategories(self.__userSelection)
        self.__userSelection.clear()
        self.__userSelection = [''] * 3

        # validate users input in order to create password
        _valid = self.__generator.validateInput()
        if _valid == False:
            wx.MessageBox('Invalid Input: Please Select the correct categories before\n'
                        'clicking "Generate"!', "Warning", wx.OK | wx.ICON_ERROR)
            self.__choice1.SetSelection(-1)
            self.__choice2.SetSelection(-1)
            self.__choice3.SetSelection(-1)
        else:
            __passwd = self.__generator.generatePasswd()
            wx.MessageBox('Password Generated\nYour password is:\n'+ __passwd, 'Password Information',
                          wx.OK | wx.ICON_INFORMATION)
            self.__choice1.SetSelection(-1)
            self.__choice2.SetSelection(-1)
            self.__choice3.SetSelection(-1)

    # close button event
    def exit(self, event):
        answer = wx.MessageBox("Do you wish to close the application?", "Close Confirm", wx.YES_NO | wx.ICON_QUESTION)
        if answer == wx.YES:
            self.Close()
