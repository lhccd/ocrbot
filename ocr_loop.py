import pytesseract
import os
from PIL import Image

def get_file(folderpath):
   for i in os.listdir(folderpath):
       if i.endswith('.pdf'):
           return i

def data_import(folderpath):
   files = []
   print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
   print("Importing all JPEG and PNG files of this folder")
   for i in os.listdir(folderpath):
       if i.endswith('.jpg') or i.endswith('.png'):
           files.append(open(os.path.join(folderpath, i)))
           print(i)
   print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
   return files

def ocr_fun(input, output, fn):
   files = input
   destination_dir = os.path.join(output, fn + ".txt")
   f = open(destination_dir, "w")
   for j, i in enumerate(files):
       im = Image.open(i)
       print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
       print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
       print("The OCR tool imports the image")
       print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
       # image = cv2.imread("Input.jpg")
       # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       print("Image imported successfully")
       print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
       print("The OCR tool tries to recognize characters and read the text on page ", j)
       print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
       # pytesseract.pytesseract.tesseract_cmd = 'ocr tool/tesseract.exe'
       text = pytesseract.image_to_string(im, lang='eng')
       print("Following text could be extracted out of the image: \n")
       print("========================================================================================\n")
       print(text, "\n")
       print("========================================================================================")
       print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
       print("\nExtracted Text will be written into a word document")
       print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
       f.write(text)
   f.close()
   print("Document successfully created.")
   print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
   print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")

# data_import()
# working_dir = r"C:\Users\deldang1\PycharmProjects\OCR_BOT\input\1_WorkingDirectoryTmp"
# output_dir = r"C:\Users\deldang1\PycharmProjects\OCR_BOT\input\2_OutputDirectory"
# directories = filter(os.path.isdir, os.listdir(working_dir))
# for value in os.listdir(working_dir):
#     filepath = os.path.join(working_dir, value)
#     if os.path.isdir(filepath):
#         images = data_import(filepath)
#         filename = get_file(filepath)
#         ocr_fun(images, output_dir, filename)

def ocr_loop():
   working_dir = r"C:\Users\deldang1\PycharmProjects\OCR_BOT\input\1_WorkingDirectoryTmp"
   output_dir = r"C:\Users\deldang1\PycharmProjects\OCR_BOT\input\2_OutputDirectory"

   filename = ""
   for value in os.listdir(working_dir):
       filepath = os.path.join(working_dir, value)
       if os.path.isdir(filepath):
           print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
           files = []
           for i in os.listdir(filepath):
               print("Importing all JPEG and PNG files of this folder")
               if i.endswith('.jpg') or i.endswith('.png'):
                   files.append(os.path.join(filepath, i))
                   print(i)
               if i.endswith('.pdf'):
                   filename=i[:-4]
           print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
           print("All images for OCR processing were imported successfully")
           print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
           destination_dir = os.path.join(output_dir, filename + ".doc")
           f = open(destination_dir, "w")
           #f = docx.Document()
           for j, i in enumerate(files):
               im = Image.open(i)
               print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
               print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
               print("The OCR tool imports the image")
               print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
               # image = cv2.imread("Input.jpg")
               # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
               print("Image imported successfully")
               print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
               print("The OCR tool is processing from file ", i)
               print("The OCR tool tries to recognize characters and read the text on page ", j)
               print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
               # pytesseract.pytesseract.tesseract_cmd = 'ocr tool/tesseract.exe'
               text = pytesseract.image_to_string(im, lang='eng')
               print("Following text could be extracted out of the image: \n")
               print("========================================================================================\n")
               print(text, "\n")
               print("========================================================================================")
               print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
               print("\nExtracted Text will be written into a word document")
               print(":.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:")
               f.write(text)
           f.close()
           print("Document successfully created.")
           print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
           print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
ocr_loop()

