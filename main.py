from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs=[]
n=int(input("how many pdf you merge\n"))
for i in range(0,n):
    name=input(f"enter the name of pdf{i+1}:")
    pdfs.append(name)
    
for pdf in pdfs:
    merger.append(pdf)3

merger.write("merged-pdf.pdf")
merger.close()