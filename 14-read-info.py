'get invoice, date and customer pin for x1 customer'
import pypdf
import re
reader = pypdf.PdfReader('Invoice390.pdf')

for page in reader.pages:
    #print(page.extract_text())
    txt = page.extract_text()
    customer_pin = re.findall(r"PIN\sNo.\s(\w\d+\w)", txt)
    print("Customer Pin:{}".format(customer_pin[0]))