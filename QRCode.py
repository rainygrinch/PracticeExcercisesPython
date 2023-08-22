# install all the libraries needed
# create and function that collects a text and converts it to a QR code
# save the QR code as an image
# run the function

# import QR Code Library
import qrcode

# create QR code function
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(File_Name)     # FIle Name will be specified by user, and appended with .png


# define variables for URL and File name from user, append .png to file name
url = input("Enter the URL: ")
File_Name = input("Enter a file name for the image: ")
File_Name = File_Name + (".png")

# run QR Code Generator
generate_qrcode(url)