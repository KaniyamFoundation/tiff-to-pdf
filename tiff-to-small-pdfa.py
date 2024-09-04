import os
import sys
import time
from pathlib import Path

markpdf = Path("./markpdf_linux-amd64")

if markpdf.is_file():
    print("Found markpdf. Adding execute permission to it.")
    os.system("chmod a+x ./markpdf_linux-amd64")
else:
    ("The file markpdf_linux-amd64 is missing in current folder. Downloading it.")

    try:
        os.system("wget -q https://github.com/KaniyamFoundation/tiff-to-pdf/raw/main/markpdf_linux-amd64")
        os.system("chmod a+x ./markpdf_linux-amd64")
    except:
        print("Cant download it. Please download manually and place in current folder")
        sys.exit()



shrinkpdf = Path("./shrink-pdf.sh")

if shrinkpdf.is_file():
    print("Found shrink-pdf.sh. Adding execute permission to it.")
    os.system("chmod a+x ./shrink-pdf.sh")
else:
    ("The file shrink-pdf.sh is missing in current folder. Downloading it.")

    try:
        os.system("wget -q https://raw.githubusercontent.com/KaniyamFoundation/tiff-to-pdf/main/shrink-pdf.sh")
        os.system("chmod a+x ./shrink-pdf.sh")
    except:
        print("Cant download it. Please download manually and place in current folder")
        sys.exit()

        


in_folder = sys.argv[1]


out_pdf = in_folder +  ".pdf"

print("Converting tif to PDF")
tiff2pdf_command = "img2pdf  " + in_folder + "/*.tif -o " + out_pdf
print(tiff2pdf_command)
os.system(tiff2pdf_command)

time.sleep(2)

print("Adding OCR layer")
add_ocr_layer = "ocrmypdf -l tam+eng  --output-type pdfa-3 " + out_pdf + " " + in_folder + "_a.pdf"
print(add_ocr_layer)
os.system(add_ocr_layer)
time.sleep(2)


print("Adding watermark")
add_watermark = './markpdf_linux-amd64  ' + in_folder + "_a.pdf 'Digitized by Roja Muthiah Research Library, Chennai' "  + in_folder   + '_b.pdf  -x -60 -y -60'
print(add_watermark)
os.system(add_watermark)
time.sleep(2)

print("Shrinking PDF")
shrink_pdf = "/bin/bash shrink-pdf.sh " + in_folder + "_b.pdf " + in_folder + "_small.pdf"
print(shrink_pdf)
os.system(shrink_pdf)
time.sleep(2)


print("Done!")
print("Check the pdf " + in_folder +"_small.pdf")





'''
ocrmypdf -l tam+eng  --output-type pdfa-3 --jbig2-lossy -O 3 138.pdf 1-3.pdf


./markpdf_linux-amd64  "./138_a.pdf" "Digitized by Roja Muthiah Research Library, Chennai" "./138_b.pdf" -x -40 -y -60


gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf

sh shrink-pdf.sh 1-3.pdf te-2.pdf


https://www.digitalocean.com/community/tutorials/reduce-pdf-file-size-in-linux

https://www.cyberciti.biz/faq/linux-shell-script-to-reduce-pdf-file-size/
'''
