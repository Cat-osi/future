import pymysql
import pandas as pd
import numpy as np
db= pymysql.connect(host="localhost",user="root",password="hybaba",db="image_su",use_unicode=True,charset='utf8')
cur=db.cursor()
sql='select * from image_suuz'
data=pd.read_sql(sql,db)

#针对print无法显示所有数据
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


#判断每一列是否为int64 在找出最大值 单个样本提取
for i in data.columns:
    if type(data.ix[5,i])==np.int64:
        print(i,end='   ')
        print(data[data[i].isin([data[i].max()])])
        




