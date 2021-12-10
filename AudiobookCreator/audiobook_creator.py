import pyttsx3
import PyPDF2

book = open("The Compound Effect - Darren hardy ( PDFDrive.com ).pdf",'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

speaker = pyttsx3.init()
page = pdfreader.getPage(5)
text = page.extractText()

speaker.say(text)
speaker.runAndWait()
print(pages)
