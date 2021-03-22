import itchat
import matplotlib.pyplot as plt
import pandas as pd
def get_head():
    itchat.login()
    friends=itchat.get_friends()
    for count, f in enumerate(friends):
            # 根据userName获取头像
            img = itchat.get_head_img(userName=f["UserName"])
            x="C:/Users/ASUS/Desktop/新建文件夹/"+str(count)+".jpg"
            imgFile = open(x,"wb")
            imgFile.write(img)
            imgFile.close()


dddd
def getSex():
    itchat.login()
    friends = itchat.get_friends(update=True)
    sex = dict()
    for f in friends:
        if f["Sex"] == 1: #男
            sex["man"] = sex.get("man", 0) + 1
        elif f["Sex"] == 2: #女
            sex["women"] = sex.get("women", 0) + 1
        else: #未知
            sex["unknown"] = sex.get("unknown", 0) + 1
    # 柱状图展示
    for i, key in enumerate(sex):
        plt.bar(key, sex[key])
    plt.show()


itchat.login()
friends = itchat.get_friends(update=True)
df_friends = pd.DataFrame(friends)
