"""
Este código realiza las siguientes tareas:

    Lee el archivo de texto llamado text.txt en español.
    Utiliza la clase Translator de la biblioteca translate para traducir el texto a inglés.
    Escribe la traducción en un archivo de texto llamado translated_text.txt en inglés.

Ten en cuenta que necesitarás instalar la biblioteca translate antes de utilizarla en tu código. Puedes hacerlo con el comando pip install translate.

Este código realiza las siguientes tareas:

    Lee el archivo de texto llamado text.txt en inglés.
    Utiliza la clase Translator de la biblioteca translate para traducir el texto a español.
    Escribe la traducción en un archivo de texto llamado translated_text.txt en español.

Ten en cuenta que necesitarás instalar la biblioteca translate antes de utilizarla en tu código. Puedes hacerlo con el comando pip install translate.

"""

from translate import Translator


def traductor_a_ingles():
    # Leer el archivo de texto en español
    with open("text.txt", "r") as file:
        text = file.read()

    # Traducir el texto a inglés
    translator = Translator(to_lang="en")
    translation = translator.translate(text)

    # Escribir la traducción en un archivo de texto en inglés
    with open("translated_text.txt", "w") as file:
        file.write(translation)

def traductor_a_español():
    # Leer el archivo de texto en inglés
    with open("text.txt", "r") as file:
        text = file.read()

    # Traducir el texto a español
    translator = Translator(to_lang="es")
    translation = translator.translate(text)

    # Escribir la traducción en un archivo de texto en español
    with open("translated_text.txt", "w") as file:
        file.write(translation)
