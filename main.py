import os
from html2image import Html2Image
from py2flowchart import *
from PIL import Image

current_path = os.getcwd()
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
