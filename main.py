# begin wxGlade: dependencies
import gettext

# end of class Principal
import wx
from fr_principal   import Principal 
# end of class Principal

class MyApp(wx.App):
	def OnInit(self):
		self.frame = Principal(None, wx.ID_ANY , "")
		self.SetTopWindow(self.frame)
		self.frame.Show()
		return True

# end of class MyApp

if __name__ == "__main__":
	gettext.install("app") # replace with the appropriate catalog name

	app = MyApp(0)
	app.MainLoop()
