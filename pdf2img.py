import os
import shutil

from pdf2image import convert_from_path, pdfinfo_from_path

input_dir = r"C:\Users\deldang1\PycharmProjects\OCR_BOT\input\0_InputDirectory"
working_dir = r"C:\Users\deldang1\PycharmProjects\OCR_BOT\input\1_WorkingDirectoryTmp"

try:
   for pdf_file in os.listdir(input_dir):
       os.chdir(working_dir)
       os.mkdir(pdf_file[:-4])
       shutil.copy(input_dir+"\\"+pdf_file,working_dir+"\\"+pdf_file)
except Exception as e:
   print("Directory already exists; Error: ", e)

# for pdf_file in os.listdir(working_dir):
#     if pdf_file.endswith(".pdf"):
#         pdf_file_dir = working_dir + "\\" + pdf_file[:-4]
#         pdf_file_path = os.path.join(working_dir, pdf_file)
#         info = pdfinfo_from_path(pdf_file_dir)
#         print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
#         print("PDF INFO: ")
#         print(info)
#         print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
#         maxPages = info["Pages"]
#         for page in range(1, maxPages + 1, 10):
#             convert_from_path(pdf_file, dpi=200, first_page=page, last_page=min(page + 10 - 1, maxPages))
#         pages = convert_from_path(pdf_file, 300)
#         shutil.move(working_dir + "\\" + pdf_file, working_dir + "\\" + pdf_file[:-4])
#         pdf_file = pdf_file[:-4]
#         for page in pages:
#             page.save(pdf_file_dir+"\\%s-page-%s.jpg" % (str(pages.index(page)).zfill(2), pdf_file), "JPEG")
#             print(pdf_file_dir+"\\%s-page-%s.jpg" % (str(pages.index(page)).zfill(2), pdf_file))
#     print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
#     print("PDF to Image conversion was successful")
#     print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")

for pdf_file in os.listdir(working_dir):
   if pdf_file.endswith(".pdf"):
       pdf_file_dir = working_dir + "\\" + pdf_file[:-4]
       pdf_file_path = os.path.join(working_dir, pdf_file)
       pdf_file_name = pdf_file[:-4]
       info = pdfinfo_from_path(pdf_file_path)
       print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
       print("PDF INFO: ")
       print(info)
       print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
       maxPages = info["Pages"]
       for j, page in enumerate(range(1, maxPages + 1)):
           pages = convert_from_path(pdf_file_path, dpi=200, first_page=page, last_page=min(page, maxPages))
           print("** Tracking ** Counter: %d - Page: %d - maxPages: %d - PagesLength: %d" % (j, page, maxPages, len(pages)))
           for p in pages:
               p.save(pdf_file_dir + "\\%s-page-%s.jpg" % (str(j).zfill(2), pdf_file_name), "JPEG")
               print(pdf_file_dir + "\\%s-page-%s.jpg" % (str(j).zfill(2), pdf_file_name))
       shutil.move(working_dir + "\\" + pdf_file, working_dir + "\\" + pdf_file[:-4])
       print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
       print("PDF to Image conversion was successful")
       print("_.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~.__.~\"~._.~\"~._.~\"~._.~\"~._")
