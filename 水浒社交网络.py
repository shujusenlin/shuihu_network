# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 08:23:10 2018

@author: dell
"""

import os
import pandas as pd
import jgraph as ig

os.chdir('D:/爬虫/水浒传')

with open("水浒传全文.txt", encoding='gb18030') as file:
    shuihu = file.read()

shuihu = shuihu.replace('\n','')
shuihu_set = shuihu.split(' ')
shuihu_set=[k for k in shuihu_set if k!='']

songjiang_set=[k for k in shuihu_set if '宋江' in k]
haohan = pd.read_excel('水浒人物.xlsx')
haohan['出场段落']=0
for i in range(0,108):
    haohan['出场段落'][i] = len([k for k in shuihu_set if haohan['使用名'][i] in k])

net_df = pd.DataFrame(columns=['排名高姓名','排名低姓名','权重'])
for i in range(0,107):
    for j in range(i+1,108):
        this_weight = len([k for k in shuihu_set if haohan['使用名'][i] in k and haohan['使用名'][j] in k])
        net_df=net_df.append({'排名高姓名':haohan['姓名'][i],'排名低姓名':haohan['姓名'][j],
                              '权重':this_weight},ignore_index=True)
        print(str(i)+':'+str(j))