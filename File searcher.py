
import os

def main():
    path = input("Enter the path to which you have to search: ")
    fileType = input("Enter the file extension you wanna search:")
    extensionLen = len(fileType)
    for root, directory, files in os.walk(path): #No files are stored in tree like structure
        for file in files:
            if file[-1 * extensionLen:] == fileType:
                 print(file)

main()
