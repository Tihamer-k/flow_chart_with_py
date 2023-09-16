import os
from py2flowchart import *  # lib para convertir un archivo PY a HTML
from html2image import Html2Image  # lib para convertir el HTML  a imagen
from PIL import Image  # lib para abrir la imagen creada

current_path = os.getcwd()  # para obtener la ruta actual del proyecto
path_project = (current_path + '\\process_op.py')


def html2image_use():
    hti = Html2Image()
    with open(current_path + '\\flowChart.html') as f:
        hti.screenshot(f.read(), save_as='out.png')


if __name__ == '__main__':
    pyfile2flowchart(path_project, 'flowChart.html')
    html2image_use()
    img = Image.open('out.png')
    img.show()
