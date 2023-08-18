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
    url = "https://forms.gle/YFs5oQm2rCZYpwcA8"
    file_path = "qr_form.png"  # เปลี่ยนเป็นตำแหน่งที่คุณต้องการเก็บไฟล์ QR code

    create_qr_code(url, file_path)
