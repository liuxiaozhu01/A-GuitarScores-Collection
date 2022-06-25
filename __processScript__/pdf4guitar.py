from PIL import Image
import img2pdf
import os

a4input = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4input)

file_list = os.listdir('..')
print(file_list)
target_path = '..//__target__//'
for music in file_list:
    if(music[0:2] == '__'):
        continue
    else:
        print(music+'...',end='')
        try:
            imgs_path = '..//' + music
            imgs_list = os.listdir(imgs_path)
            # print(imgs_list)
            pdf_path = target_path + music + '.pdf'
            # print(pdf_path)
            os.chdir('..//'+music)
            with open(target_path + music + '.pdf', 'wb') as f:
                f.write(img2pdf.convert(imgs_list, layout_fun=layout_fun))
            print('ok')
        except:
            print('error!')
            
