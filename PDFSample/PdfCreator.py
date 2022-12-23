from fpdf import FPDF


def createEmptyPagePDF():
    document = FPDF()
    document.add_page()
    document.output('emptypage.pdf', 'F')

createEmptyPagePDF()