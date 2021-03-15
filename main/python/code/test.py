# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import os
import csv

#野菜図巻　切り方取得

def get_cut(req):
    r = requests.get("https://www.yasainavi.com/column/")
    soup = BeautifulSoup(r.content, "html.parser")

    #textで正規表現でほしいデータを抽出
    a=req
    link=soup.find_all("a", text=re.compile(a))
    res=[]
    url=[]
    if link==[]:
        print("ありません。カタカナ|漢字でtryしてみてください。")

    
    for i in range(0,len(link)):
        res.append(link[i].get('href'))
    for i in range(0,len(res)):
        q=requests.get("https://www.yasainavi.com/"+res[i])
        print(q.url)
        url=q.url
    return url




#野菜図巻 野菜取得
def get_wisdom(req):
    r = requests.get("https://www.yasainavi.com/zukan/")
    soup = BeautifulSoup(r.content, "html.parser")

    #textで正規表現でほしいデータを抽出
    a=req
    link=soup.find_all("a", text=re.compile(a))
    res=[]
    url=[]
    if link==[]:
        print("ありません。カタカナ|漢字でtryしてみてください。")

    for i in range(0,len(link)):
        res.append(link[i].get('href'))
    for i in range(0,len(res)):
        q=requests.get("https://www.yasainavi.com/"+res[i])
        print(q.url)
        url=q.url
    return url
