# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:19:16 2018

@au
pip install lxmlthor: 73902
"""
import sys
sys.setdefaultencoding('utf-8')
m=[]
import os
import urllib
from bs4 import BeautifulSoup
import re
import nltk
import nltk.data
import pandas as pd
import numpy as np
import time

def shai(st):
    st=st.replace('[',' ')
    st=st.replace(']',' ')
    st=st.replace('(',' ')
    st=st.replace(')',' ')
    return st
#过滤
def lu(x): 
    p=re.compile(r'[^\x00-\x7f]')
    m=re.sub(p,'',x)
    return(m)


def ss(paragraph):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(paragraph)
    return sentences

def urlf(word):
    return 'http://dict.youdao.com/search?q=' + word + '&keyfrom=dict.index'
def tran(word):
    
    soup=BeautifulSoup(urllib.request.urlopen(urlf(word)).read())
    right=("→")
    right=right.encode('utf-8')
	# To find all "collinsOrder" and "examples"
    collins=str(soup.find_all(id='collinsResult'))
    collins=collins.replace('<b>',' ')
    collins=collins.replace('<//b>',' ')
    collins=BeautifulSoup(collins)
    a=''
    for string in collins.stripped_strings:
		   pattern=re.compile('[\.\?!":]|\[.*\]|\/')
		   match=pattern.search(string)
     
		   if match:
			      a=a+string
    if len(ss(a))>1:
           text=ss(a)[1]
    else:
           text=ss(a)[0]   
    st='例句:'+lu(text)
    st=shai(st)
    docs.append(st)
    print(word)
    time.sleep(0.3)



os.chdir('D:\lucas')
df=pd.read_excel('day.xlsx')
worr=df['Word']
docs=[]
for i in range(len(worr)):
    tran(worr[i])
    print(i)

len(docs)
date=pd.DataFrame(docs)

file2= pd.ExcelWriter('file2.xlsx')
date.to_excel(file2,'page_1',float_format='%.5f')
file2.save()



#输出
xg=pd.read_excel('file2.xlsx')
wor2=xg['word']







newlist=[]
for i in range(len(wor2)):
    
    if wor2[i]==nan:
        break
        
    newlist.append(shai(wor2[i]))
    
    print(i)
pd.DataFrame(newlist)