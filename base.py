import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate_qr_pdf(data, pdf_filename="qr_code.pdf"):
    # Générer l'image QR
    qr = qrcode.make(data)
    img_path = "temp_qr.png"
    qr.save(img_path)

    # Crée le PDF avec ReportLab
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4

    # Optionnel : ajouter du texte
    c.drawString(100, height - 100, f"QR Code pour : {'https://www.cleanertombe.fr/'}")

    # Ajouter l'image QR au centre
    c.drawImage(img_path, 150, height/2 - 150, width=300, height=300)

    # Sauvegarder le PDF
    c.save()

    print(f"✅ PDF généré : {pdf_filename}")

# Exemple d'utilisation
generate_qr_pdf("https://www.cleanertombe.fr/")