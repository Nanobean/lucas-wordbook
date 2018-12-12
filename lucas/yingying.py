# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:50:09 2018

@author: 73902
"""
import os
import urllib
from bs4 import BeautifulSoup
import re
import nltk
import nltk.data
import pandas as pd
import numpy as np
import time


                  
def de(out):
    return out.replace('<',' ')  
def wr(collins):
    pattern=re.compile('<span class="def">.*<')
    match=pattern.search(str(collins))
    if match:
        
        output=str(match.group(0))
        return output.replace('<span class="def">',' ')  
    else:
        return ''

def wo(collins):
    patternwor=re.compile('<span class="pos">.*<')
    match=patternwor.search(str(collins))
    if match:
        outputword=str(match.group(0))
        return outputword.replace('<span class="pos">',' ')
    else:        
        
        return ''

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
def tranee(word):
    soup=BeautifulSoup(urllib.request.urlopen(urlf(word)).read())
#    print (soup.prettify())

    right=("→")
    right=right.encode('utf-8')
	# To find all "collinsOrder" and "examples"
    collins=str(soup.find_all(id='tEETrans'))
    collins=collins.replace('<b>',' ')
    collins=collins.replace('<//b>',' ')
    collins=BeautifulSoup(collins)
    out=str(wo(collins))+str(wr(collins))
 #   out=str(wr(collins))
    docsee.append(de(out))
    time.sleep(0.3)
          
    
    

os.chdir('D:\lucas')
df=pd.read_excel('day.xlsx')
wor=df['Word']
docsee=[]
for i in range(len(wor)):
    tranee(wor[i])
#    tran(wor[i])
    print(i)

dateee=pd.DataFrame(docsee)

file3= pd.ExcelWriter('file3.xlsx')
dateee.to_excel(file3,'page_1',float_format='%.5f')
file3.save()
