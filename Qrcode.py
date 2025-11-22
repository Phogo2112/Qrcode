import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generate_qr_pdf(data, pdf_filename="NomDeVotreFichier.pdf"):
    qr = qrcode.make(data)
    img_path = "NomDeVotreImage.png"
    qr.save(img_path)
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    c.drawString(100, height - 100, f"QR Code pour : {'Ajoute le texte ici'}")
    c.drawImage(img_path, 150, height/2 - 150, width=300, height=300)
    c.save()
    print(f" PDF généré : {pdf_filename}")

generate_qr_pdf("ici L'url")
