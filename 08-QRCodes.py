#QR Codes
import pyqrcode
from pyqrcode import QRcode
# String which represent the QR code 
s = ""
# Generate QR code 
url = pyqrcode.creae(s)
# Create and save the png file naming "myqr.png" 
url.svg(".svg", scale = 8) 
