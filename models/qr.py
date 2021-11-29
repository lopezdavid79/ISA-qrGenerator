from   pathlib import Path 
import pyqrcode 
import png 


class Qr():
	def __init__(self , site ,name ,scale,qrFormat):
		self.site = site
		self.name = name
		self.scale =scale
		self.qrFormat=qrFormat

	def __str__(self):
		return f"{self.site}"
# Generate QR code 
	def generate_qr(self ):
		return  pyqrcode.create(self.site) 

	def save(self , qrcd):
		return qrcd.svg(self.name+".svg", scale = self.scale)    

	def save_png(self , qrcd):
		return qrcd.png(self.name+".png", scale = self.scale)    