from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm


doc = SimpleDocTemplate("PDFavecImage.pdf", pagesize = A4)

largeurP, hauteurP = A4

Story = []
GraphIV = "IV.jpg"
GraphP = "Piv.jpg"


im = Image(GraphIV, width = largeurP - 2*cm , height = hauteurP/2 - 5*cm)
Story.append(im)

Story.append(Spacer(1, 50))

im2 = Image(GraphP, width = largeurP - 2*cm, height = hauteurP/2 - 5*cm)
Story.append(im2)

doc.build(Story)