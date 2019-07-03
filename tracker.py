import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.de/Canon-Foto%C4%9Fraf-Makinesi-Megapiksel-Ekran-Schwarz/dp/B01L8U5924/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2QIBX069RVRU8&keywords=canon+5d+mark+iv&qid=1562182791&s=gateway&sprefix=canon+5d%2Caps%2C163&sr=8-1';

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 2.500):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sobhanniroula2012@gmail.com', 'nztvwvyykbgguwlz')

    subject = 'Hey! The price has dropped down!!'
    body = 'Check the Amazon link https://www.amazon.de/Canon-Foto%C4%9Fraf-Makinesi-Megapiksel-Ekran-Schwarz/dp/B01L8U5924/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2QIBX069RVRU8&keywords=canon+5d+mark+iv&qid=1562182791&s=gateway&sprefix=canon+5d%2Caps%2C163&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sobhanniroula2012@gmail.com',
        'sobhan_niroula@yahoo.com',
        msg
    )
    print('Email has been sent')
    server.quit()


while(True):
    check_price()
    time.sleep(86400)