# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import random

ip_port_list={}
#获取ip网站的  ip：端口号 字典
def ip_port(url):
    headers=headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    html=requests.get(url,headers=headers)
    obj=BeautifulSoup(html.text,"html.parser")
    lable1=obj.find("table",{"id":"ip_list"}).find_all("tr")
    for i in range(1,len(lable1)):
        ip_port_list[lable1[i].find_all("td")[1].get_text()+":"+lable1[i].find_all("td")[2].get_text()]=lable1[i].find_all("td")[5].get_text().lower()
    return ip_port_list

#返回一个proxies字典
def get_proxies(ip_port_list):
    temp=random.choice(list(ip_port_list.keys()))
    temp1=ip_port_list[temp]
    if temp1=="https":
        temp2="https://"+temp
        proxies={"https":temp2}       
    elif temp1=="http":
        temp2="http://"+temp
        proxies={"https":temp2}
    return proxies

headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
while True:
    try:
        html=requests.get("https://www.ipip.net/", headers=headers,proxies=get_proxies(ip_port("http://www.xicidaili.com/nn/")))
        if html.status_code==200:
            content=html.text    
            html=etree.HTML(content)    
            ip=html.xpath('//ul[@class="inner"]/li[1]/text()')[0]
            print("当前请求IP地址为："+ip)
            break
    except:
        print("不行啊")
            
    








