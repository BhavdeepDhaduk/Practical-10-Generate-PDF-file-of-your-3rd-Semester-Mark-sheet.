"""BHAVDEEP DHADUK -20CE024
Practical 10: Generate PDF file of your 3rd Semester Mark-sheet."""
from fpdf import FPDF
# save FPDF() class into
# a variable pdf
pdf = FPDF()
# Add a page
pdf.add_page()
# set style and size of font
# that you want in the pdf
# open the text file in read mode
f = open("marksheet.txt", "r")
pdf.set_font("Arial", size = 16, style="B")
pdf.cell(200, 0, txt = "MARKSHEET", ln = 1, align="C")
pdf.set_font("Arial", size = 10)
pdf.cell(200, 10, txt = "SEMESTER-3", ln = 1, align="C")
# insert the texts in pdf
pdf.set_font("Arial", size = 12, style="B")
pdf.cell(200, 20, txt = "Name: BHAVDEEP PRAVINBHAI DHADUK", ln = 2)
pdf.set_font("Arial", size = 12)
for x in f:
	# pdf.cell(100, 10, txt = " Subject",border= 1 , ln = 0)
	# pdf.cell(50, 10, txt = " Credits",border= 1 , ln = 0)
	# pdf.cell(0, 10, txt = " Grades",border= 1 , ln = 1)
  pdf.cell(0, 6, txt = x, ln = 1)
# save the pdf with name .pdf
pdf.output("Result.pdf")