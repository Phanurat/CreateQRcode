import qrcode

def create_colored_qr_code(url, output_path, qr_fill_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=qr_fill_color, back_color="white")
    qr_img.save(output_path)

if __name__ == "__main__":
    url = "https://forms.gle/YFs5oQm2rCZYpwcA8"
    output_path = "colored_qr_code.png"
    qr_fill_color = "#FF0000"  # เปลี่ยนเป็นสีที่คุณต้องการ (ในรูปแบบ HEX color code)

    create_colored_qr_code(url, output_path, qr_fill_color)
