# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:14:25 2018

@author: ASUS
"""
import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
import re
import os
import pickle
'''
jpg=set()

url="http://jandan.net/ooxx/page-1#comments"
def geturl(url):
    headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, cko) Chromlike Gee/54.0.2840.87 Safari/537.36"}
    driver = webdriver.PhantomJS()
    driver.get(url)
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource,"html.parser")
    for i in bsObj.findAll("img"):
        jpg.add(i.attrs["src"])
    driver.quit()

for i in range(1,48):
    try:
        url="http://jandan.net/ooxx/page-{}#comments".format(str(i))
        geturl(url)
        print(len(jpg))
    except:
        print("第{}页没下载".format(str(i)))
'''
jpg=pickle.load(open("C:\\Users\\ASUS\\Desktop\\python代码库\\煎蛋网图片\\url集合.txt","rb"))
jpg1=list(jpg)
try:
    os.makedirs("C:\\Users\\ASUS\\Desktop\\python代码库\\煎蛋网图片\\煎蛋网图片")
except:
    mkdir="C:\\Users\\ASUS\\Desktop\\python代码库\\煎蛋网图片\\煎蛋网图片"
finally:
    mkdir="C:\\Users\\ASUS\\Desktop\\python代码库\\煎蛋网图片\\煎蛋网图片"

for i in jpg1:
    try:
        html=requests.get(i)
        with open(mkdir+"\\"+i.split("/")[-1],"wb") as f:
            f.write(html.content)
    except:
        print("这张图没下载哦！")

        
