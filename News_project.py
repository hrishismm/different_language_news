#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:23:40 2020

@author: hrishi
"""

from bs4 import BeautifulSoup
import requests
import time
import codecs

#Prints current time
def currenttime():
    t=time.localtime()
    c_time=time.strftime("%H:%M:%S",t)
    print("Current Time is"+" "+c_time)

#Scaping code for each site
def abpnews():
    currenttime()
    news_site_link="https://www.abplive.com/latest-news-in-hindi"
    res=requests.get(news_site_link)
    bs4=BeautifulSoup(res.content.decode('utf-8','ignore'),features="lxml")
    list1=bs4.find_all("div",{"class":"uk-width-3-5"}) 
    b=1
    for a in list1[:10]:
        print(b,")",a.get_text())
        b+=1
def republicbharat():
    currenttime()
    news_site_link="https://bharat.republicworld.com/livetv"
    res=requests.get(news_site_link)
    bs4=BeautifulSoup(res.content.decode('utf-8','ignore'),features="lxml")
    list1=bs4.find_all("div",{"class":"texthover font16 lineHeight21px fontweight500 txtTruncate lineClip3"}) 
    b=1
    for a in list1:
        print(b,")",a.get_text())
        b+=1
def abpmajha():
    currenttime()
    news_site_link="https://marathi.abplive.com/"
    res=requests.get(news_site_link)
    bs4=BeautifulSoup(res.content.decode('utf-8','ignore'),features="lxml")
    list1=bs4.find_all("h3",{"class":"uk-margin-remove fz20 uk-text-bold"}) 
    b=1
    for a in list1[:10]:
        print(b,")",a.get_text())
        b+=1
def ibnlokmat():
    currenttime()
    news_site_link="https://lokmat.news18.com/"
    res=requests.get(news_site_link)
    bs4=BeautifulSoup(res.content.decode('utf-8','ignore'),features="lxml")
    list1=bs4.find_all("a",{"class":"events_ana"}) 
    b=1
    for a in list1[:10]:
        print(b,")",a.get_text())
        b+=1
def ndtv():
    currenttime()
    news_site_link="https://www.ndtv.com/"
    res=requests.get(news_site_link)
    bs4=BeautifulSoup(res.content.decode('utf-8','ignore'),features="lxml")
    list1=bs4.find_all("a",{"class":"item-title"}) 
    b=1
    for a in list1[:10]:
        print(b,")",a.get_text())
        b+=1
def opindia():
    currenttime()
    news_site_link="https://www.ndtv.com/"
    res=requests.get(news_site_link)
    bs4=BeautifulSoup(res.content.decode('utf-8','ignore'),features="lxml")
    list1=bs4.find_all("a") 
    b=1
    for a in list1[50:80]:
        if(a.get_text()==""):
            continue
        print(b,")",a.get_text())
        b+=1

#to choose desired news channel    
def hindi():
    n_choice=int(input("Enter your newschannel choice:\n 1:ABP News\n 2)Republic Bharat\n"))
    if(n_choice==1):
        abpnews()   
    elif(n_choice==2):
        republicbharat()
    else:
        print("Invalid Choice")
def marathi():
    n_choice=int(input("Enter your newschannel choice:\n 1:ABP Majha\n 2)IBN Lokmat\n"))
    if(n_choice==1):
        abpmajha()   
    elif(n_choice==2):
        ibnlokmat()
    else:
        print("Invalid Choice")

def english():
    n_choice=int(input("Enter your newschannel choice:\n 1:NDTV\n 2)OpIndia\n"))
    if(n_choice==1):
        ndtv()   
    elif(n_choice==2):
        opindia()
    else:
        print("Invalid Choice")

#To choose your desired language
choice=int(input("Choose your Language:\n 1:Hindi\n 2:Marathi\n 3:English\n"))
if(choice==1):
    hindi()   
elif(choice==2):
    marathi()
elif(choice==3):
    english()
else:
    print("Invalid Choice")

