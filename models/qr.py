# Import QRCode from pyqrcode 
import pyqrcode 
import png 


class Qr():
	def __init__(self , site ,name ,scale,qrFormat):
		self.site = site
		self.name = name
		self.scale =scale
		self.qrFormat=qrFormat
# Generate QR code 
	def generate_qr(self ):
		return  pyqrcode.create(self.site) 

	def save(self , qrcd):
		return qrcd.svg(self.name+"."+self.qrFormat, scale = self.scale)    

	def save_png(self , qrcd):
		return qrcd.png(self.name+"."+sel.qrFormat, scale = self.scale)    