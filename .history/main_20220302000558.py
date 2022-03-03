from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog

from FloorList import FloorList



FloorList1 = FloorList()

def FileChooser():
    RuteFIle = ''
    Tk().withdraw()
    try:
        filename = filedialog.askopenfile(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos xml', "*.{}".format('xml')),
                         ('Todos los archivos', '*.*'))
        )
        return filename
    except:
        print('No se selecciono correctamente el archivo')
        return None


def ElementTree(file):
    tree = ET.parse(file)
    root = tree.getroot()
    for element in root:
        name = element.attrib['nombre']
        row = ''
        column = ''
        flip = ''
        slide = ''
        for subelement in element:
            tag = str(subelement.tag).lower()
            if tag == 'r':
                row = int(subelement.text)
            elif tag == 'c':
                column = int(subelement.text)
            elif tag == 'f':
                flip = int(subelement.text)
            elif tag == 's':
                slide = int(subelement.text)
            elif tag == 'patrones':
                patrones = subelement
            else:
                print('Atributo no registrable', subelement.tag)
        FloorList1.AddFloor(name, row, column, flip, slide, patrones)
        
        
if __name__ == '__main__':

    while True:
        Menu = input ('''==============================
||1. Cargar Archivo XML     ||
||2. Mostrar Pisos Cargados ||
||3. Analizar               ||
||4. Reportes               ||
||5. Salir                  ||
==============================
Elige una opción:  ------->  ''')

        if Menu == '1':
            FilePath = FileChooser()
            ElementTree(FilePath)
            print('Elementos Cargados Exitosamente')
        elif Menu == '2':
            while True:
                FloorList1.ShowFloors()
                MenuDos = input('''=================================
||1. Selecciona un Piso         ||
||2. Regresar al Menu Principal ||
=================================
Elige una opción:  ------->  ''')
                if MenuDos == '1':
                    pass
                elif MenuDos == '2':
                    break



    