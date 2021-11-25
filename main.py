from models.qr import Qr
# import pyqrcode


site =input("ingrese enlace  web") 
name = input("ingrese nombre de archivo")
scale = int(input("ingrese tamaño de escala"))
qrFormat = input("ingrese formato")
  

qr = Qr(site , name , scale,qrFormat)

qrcd = qr.generate_qr() 

if qrFormat=="svg":	
	qr.save(qrcd)
elif qrFormat== "png":
	qr.save(qrcd)
print("Generando qr")