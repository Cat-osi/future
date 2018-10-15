from selenium import webdriver
from bs4 import BeautifulSoup
list1=[]


driver=webdriver.PhantomJS()
driver.get("http://www.douyu.com/directory/all")

def list1_append():
    obj=BeautifulSoup(driver.page_source,"html.parser")
    for i in obj.findAll("p"):
        x=i.get_text()
        list1.append(x)


while True:
    try:
        list1_append()
        elem = driver.find_element_by_class_name('shark-pager-next') 
        elem.click()
        if driver.page_source.find('shark-pager-disable-next') != -1:
            break
        
    except:
        continue
