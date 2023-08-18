import qrcode
from PIL import Image

def create_qr_code_with_logo(url, logo_path, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # โหลดรูปโลโก้
    logo = Image.open(logo_path)

    # ปรับขนาดของโลโก้ให้เหมาะสมกับ QR code
    logo = logo.resize((50, 50))

    # นำโลโก้ไปวางลงบน QR code
    qr_img.paste(logo, (qr_img.size[0] // 2 - logo.size[0] // 2, qr_img.size[1] // 2 - logo.size[1] // 2))

    # บันทึกภาพ QR code ที่มีโลโก้ลงไป
    qr_img.save(output_path)

if __name__ == "__main__":
    url = "https://www.example.com"
    logo_path = "logo.png"  # เปลี่ยนเป็นตำแหน่งไฟล์โลโก้ที่คุณมี
    output_path = "qr_code_with_logo.png"  # เปลี่ยนเป็นตำแหน่งที่คุณต้องการเก็บไฟล์ QR code ที่มีโลโก้

    create_qr_code_with_logo(url, logo_path, output_path)
