import re
import string
import random
import jieba
#文本text获取
f=open("C:\\Users\\ASUS\\Desktop\\马尔可夫str.txt","r")
text=f.read()
f.close()

#文本text清洗
def cleantext(input):
    input=re.sub("\s","",input)
    input=re.sub(r'[{}]'.format(string.punctuation),"",input)
    input=re.sub("[；：，。·！（）]","",input)
    return input

#分割text变成列表
text_list=jieba.lcut(cleantext(text))


#生成马尔可夫字典
dict1={}
def generate_dict(input):
    for j,i in enumerate(input):
        if j==len(text_list)-1:
            break
        if i not in dict1:
            dict1[i]={}
            dict1[i][input[j+1]]=0
        if i in dict1:
            if input[j+1] not in dict1[i]:
                dict1[i][input[j+1]]=0
            if input[j+1] in dict1[i]:
                dict1[i][input[j+1]]+=1
    return dict1

#根据权重随机获取文字
def list_method(dict1,chain_temp):
    all_data = []
    for v, w in dict1[chain_temp].items():
        temp = []
        for i in range(w):
            temp.append(v)
        all_data.extend(temp)
        
    n = random.randint(0,len(all_data)-1)
    return all_data[n]

#得到chain
def chain_end(chain,lenth):
    chain_temp=chain
    for i in range(lenth):
        chain+=list_method(generate_dict(text_list),chain_temp)
        chain_temp=list_method(generate_dict(text_list),chain_temp)
    print(chain)

x=input("请输入一个文字：")
y=eval(input("再输入一个数字："))
chain_end(x,y)


