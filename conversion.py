import sys
import os
import PyPDF2
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import aspose.words as aw
import cv2
import pytesseract
from os import listdir
import pytesseract



folder_path = r"C:\Users\Nikitha.Thota\source\repos\text extraction"
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
print(pdf_files)
for pdf in (pdf_files):
    print(f"Converting {pdf} to images")
    pdf_path = os.path.join(folder_path, pdf)
    #print(pdf_path)
    # import module
    # Store Pdf with convert_from_path function
    f = open(pdf.split(".")[0]+"_opt.txt", "w")
    images = convert_from_path(pdf_path,500,poppler_path = r"C:\Users\Nikitha.Thota\Downloads\OCR\OCR\poppler-0.68.0_x86\poppler-0.68.0\bin")
    for i in range(len(images)):
       # Save pages as images in the pdf
       images[i].save('page'+ str(i) +'.jpg', 'JPEG')



       # opened file as reading (r) in binary (b) mode
    
       # store data in pdfReader
       pdfReader = PyPDF2.PdfReader(pdf_path)
        # count number of pages
       totalPages = len(pdfReader.pages)
        # print number of pages
       print(f"Total Pages: {totalPages}")
       break
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Nikitha.Thota\Downloads\OCR\OCR\tesseract.exe'
    # img_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    #print(img_files)
     # display
    for i in range(totalPages):
        # img_path=f"page{i}.jpg"
        # dir=folder_path+img_path
       
        img = cv2.imread(f"page{i}.jpg")
        
        if img is not None:
            text = pytesseract.image_to_string(f"page{i}.jpg")
            #print(text)
            f.write(text)
            
        else:
            print("data not found")

