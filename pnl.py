import re
import funciones

# Texto extraído del archivo PDF



def segmentacion_(text):
    informacion_personal= re.compile(r'(.*?)\nResumen', re.DOTALL)
    resumen =re.compile(r'Resumen(.*?)Experiencia laboral',re.DOTALL)
    experiencia_laboral = re.compile(r'Experiencia laboral(.*?)Honores y reconocimientos', re.DOTALL)
    honores_reconocimientos = re.compile(r'Honores y reconocimientos(.*?)Proyectos', re.DOTALL)
    proyectos = re.compile(r'Proyectos(.*?)Educación', re.DOTALL)
    educacion = re.compile(r'Educación(.*?)Cursos Certificados', re.DOTALL)
    cursos_certificados = re.compile(r'Cursos Certificados(.*?)Habilidades', re.DOTALL)
    habilidades = re.compile(r'Habilidades(.*?)  ', re.DOTALL)



    informacion_personal = informacion_personal.search(text).group(1).strip()
    resumen = resumen.search(text).group(1).strip()
    experiencia_laboral = experiencia_laboral.search(text).group(1).strip()
    honores_reconocimientos = honores_reconocimientos.search(text).group(1).strip()
    proyectos = proyectos.search(text).group(1).strip()
    educacion = educacion.search(text).group(1).strip()
    cursos_certificados = cursos_certificados.search(text).group(1).strip()
    habilidades = habilidades.search(text).group(1).strip()
    print(habilidades)

    #rutas creadas
    ruta_informacion_personal ='./data_segmentada/informacion_personal/Hamer_franklin.txt'
    ruta_resumen ='./data_segmentada/resumen/Hamer_franklin.txt'
    ruta_experiecia_laboral ='./data_segmentada/experiencia_laboral/Hamer_franklin.txt'
    ruta_honores_reconocimientos ='./data_segmentada/honores_reconocimientos/Hamer_franklin.txt'
    ruta_proyectos ='./data_segmentada/proyectos/Hamer_franklin.txt'
    ruta_educacion ='./data_segmentada/educacion/Hamer_franklin.txt'
    ruta_cursos_certificados ='./data_segmentada/cursos_certificados/Hamer_franklin.txt'
    ruta_habilidades ='./data_segmentada/habilidades/Hamer_franklin.txt'

    funciones.escribir_txt(informacion_personal,ruta_informacion_personal)
    funciones.escribir_txt(resumen,ruta_resumen)
    funciones.escribir_txt(experiencia_laboral,ruta_experiecia_laboral)
    funciones.escribir_txt(honores_reconocimientos,ruta_honores_reconocimientos)
    funciones.escribir_txt(proyectos,ruta_proyectos)
    funciones.escribir_txt(educacion,ruta_educacion)
    funciones.escribir_txt(cursos_certificados, ruta_cursos_certificados)
    funciones.escribir_txt(habilidades, ruta_habilidades)

    #print('Informacion personal:\n', informacion_personal)
    #print('Resumen:\n', resumen)
    #print('Experiencia Laboral:\n', experiencia_laboral)
    #print('Honores y reconocimientos:\n', honores_reconocimientos)
    #print('Proyectos:\n', proyectos)
    #print('Educacion:\n', educacion)
    #print('Cursos certificados:\n', cursos_certificados)

    #print('Habilidades:\n', habilidades)




