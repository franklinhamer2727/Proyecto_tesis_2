import os
import re


def escribir_txt(text,ruta):
    with open(ruta, "w") as file:
        file.write(text)
        file.close()

def limpiar(file_txt):
    with open(file_txt, "r") as file:
        text = file.read()
    # Limpiar el texto usando expresiones regulares
    clean_text = re.sub(r'[^a-zA-Z\sáéíóúÁÉÍÓÚñÑ]', '', text)
    # Eliminar más de un salto de línea
    clean_text = re.sub(r'\n+', '\n', clean_text)
    # Eliminar espacio en blanco al inicio y al final de la línea
    clean_text = re.sub(r'^\s+|\s+$', '', clean_text)
    return limpiar_documento(clean_text)
def limpiar_documento(clean_text):
    # Eliminar espacio en blanco al inicio y al final de la línea
    clean_text = re.sub(r'^\s+|\s+$', '', clean_text)
    with open("data_limpia/Hamer_Franklin.txt", "w") as file:
        file.write(clean_text)
    return clean_text

def leer_documento(ruta):
    with open(ruta, "r") as file:
        content = file.read()

    return content

def leer_contenido_directorio(ruta_directorio):
    archivos = os.listdir(ruta_directorio)
    nombres_archivos = []
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_directorio, archivo)
        if os.path.isfile(ruta_archivo):
            nombre_archivo = os.path.basename(ruta_archivo)
            nombres_archivos.append(nombre_archivo)
    return nombres_archivos

