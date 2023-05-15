import re


def escribir_txt(text,ruta):
    with open(ruta, "w") as file:
        file.write(text)
        # Cerrar el archivo
        file.close()

def limpiar(file_txt):

    # Abrir el archivo de texto y leer su contenido
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
    with open("./data_limpia/Hamer_franklin.txt", "w") as file:
        file.write(clean_text)
    return clean_text

def leer_documento(ruta):
    with open(ruta, "r") as file:
        content = file.read()

    return content