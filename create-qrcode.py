import qrcode

def create_qr_code(url, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

if __name__ == "__main__":
    # เปลี่ยน url ตามลิงก์ที่ต้องการสร้าง QR code
    url = "https://drive.google.com/drive/folders/1bDb-dKuspAM_4BckY3EfcVv077R97wvE?usp=drive_link"
    file_path = "qr_code.png"  # เปลี่ยนเป็นตำแหน่งที่คุณต้องการเก็บไฟล์ QR code

    create_qr_code(url, file_path)
