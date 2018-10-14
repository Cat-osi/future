import re
f=open("C:\\Users\\ASUS\\AppData\Local\\Temp\\论语-网络版.txt",encoding='utf-8',errors='ignore')
text=f.readlines()
f.close()
newlist=[]
for i in text:
    if i!="\n":
        i=i.strip(" ")
        i=re.sub("\d*·\d*","",i)
        i=re.sub("\(\d*\)","",i)
        newlist.append(i)
f=open("C:\\Users\\ASUS\\AppData\Local\\Temp\\论语-原文.txt","w+",encoding='utf-8',errors='ignore')
f.writelines(newlist)
f.close()
        


        
    
