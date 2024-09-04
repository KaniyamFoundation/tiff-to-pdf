
import os
import sys
import time

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
