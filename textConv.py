import cv2
import os
import pytesseract
from PyPDF2 import PdfReader
from os import listdir
 
#fileNames = [ "ANN900297298.pdf", "ANY900648244.pdf","ANY900652274.pdf","NBA900248381.pdf" ]
if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Nikitha.Thota\Downloads\OCR\OCR\tesseract.exe'
    #img_dir='C:\\Users\\Nikitha.Thota\\source\\repos\\text extraction\\'
    #a = PdfReader("C:\\Users\\Nikitha.Thota\\source\\repos\\text extraction\\ANY900648244.pdf")
    #a = PdfReader("ANN900297298.pdf", "ANY900648244.pdf","ANY900652274.pdf","NBA900248381.pdf" )
   
    # get the path or directory
    folder_dir = "C:\\Users\\Nikitha.Thota\\source\\repos\\text extraction"
    for images in os.listdir(folder_dir):
 
        # check if the image ends with png or jpg or jpeg
        if (images.endswith(".jpg")):
            # display
            for i in range(len(folder_dir)):
               img_path=f"output_{i}.jpg"
               dir=folder_dir+img_path
       
               img = cv2.imread(f"output_{i}.jpg")
        
               if img is not None:
                 text = pytesseract.image_to_string(f"output_{i}.jpg")
                 print(text)
                 os.remove(f"output_{i}.jpg")
