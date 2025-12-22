#  PDF Merger (Merge PDF using python) (i have added one notification system to let you know your pdf is merged successfully)
from PyPDF2 import PdfWriter
from plyer import notification

merger = PdfWriter()

pdfs = []
n = int(input("Enter number of PDF you want to merge: \n"))
for i in range(0,n):
    name = (input(f"Enter the name of PDF {i+1}: "))
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
notification.notify(title  = "PDF Merging Successful",message = "Your PDFs are successfully merged" )
merger.close()