import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)

site = input("Site :")

qr.add_data(site)
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")
img.save('qrcode.png')