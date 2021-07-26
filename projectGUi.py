# module for GUI
import tkinter as tk
from tkinter.constants import CENTER, COMMAND, FALSE, LEFT, RIGHT, TOP, X
from tkinter import *  
from PIL import ImageTk,Image 


# modules for main functions
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import pywhatkit as whatsApp
from datetime import datetime


def amazon_fun(URL, priceFall, email):
    # URL = input("GIVE THE URL OF THE PRODUCT "

    # now = datetime.now()
    # x = 1
    # send_time_minute = 0
    # send_time_hr = int(now.strftime("%H"))
    # send_time_minute = int(now.strftime("%M"))+2
    A = True

    headers = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7. 10 Chrome/47.0. 2526.110 Brave/0.36. 5 Safari/537.36.'}

    def convert_price(s):
        l = []
        for c in s:
            if(c >= '0' and c <= '9'):
                l.append(c)
        return float(''.join(l))

    def send_Email():
        # whatsApp.sendwhatmsg("+91"+phone,"URL",send_time_hr,send_time_minute)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("akshaybargaje56@gmail.com", "ylnnzrnzgslpxqrp")

        subject = "price fell down"
        body = URL
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(  # for sending email
            "akshaybargaje56@gmail.com",
            email,
            msg
        )

        server.quit()

    while(A == True):
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id="productTitle").get_text()
        price = soup.find(id="priceblock_dealprice").get_text()
        converted_price = convert_price(price)

        if converted_price > priceFall:
            send_Email()
            A = FALSE
        # time.sleep(3600*24)     #in seconds here we are checking once a day


def flipcart_fun(URL, priceFall, email):
    # URL = input("GIVE THE URL OF THE PRODUCT "

    # now = datetime.now()
    # x = 1
    # send_time_minute = 0
    # send_time_hr = int(now.strftime("%H"))
    # send_time_minute = int(now.strftime("%M"))+2
    status = True

    headers = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7. 10 Chrome/47.0. 2526.110 Brave/0.36. 5 Safari/537.36.'}

    def convert_price(s):
        l = []
        for c in s:
            if(c >= '0' and c <= '9'):
                l.append(c)
        return float(''.join(l))

    def send_mail(URL):
        # whatsApp.sendwhatmsg("+91"+phone,"URL",send_time_hr,send_time_minute)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('nayan.bari20@vit.edu', 'kggpowquhwocdlxe')
        subject = 'Price fell down!'
        body = URL
        msg = f'Subject: {subject} \n\n {body}'
        server.sendmail('nayan.bari20@gmail.com', email, msg)
        server.quit()

    while(status == True):
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(class_="B_NuCI").get_text()
        price = soup.find(class_="_30jeq3").get_text()

        converted_price = convert_price(price)

        if converted_price > priceFall:
            send_mail()
            status = FALSE


def Lenskart_fun(URL, priceFall, email):
    # URL = input("GIVE THE URL OF THE PRODUCT "

    # now = datetime.now()
    # x = 1
    # send_time_minute = 0
    # send_time_hr = int(now.strftime("%H"))
    # send_time_minute = int(now.strftime("%M"))+2
    status = True

    headers = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7. 10 Chrome/47.0. 2526.110 Brave/0.36. 5 Safari/537.36.'}

    def convert_price(s):
        l = []
        for c in s:
            if(c >= '0' and c <= '9'):
                l.append(c)
        return float(''.join(l))

    def send_mail(URL):
        # whatsApp.sendwhatmsg("+91"+phone,"URL",send_time_hr,send_time_minute)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('nayan.bari20@vit.edu', 'kggpowquhwocdlxe')
        subject = 'Price fell down!'
        body = URL
        msg = f'Subject: {subject} \n\n {body}'
        server.sendmail('nayan.bari20@gmail.com', email, msg)
        server.quit()

    while(status == True):
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(class_="capitalize fs16 padding-t10 padding-b10 product-fullName").get_text()
        price = soup.find(class_="price fs22 color-green nowrap fw-bold").get_text()

        converted_price = convert_price(price)

        if converted_price > priceFall:
            send_mail()
            status = FALSE



def Ajio_fun(URL, priceFall, email): 
    # URL = input("GIVE THE URL OF THE PRODUCT "

    # now = datetime.now()
    # x = 1
    # send_time_minute = 0
    # send_time_hr = int(now.strftime("%H"))
    # send_time_minute = int(now.strftime("%M"))+2
    status = True

    headers = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7. 10 Chrome/47.0. 2526.110 Brave/0.36. 5 Safari/537.36.'}

    def convert_price(s):
        l = []
        for c in s:
            if(c >= '0' and c <= '9'):
                l.append(c)
        return float(''.join(l))

    def send_mail(URL):
        #whatsApp.sendwhatmsg("9309590522","url",send_time_hr,send_time_minute)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("prem.baravkar20@vit.edu", "iyqlpjiavxennhdi")
    
        subject = 'Price fail down!'
        body =  URL
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            "prem.baravkar20@vit.edu",
            email,
            msg
        )
        server.quit()

    while(status == True):
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(class_="proud-name").get_text()
        price= soup.find(class_= "proud-sp").get_text()
        converted_price = convert_price(price)
        if converted_price > priceFall:
            send_mail()
            status = FALSE

    

