"""
Este código realiza las siguientes tareas:

    Lee el archivo de texto llamado text.txt.
    Realiza la tokenización de oraciones en español, dividiendo el texto en oraciones individuales.
    Realiza la tokenización de palabras en español, dividiendo el texto en palabras individuales.
    Convierte las palabras en un objeto de texto de NLTK llamado text_object.
    Calcula la frecuencia de cada palabra utilizando la clase FreqDist de NLTK.
    Imprime las 10 palabras más frecuentes.
    Utiliza el método concordance de text_object para buscar frases o palabras dentro del texto que contengan la palabra "Jara Ocas".
    Identifica las sustantivos en
"""


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist, Text, pos_tag

# Descargar los paquetes necesarios para el procesamiento en español
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")

# Leer el archivo de texto
with open("./data_segmentada/habilidades/Hamer_franklin.txt", "r") as file:
    text = file.read()

# Tokenización de oraciones
sentences = sent_tokenize(text, language="spanish")

# Tokenización de palabras
words = word_tokenize(text, language="spanish")

# Convertir las palabras en un objeto de texto de NLTK
text_object = Text(words)

# Calcular la frecuencia de las palabras
fdist = FreqDist(words)

# Imprimir las 10 palabras más frecuentes
print("10 palabras más frecuentes:")
print(fdist.most_common(20))

# Buscar frases o palabras dentro del texto
search_word = "python"
print(f"Frases que contienen la palabra '{search_word}':")
text_object.concordance(search_word)

# Hallar oraciones importantes y contextuales
#tagged_words = pos_tag(words, lang="spanish")
#nouns = [word for word, pos in tagged_words if pos.startswith("N")]
#text_object = Text(nouns)
#print("Oraciones importantes y contextuales:")
#text_object.collocations()
