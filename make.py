

from pdf2image import convert_from_path

 

images = convert_from_path(repr('C:/Users/drdeb/OneDrive/Desktop/tt.pdf'),500,poppler_path="poppler/bin")
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save(repr('C:/Users/drdeb/OneDrive/Desktop/page1')+ str(i) +'.jpg', 'JPEG')