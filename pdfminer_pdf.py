from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
#importar funciones


#defnimos una funcion
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    string_io = StringIO()
    device = TextConverter(resource_manager, string_io, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)
    text = string_io.getvalue()
    device.close()
    string_io.close()

    return text
































































