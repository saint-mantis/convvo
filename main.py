#god is great
#and thr msi
import eel
from  tkinter import *
from  tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import img2pdf
from PIL import Image
import os


eel.init('web')

imgtopdf_img_array=[]
imgtopdf_pdf_array=[]

@eel.expose
def select_img():
    import tkinter
    window=tkinter.Tk()
    window.attributes("-topmost", True)
    window.withdraw()
    img_path = filedialog.askopenfilename()
    print(img_path)
    imgtopdf_img_array.append(img_path)

@eel.expose
def save_file():
    files = [('PDF', '*.pdf')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    pdf_path=file.name
    imgtopdf_pdf_array.append(pdf_path)
    print(pdf_path)


@eel.expose
def convert_img_to_pdf():
    def ImgtoPdf(img_path,pdf_path):
        print("started")
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(pdf_path, "wb")
        file.write(pdf_bytes)
        image.close()
        file.close()
        print("Successfully made pdf file")

    ImgtoPdf(imgtopdf_img_array[0],imgtopdf_pdf_array[0])









eel.start('imgtopdf.html')








    