def Ebay_fun(URL, priceFall, email):
    # URL = input("GIVE THE URL OF THE PRODUCT "

    # now = datetime.now()
    # x = 1
    # send_time_minute = 0
    # send_time_hr = int(now.strftime("%H"))
    # send_time_minute = int(now.strftime("%M"))+2
    status = True

    headers = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7. 10 Chrome/47.0. 2526.110 Brave/0.36. 5 Safari/537.36.'}

    def convert_price(s):
        l = []
        for c in s:
            if(c >= '0' and c <= '9'):
                l.append(c)
        return float(''.join(l))

    def send_mail(URL):
        # whatsApp.sendwhatmsg("+91"+phone,"URL",send_time_hr,send_time_minute)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("prem.baravkar20@vit.edu", "iyqlpjiavxennhdi")
        subject = 'Price fell down!'
        body = URL
        msg = f'Subject: {subject} \n\n {body}'
        server.sendmail("prem.baravkar20@vit.edu", email, msg)
        server.quit()

    while(status == True):
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id="itemTitle").get_text()
        price = soup.find(id="mm-saleDscPrc").get_text()

        converted_price = convert_price(price)

        if converted_price > priceFall:
            send_mail()
            status = FALSE



def SnapDeal_fun(URL, priceFall, email):
    # URL = input("GIVE THE URL OF THE PRODUCT "

    # now = datetime.now()
    # x = 1
    # send_time_minute = 0
    # send_time_hr = int(now.strftime("%H"))
    # send_time_minute = int(now.strftime("%M"))+2
    status = True

    headers = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/0.7. 10 Chrome/47.0. 2526.110 Brave/0.36. 5 Safari/537.36.'}

    def convert_price(s):
        l = []
        for c in s:
            if(c >= '0' and c <= '9'):
                l.append(c)
        return float(''.join(l))

    def send_mail(URL):
        # whatsApp.sendwhatmsg("+91"+phone,"URL",send_time_hr,send_time_minute)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('ishwari.baranjalekar20@vit.edu', 'cazsulolwxavpall')
        subject = 'Price fell down!'
        body = URL
        msg = f'Subject: {subject} \n\n {body}'
        server.sendmail('ishwari.baranjalekar20@vit.edu', email, msg)
        server.quit()

    while(status == True):
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(class_="pdp-e-i-head").get_text().strip()
        price = soup.find(class_="payBlkBig").get_text()
        converted_price = convert_price(price)

        if converted_price > priceFall:
            send_mail()
            status = FALSE


#               This is used for switching frames             #
A = False
E = False
F = False
AJ = False
LN = False
SN = False


def Amazon():
    general_frame.grid()
    main_frame.grid_forget()
    global A
    A = True
    heading.config(text="Amazon")


def Flipcart():
    general_frame.grid()
    main_frame.grid_forget()
    global F
    F = True
    heading.config(text="FlipCart")


def Ebay(): 
    general_frame.grid()
    main_frame.grid_forget()
    global E
    E = True
    heading.config(text="Ebay")


def Ajio():
    general_frame.grid()
    main_frame.grid_forget()
    global AJ
    AJ = True
    heading.config(text="Ajio")


def Lenskart():
    general_frame.grid()
    main_frame.grid_forget()
    global LN
    LN = True
    heading.config(text="Lenskart")


def SnapDeal():
    general_frame.grid()
    main_frame.grid_forget()
    global SN
    SN = True
    heading.config(text="SnapDeal")


#                       This is the GUI part                  #
main_window = tk.Tk(className=" NOTIFIER")
main_window.config(bg="#3D3D3D")
main_window.geometry('960x570')


main_frame = tk.Frame(master=main_window, borderwidth=2, bg="#333333")
main_frame.grid(padx=35, pady=35)

general_frame = tk.Frame(master=main_window, borderwidth=2, bg="#3D3D3D")
general_frame.grid(padx=35, pady=35)
general_frame.grid_forget()


Amazon_img = ImageTk.PhotoImage(Image.open('img//Amazon.jpg'))
Flipcart_img = ImageTk.PhotoImage(Image.open('img//flipkart.png')) 
Ebay_img = ImageTk.PhotoImage(Image.open('img//ebay.png'))    
Ajio_img = ImageTk.PhotoImage(Image.open('img//AJIO.jpg'))
lenskart_img = ImageTk.PhotoImage(Image.open('img//lenskat.jpg'))
snapDeal_img = ImageTk.PhotoImage(Image.open('img//snapdeal.png'))
    


