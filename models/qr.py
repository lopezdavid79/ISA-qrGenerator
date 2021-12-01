from   pathlib import Path 
import pyqrcode 
import png 


class Qr():
	def __init__(self , site ,name ,scale,qrFormat,path):
		self.site = site
		self.name = name
		self.scale =scale
		self.qrFormat=qrFormat
		# self.path="C:/Users\david\Downloads/"
		self.path = path

	def __str__(self):
		return f"{self.site}"
# Generate QR code 
	def generate_qr(self ):
		return  pyqrcode.create(self.site) 

	def save(self , qrcd):
		return qrcd.svg(Path(self.path,self.name+".svg"), scale = self.scale)    

	def save_png(self , qrcd):
		return qrcd.png(Path(self.path,self.name+".png"), scale = self.scale)    