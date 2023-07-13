
import glob
import os
import re
lista_archivos = glob.glob('*.png')
ln = [re.sub('[^a-zA-Z0-9\_\.]'), '',string.strip() for string in lista_archivos]
limpia = [string for string in ln if string]
for i in range(len(lista_archivos)):
    os.rename(lista_archivos[i], limpia[i])
