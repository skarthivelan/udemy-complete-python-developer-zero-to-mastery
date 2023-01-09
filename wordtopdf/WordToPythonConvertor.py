from docx2pdf import convert

def converter():
    convert("sample.docx")
    convert("sample.docx", "SamplePdf.pdf")
    convert("/Users/Shared/Python")

converter()