'get invoice, date and customer pin for x1 customer'
import pypdf
import re
reader = pypdf.PdfReader('Invoice390.pdf')

for page in reader.pages:
    #print(page.extract_text())
    txt = page.extract_text()
    customer_pin = re.findall(r"PIN\sNo.\s(\w\d+\w)", txt)
    invoice_number = re.findall(r"(\s\d{3}\s)", txt)
    date = re.findall(r"\d{2}th\s\w+\s\d{4}", txt)
    print("Customer Pin:{}".format(customer_pin[0]))
    print("Invoice number:{}".format(invoice_number[0]))
    print("Date:{}".format(date[0]))