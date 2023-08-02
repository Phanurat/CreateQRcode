from PIL import Image

# กำหนดตำแหน่งไฟล์ที่เก็บ QR code ที่สร้างขึ้น
file_path = "qr_code.png"

# แสดงรูปภาพ QR code บนหน้าจอ
img = Image.open(file_path)
img.show()
