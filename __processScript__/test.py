# this script should be in the same directory with images
# as you see from the file name, it is a test script
from PIL import Image
import img2pdf
import os

a4input = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4input)

def guitarpro_pdf_convert():

    photo_list = os.listdir('.')[0:-1]
    print(photo_list)
    for i in range(len(photo_list)):
        im = Image.open(photo_list[i])
        im = im.convert('RGB')
        im.save(photo_list[i])
    with open('.'+'\\1result.pdf', 'wb') as f:
        f.write(img2pdf.convert(photo_list, layout_fun=layout_fun))

guitarpro_pdf_convert()