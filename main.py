import funciones
import pdfminer_pdf
import pnl


if __name__ == '__main__':
    pdf_path = './data_pdf/Hamer_Franklin.pdf'
    ruta = "./data_txt/Hamer_Franklin.txt"
    text = pdfminer_pdf.extract_text_from_pdf(pdf_path)

    funciones.escribir_txt(text, ruta)
    text_limpio = funciones.limpiar('./data_txt/Hamer_Franklin.txt')
    text_seg = funciones.leer_documento('./data_limpia/Hamer_franklin.txt')
    pnl.segmentacion_(text_seg)