Amazon_button = tk.Button(master=main_frame, command=Amazon,image=Amazon_img ,height=100,width=150)
Amazon_button.grid(row=0, column=1, sticky="nw", padx=70, pady=70)


Flipcart_button = tk.Button(
    master=main_frame, command=Flipcart,image=Flipcart_img,height=100,width=150)
Flipcart_button.grid(row=0, column=21, sticky="n", padx=70, pady=70)

Ebay_button = tk.Button(master=main_frame, command=Ebay,image=Ebay_img,height=100,width=150)
Ebay_button.grid(row=0, column=41, sticky="ne", padx=70, pady=70)

Ajio_button = tk.Button(master=main_frame, command=Ajio,image=Ajio_img,height=100,width=150)
Ajio_button.grid(row=5, column=1, sticky="se", padx=70, pady=70)

lenskart_button = tk.Button(
    master=main_frame, command=Lenskart,image=lenskart_img,height=100,width=150)
lenskart_button.grid(row=5, column=21, sticky="s", padx=70, pady=70)

snapDeal_button = tk.Button(
    master=main_frame, command=SnapDeal,image=snapDeal_img,height=100,width=150)
snapDeal_button.grid(row=5, column=41, sticky="sw", padx=70, pady=70)


def Done():
    global A
    print(A)
    try:
        lbl.config(text="PROGRAMME IS RUNNING.......")
        URL = Url_txt.get()
        FallPrice = float(price_Fall.get())
    #   phone = phone_no.get()
        email = email_text.get()
        if bool(A):
            amazon_fun(URL, FallPrice, email)
        elif bool(F):
            flipcart_fun(URL, FallPrice, email)
        # elif bool(E):
        #     Ebay_fun(URL, FallPrice, email)
        # elif bool(AJ):
        #     Ajio_fun(URL, FallPrice, email)
        # elif bool(LN):
        #     lenskart_fun(URL, FallPrice, email)
        elif bool(SN):
            SnapDeal_fun(URL, FallPrice, email)

        lbl.config(text="message sent")
    except:
        lbl.config(text="please provide Vailid input")


firstclick_URL = True
# firstclick_phone = True
firstclick_Email = True
firstclick_price = True

# def on_entry_click(event):       
#     global firstclick_URL
#     global firstclick_Email
#     global firstclick_price
#     # global firstclick_phone


#     if event == Url_txt: 
#         firstclick_URL = False
#         Url_txt.delete(0, "end") # delete all the text 
#     elif event == price_Fall: 
#         firstclick_Email = False
#         price_Fall.delete(0, "end")
#     elif event == email_text: 
#         firstclick_price = False
#         email_text.delete(0, "end") 
#     # elif firstclick_phone: 
#         # firstclick_phone = False
#         # Url_txt.delete(0, "end") 

# LAble -- text show
# button -- 
# Entry---text input

heading = tk.Label(master=general_frame, text="",font=('beautiful mountain',28),bg="#3D3D3D",fg='White')
heading.grid(row=0,column=0,sticky='n',padx=400,pady=25)
Url_txt = tk.Entry(master=general_frame,bg="#3D3D3D",fg='light grey')
Url_txt.grid(row=1,column=0,sticky='n',padx=400,pady=20)
# Url_txt.insert(0, 'Enter The URl Of Product.')
# Url_txt.bind('<FocusIn>', on_entry_click(Url_txt))

# phone_no = tk.Entry(master=general_frame,show="Enter Your phone Number ")
# phone_no.pack(row=0,column=0,sticky='n',padx=400,pady=10)
# phone_no.insert(0, "Enter The Expected Price Of Product")
# phone_no.bind('<FocusIn>', on_entry_click)

price_Fall = tk.Entry(master=general_frame,bg="#3D3D3D",fg='light grey')
price_Fall.grid(row=2,column=0,sticky='n',padx=400,pady=20)
# price_Fall.insert(0, "Enter The Expected Price Of Product")
# price_Fall.bind('<FocusIn>', on_entry_click(price_Fall))

email_text = tk.Entry(master=general_frame,bg="#3D3D3D",fg='light grey')
email_text.grid(row=3,column=0,sticky='n',padx=400,pady=20)
# email_text.insert(0, "Enter Your Email")
# email_text.bind('<FocusIn>', on_entry_click(email_text))

printButton = tk.Button(master=general_frame,bg="#3D3D3D",fg='white',
                        text="Done",
                        command=Done,font=('beautiful mountain',18))
printButton.grid(row=4,column=0,sticky='n',padx=400,pady=30)


lbl = tk.Label(master=general_frame,bg="#3D3D3D",fg='White')
lbl.grid(row=5,column=0,sticky='n',padx=400,pady=20)



main_window.mainloop()