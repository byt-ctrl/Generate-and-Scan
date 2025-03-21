# QR CODE GENERATOR FROM USER INPUT URL
# This code will generate a QR code from a user input URL and save it as 'QR Code.png' in the same directory.

import qrcode

# Data to be stored in QR Code Format
data = "https://www.python.org/"  # EXAMPLE DATA  (User can put any URL in Between "" to generate its QR Code)

# Creating The QR Code 
qr_code_generator=qrcode.QRCode(
    version=1,  # size of QR Code (Versions range from 1 to 40) (we took '1' here for efficency)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR Correction Level (L (Low) , M(Medium) , Q(Quartile) , H(High))
    box_size=12,  # Sixe of each Box in The QR GRID
    border=5,  # Thickness of the border (The Minimum value has to be 4)
)

qr_code_generator.add_data(data)
qr_code_generator.make(fit=True)

# Creating And Saving Image 
image=qr_code_generator.make_image(fill_color="black", back_color="white")
image.save("QR Code.png")
print("QR Code generated and saved as 'my_qr_code.png'.")

# END
