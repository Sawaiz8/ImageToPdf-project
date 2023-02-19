from PIL import Image
from PyPDF2 import PdfFileMerger
import os
def main():
    noOfImages = int(input("Enter the number of images to process:"))
    imageExtension = input("Enter the extension of the images:")
    seperatePdfs = input("Enter Y if you want to convert Images seperately and N if you dont:").lower()
    if seperatePdfs == "y": seperatePdfs = True
    else: seperatePdfs = False
    merger = PdfFileMerger()
    for imageNumber in range(1,noOfImages + 1):
        name = str(imageNumber)
        accessedImage = Image.open("Image (" + str(imageNumber) + ")" + imageExtension)
        accessedImage = accessedImage.convert("RGB") #It is important to change the color scheme otherwise it wont be compatible
        accessedImage.save(str(imageNumber) + ".pdf")#.save method cant save RGBA color scheme. Note some images are already in RGB
                                                     #so there is not need for it to change  
        if not seperatePdfs:
            merger.append(str(imageNumber) + ".pdf")
            #os.remove(str(imageNumber) + ".pdf")#I cannot remove a file that is appended in the merger. remove after CLOSING MERGER               
    if not seperatePdfs:merger.write("Combined.pdf")
    merger.close()
    if not seperatePdfs:
        for imageNumber in range(1,noOfImages+1):
            os.remove(str(imageNumber) + ".pdf") #Command to remove files
    
main()
                           
