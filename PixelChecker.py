from PIL import Image

def main():
    name = input("Enter the file name with its extension: ")
    imageObject = Image.open(name)
    width, length = imageObject.size
    print("Width:", width, "Length:", length, "Total Pixels:", width * length)

main()
