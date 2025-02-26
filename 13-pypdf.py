'get invoice, date and customer pin for x1 customer'
import pypdf
import re
reader = pypdf.PdfReader('3149.pdf')

for page in reader.pages:
    #print(page.extract_text())
    txt = page.extract_text()
    invoice = re.findall(r"Invoice\s(\d+)", txt)
    date = re.findall(r"\d{2}\s[A-Z][a-z]+\s\d{4}",txt)
    pin = re.findall(r"", txt)
    print("Invoice:{}".format(invoice[0]))
    print("Due date:{}".format(date[0]))