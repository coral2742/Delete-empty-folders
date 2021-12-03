'''
Python program to delete empty folders
Program written with ♥ by @coral2742
'''

import os
# Main function that deletes all the empty folders
# If a folder contains another and it's empty, a recursive function will be called and this folder will be deleted
def deleteEmptyFolders(path):
    """
    Function that deletes all empty folders from a path passed as parameter
    @param path: path of the folder to be scanned for empty folders
    """

    dirs = os.listdir(path)

    # Iterate all the folders from this path
    for carpeta in dirs:
        subfolder = path + carpeta
        # Probe if the content is a folder
        if (os.path.isdir(subfolder)):
            # Probe if it's empty to delete it
            if (isEmpty(subfolder)):
                os.rmdir(subfolder)
            # Otherwise, a recursive method will be called to delete the empty subfolders
            else:
                deleteEmptyFolders(subfolder + "/")
                # If the main folder is empty, delete it
                if (isEmpty(subfolder)):
                    os.rmdir(subfolder)


def isEmpty(folder):
    """
    Function that checks if a folder is empty returning true or false
    An empty folder is considered one that doesn't contain files or others folders (even if they're empty)
    @param folder: folder to check if it's empty or not
    """
    if (len(os.listdir(folder)) == 0):
        return True
    return False


# Main

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
        path = desktop_path + input("Insert main folder name: ") + "\\"
    if (option == "DOWNLOADS"):
        validIOption = True
        path = downloads_path + input("Insert main folder name: ") + "\\"
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
    print("\nERROR: Name's folder doesn't exist")
    exit

# Press any key to exit
input()
