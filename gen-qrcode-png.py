import qrcode
from PIL import Image

def create_qr_code_with_colored_logo(url, logo_path, output_path):
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

    # แปลงโลโก้เป็นโทนสีที่มาจากรูปภาพเดิม
    logo_colored = logo.convert("RGBA")

    # นำโลโก้ไปวางลงบน QR code
    qr_img.paste(logo_colored, (qr_img.size[0] // 2 - logo_colored.size[0] // 2, qr_img.size[1] // 2 - logo_colored.size[1] // 2))

    # บันทึกภาพ QR code ที่มีโลโก้ลงไป
    qr_img.save(output_path)

if __name__ == "__main__":
    url = "https://forms.gle/YFs5oQm2rCZYpwcA8"
    logo_path = "Logo/logo-thonburi.png"
    output_path = "qr_code_with_colored_logo.png"

    create_qr_code_with_colored_logo(url, logo_path, output_path)
