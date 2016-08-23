import os
import glob
 
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
 
def convert_pdf(path):
 
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    laparams.all_texts = True
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
 
    fp = file(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
 
    str = retstr.getvalue()
    retstr.close()
    return str
 
pdflist = glob.glob("*.pdf")
textName = pdf + ".txt"
for pdf in pdflist:
    print("Working on: " + pdf + '\n')
    fout = open(textName,'a')
    fout.write(convert_pdf(pdf))
    fout.close()