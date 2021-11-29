import pyqrcode
from pyqrcode import QRCode

if __name__ == '__main__':
    url = input("Enter url to make the QR code: ")
    name_of_QR_code = input("Enter name of QR code with svg extension: ")
    generate_QRcode = pyqrcode.create(url)
    generate_QRcode.svg(name_of_QR_code,scale=8)