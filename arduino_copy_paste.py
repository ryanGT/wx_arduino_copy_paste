import wx

box_width = 400

class Mywin(wx.Frame): 
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title,size = (600,400))

        panel = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 

        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(panel, -1, "Base Filename") 

        hbox1.Add(l1, 1, wx.ALIGN_RIGHT|wx.ALL,5) 
        self.base_name = wx.TextCtrl(panel,-1, size=(box_width, -1)) 

        hbox1.Add(self.base_name,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.base_name.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
        vbox.Add(hbox1) 

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "Data Folder") 

        hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5) 
        self.data_folder = wx.TextCtrl(panel,-1, size=(box_width, -1)) 
        hbox2.Add(self.data_folder,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        self.browse_button = wx.Button(panel, wx.Window.NewControlId(), label = "browse", \
                      style = wx.ALIGN_CENTER) 
        hbox2.Add(self.browse_button,1,wx.ALIGN_RIGHT|wx.ALL,5)
        self.Bind(wx.EVT_BUTTON, self.onBrowse, self.browse_button)
        
        vbox.Add(hbox2) 

        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
        l3 = wx.StaticText(panel, -1, "Data from Arduino") 

        hbox3.Add(l3,1, wx.ALIGN_LEFT|wx.ALL,5) 
        self.t3 = wx.TextCtrl(panel,size = (box_width,200),style = wx.TE_MULTILINE) 

        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox3) 
        self.t3.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)  

        hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
        l4 = wx.StaticText(panel, -1, "") 

        hbox4.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.go_button = wx.Button(panel, wx.Window.NewControlId(), label = "Save to CSV", \
                              style = wx.ALIGN_CENTER) 

        hbox4.Add(self.go_button,1,wx.EXPAND|wx.ALIGN_CENTER|wx.ALL,5) 
        vbox.Add(hbox4) 
        panel.SetSizer(vbox)


        ## Menu and keyboard shortcuts

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        quitID = wx.Window.NewControlId()
        quitMenuItem = fileMenu.Append(quitID, "Quit",
                                       "Quit the application")
        saveID = wx.Window.NewControlId()
        saveMenuItem = fileMenu.Append(saveID, "Save CSV File",
                                       "Save Arduino data to CSV file")
        browseID = wx.Window.NewControlId()
        browseMenuItem = fileMenu.Append(browseID, "Browse for data folder",
                                       "Browse for the data to save the CSV data into")

        
        menuBar.Append(fileMenu, "&File")
        self.Bind(wx.EVT_MENU, self.onQuit, quitMenuItem)
        self.Bind(wx.EVT_MENU, self.onSave, saveMenuItem)
        self.Bind(wx.EVT_MENU, self.onBrowse, browseMenuItem)         
        self.SetMenuBar(menuBar)


        # set up accelerators
        accelEntries = []
        accelEntries.append((wx.ACCEL_CTRL, ord('q'), quitID))
        accelEntries.append((wx.ACCEL_CTRL, ord('s'), saveID))
        accelEntries.append((wx.ACCEL_CTRL, ord('b'), browseID))                

        accelTable  = wx.AcceleratorTable(accelEntries)
        self.SetAcceleratorTable(accelTable)


        self.Centre() 
        self.Show() 
        self.Fit()  


    def onQuit(self, event):
        self.Close()


    def onSave(self, event):
        print("this is what I would do to save data...")
        print("...someone should write this function")


    def onBrowse(self, event):
        print("this is what I would do to browse for the folder to save the data in...")
        print("...someone should write this function")

        
    def OnKeyTyped(self, event): 
        print(event.GetString())

    def OnEnterPressed(self,event): 
        print("Enter pressed")

    def OnMaxLen(self,event): 
        print("Maximum length reached")

app = wx.App() 
Mywin(None,  'TextCtrl demo')
app.MainLoop()
