import PyPDF2
import re

# Open the pdf file
object = PyPDF2.PdfFileReader(r"UserManual.pdf")

# Get number of pages
NumPages = object.getNumPages()

# Enter code here
String = "http://www.virtualbox.org"

# Extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    if re.search(String,Text):
         print("Pattern Found on Page: " + str(i))
