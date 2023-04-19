# pip install pypdf2
from PyPDF2 import PdfReader

reader = PdfReader("first2.pdf")
number_of_pages = len(reader.pages)
print(number_of_pages)