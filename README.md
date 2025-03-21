# QR Code Generator and Scanner 🔍📱

→  The project enables Python users to create along with scan QR codes.  This software transforms any type of information including URLs into QR codes which it saves as image files.  The python file uses a QR Code Scanner component to extract data from images by reading QR codes before displaying results on the console. The project uses the **`qrcode`**  library to generate QR codes and the   **`pyzbar`** library to scan and decode QR codes. The detected QR code receives highlighting within the image that OpenCV displays.  The running system requires users to make a QR code through the generator section followed by scanning and decoding processes from the image itself.

## How to Use 🛠️

→  First , generate your desired URL QR code using the `QR_code_generator.py` file. The file operation generates the saved QR code image within the same directory after program execution. Once the QR code is generated, use the `scanner.py` file to scan the QR code image. The terminal will show the URL content encoded in the QR code after scanning it.


---
## What Are The Requirements ⚙️

- Python 3
- Libraries : `qrcode`, `opencv-python`, `pyzbar`
  
Install the required libraries using the following command:

→   The following libraries are required for this project:

- `qrcode` for generating QR codes
- `opencv-python` for handling images
- `pyzbar` for scanning QR codes from images
- `numpy` for handling arrays in OpenCV

After setting up the libraries, you can generate and scan QR codes using the provided Python scripts. 
