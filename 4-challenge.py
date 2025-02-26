#!/usr/bin/python3

"""
    we are loking for e, special symbols and numbers 
"""

import re 
paragraph="""The @market opened at 9:00 AM, with stocks rising by 5% in the first #hour. Investors watched as $10,000 turned into $12,500 within 30 minutes! Meanwhile, John checked his email (john_doe123@email.com) and noticed a 50% discount on his favorite gadget—only $199.99 instead of $399.99. Excited, he added it to his cart but forgot his password: P@ssw0rd! He quickly reset it, confirming with a 6-digit code: 274891. As he clicked "Buy Now," his phone buzzed—an urgent message from work: "Meeting rescheduled to 3:45 PM @ HQ. Be there!"
"""
x = re.findall("[0-9]+", paragraph)
print(x)