""" Python program to delete empty folders"""

import os

# Función principal que borra todas las carpetas vacías
# Si una carpeta contiene otra carpeta y está vacía, se llamará de forma recursiva y la borrará
def deleteEmptyFolders(path):
    """
    Función que borra todas las carpetas vacías a partir de una ruta pasada como parámetro
    @param ruta: ruta de la carpeta que se desea analizar las carpetas vacías
    """

    dirs = os.listdir(path)

    # Recorremos todas las carpetas de esa ruta
    for carpeta in dirs:
        subfolder = path + carpeta
        # Comprobamos si el contenido es una carpeta
        if (os.path.isdir(subfolder)):
            # Comprobamos si está vacía, en ese caso la borramos
            if (isEmpty(subfolder)):
                os.rmdir(subfolder)
            # Sino, llamamos a un método recursivo para que borre las posibles subcarpetas vacías
            else:
                deleteEmptyFolders(subfolder + "/")
                # Si la carpeta raíz se ha quedado vacía, borrarla
                if (isEmpty(subfolder)):
                    os.rmdir(subfolder)


def isEmpty(folder):
    """
    Función que comprueba si una carpeta está vacía retornando true o false en caso contrario
    Se considera una carpeta vacía aquella que no contiene ni ficheros ni otras carpetas (aunque estén vacías)
    @param: carpeta a comprobar si está vacía o no
    """
    if (len(os.listdir(folder)) == 0):
        return True
    return False


# Programa principal

desktop_path = os.path.expanduser("~\Desktop\\")
downloads_path = os.path.expanduser("~\Downloads\\")
current_path = os.getcwd() + "\\"

print("\nProgram written with ♥ by @coral2742\n\n")

print("PATH OPTIONS:\n[DESKTOP]\n[DOWNLOADS]\n[CURRENT] is the current working directory\n")


validIOption = False
while (not validIOption):
    option = (input("Insert your path option: ")).upper()
    if (option == "DESKTOP"):
        validIOption = True
        path = desktop_path + input("Introduce el nombre de la carpeta raíz a analizar: ") + "\\"
    if (option == "DOWNLOADS"):
        validIOption = True
        path = downloads_path + input("Introduce el nombre de la carpeta raíz a analizar: ") + "\\"
    if (option == "CURRENT"):
        validIOption = True
        path = current_path


if (os.path.exists(path)):
    print("\PATH: " + path + "\n")
    print("\nFOLDER CONTENT: \n")
    print(os.listdir(path))
    print("\n")

    deleteEmptyFolders(path)

    print("UPDATED FOLDER CONTENT: \n")
    print(os.listdir(path))

else:
    print("\nERROR: El nombre de la carpeta no existe")
    exit

# Pulsar tecla para salir de la ventana de comandos
input()
