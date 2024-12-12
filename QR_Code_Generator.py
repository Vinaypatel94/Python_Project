import qrcode  # Import the qrcode module 
user_input = input("Enter the text or URL to generate a QR code: ")

# Generate a QR code using the input
qr_code = qrcode.make(user_input)

# Save the QR code in file you working diactory
file_name = "qrcode.png"
qr_code.save(file_name)

print(f"QR code successfully saved as {file_name}.")



