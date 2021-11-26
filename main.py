#god is great
    
import eel
from  tkinter import *
from  tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import img2pdf
from PIL import Image
import os
import pdf2image


eel.init('web')

imgtopdf_img_array=[]
imgtopdf_pdf_array=[]
pdftoimgopen_array=[]
pdftoimgsave_array=[]

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
    import tkinter
    window=tkinter.Tk()
    window.attributes("-topmost", True)
    window.withdraw()
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

@eel.expose
def pdftoimgselect_img():
    import tkinter
    window=tkinter.Tk()
    window.attributes("-topmost", True)
    window.withdraw()
    img_path = filedialog.askopenfilename()
    print(img_path)
    pdftoimgopen_array.append(img_path)


@eel.expose
def pdftoimgsave_file():
    files = [('Img', '*.jpg')]
    import tkinter
    window=tkinter.Tk()
    window.attributes("-topmost", True)
    window.withdraw()
    file = asksaveasfile(filetypes = files, defaultextension = files)
    pdf_path=file.name
    pdftoimgsave_array.append(pdf_path)
    print(pdf_path)



@eel.expose
def convert_pdftoimg():
    def pdftoimg(pdfpath,imgpath):
        from pdf2image import convert_from_path
        images = convert_from_path(pdfpath,500,poppler_path="poppler/bin")
        for i in range(len(images)):
            images[i].save(imgpath+ str(i) +'.jpg', 'JPEG')
    print("success")

    pdftoimg(pdftoimgopen_array[0],pdftoimgsave_array[0])
        
   

    

   
  
    









eel.start('pdftoimg.html',size=(1000, 600), position=(450,150))








    