########### BATCH Quitar Basura de Nombres ##########################
# 1.- quita glyphs no deseados de los nombres de archivos y carpetas
#     enforce Pascal Naming 
# 2.- reemplaza extension de los archivos
# Autor:  Homar Richard Orozco Apaza
#           LaPaz - Bolivia
# Mail: homar.orozco@gmail.com
####################################################################
import os
from pathlib import Path
import re

tplExtension = ('.m4v','.mp4')
    
def arreglarFolder(木, nombreViejo):             # osea Folders
    文字列 = nombreViejo 
    表現 = re.compile(r'[^\w\s]')               #quitar puntuacion
    文字列 = re.sub(表現 , '', 文字列)
    表現 = re.compile(r'(\s)+(\w)')              #grupos
    文字列 = re.sub(表現 , aMayuscula, 文字列)     #nombre arreglado
    os.rename(os.path.join(木, nombreViejo), os.path.join(木, 文字列))

def arreglarArchivo(木, nombreArchivo):
    文字列 = Path(nombreArchivo).stem                                     # solo usar el nombre sin extension
    表現 = re.compile(r'[^\w\s]')               #quitar puntuacion
    文字列 = re.sub(表現 , '', 文字列)
    表現 = re.compile(r'(\s)+(\w)')              #grupos
    文字列 = re.sub(表現 , aMayuscula, 文字列)     #nombre arreglado
    文字列 += Path(nombreArchivo).suffix
    print(文字列)
    os.rename(os.path.join(木, nombreArchivo), os.path.join(木, 文字列))

def cambioDeExtension(木, nombreArchivo):
    if Path(nombreArchivo).suffix in tplExtension[0]:
        文字列 = nombreArchivo.replace(tplExtension[0], tplExtension[1])   
        os.rename(os.path.join(木, nombreArchivo), os.path.join(木, 文字列))

def aMayuscula(cadenita):
    return cadenita.group(2).upper()

def main():
    print("----------------------------------------------------------")
    for 木, folders, archivos in os.walk(os.getcwd()):                      # el arbol de directorios        
        for folderName in folders:            
            arreglarFolder(木, folderName)
        
    for 木, folders, archivos in os.walk(os.getcwd()):                      # el arbol de directorios        
        for nombreArchivo in archivos:
            arreglarArchivo(木, nombreArchivo)
    
    # for 木, folders, archivos in os.walk(os.getcwd()):                      # el arbol de directorios
    #     for nombreArchivo in archivos:
    #         cambioDeExtension(木, nombreArchivo)

if __name__ == "__main__": main()