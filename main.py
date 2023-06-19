import funciones
import pdfminer_pdf
import pnl
import os

if __name__ == '__main__':

    array_nombres = funciones.leer_contenido_directorio("./data_pdf/")
    for nombre in array_nombres:
        pdf_path = os.path.join('./data_pdf/',nombre)
        solo_nombre, extencion = nombre.split(".")
        ruta_txt = os.path.join("./data_txt",solo_nombre+'.txt')
        text = pdfminer_pdf.extract_text_from_pdf(pdf_path)

        funciones.escribir_txt(text, ruta_txt) #escribir  el texto en un txt
        text_limpio = funciones.limpiar(ruta_txt)
        text_seg = funciones.leer_documento(os.path.join('./data_limpia',solo_nombre +'.txt'))
        pnl.segmentacion_(text_seg)