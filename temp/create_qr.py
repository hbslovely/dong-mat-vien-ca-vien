import qrcode
import os

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to QR code - now pointing to ShopeeFood
qr.add_data("https://shopeefood.vn/now-food/shop/1000090724")
qr.make(fit=True)

# Create image from QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("logo/qrcode.png")

print("QR code saved as logo/qrcode.png") 