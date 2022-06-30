from pdf2image import convert_from_path 
import os

print(os.getcwd())   #already set the directory containing the pdf file (in spyder)

#extracting 50 images at a time else memory problem because of my large book
for iter in range(1,16+1):
    print("iteration %d" %iter)
    images= convert_from_path('hablemos-guarani.pdf',first_page=iter*50-50+1,last_page=(iter-1)*50+50)
    print("converted from path")
    
    i=iter*50-50+1
    for image in images:
        image.save('%003d.png' %i)  #saves images in the current directory itself
        print(i)
        i += 1
