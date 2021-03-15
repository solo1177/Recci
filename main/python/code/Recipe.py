# coding:utf-8
#レシピ提案完成
import csv
import pprint
import requests
from collections import defaultdict
import os
def Recipe(req):
    test=req
    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&applicationId=1010512519693442205&categoryType=small&formatVersion=2 '
    api_data = requests.get(url).json()

    api_data.values()

    print("result" in api_data )

    for menu in api_data["result"]:
        print(menu)

    print(type(api_data["result"]["small"]))


    small_list=api_data["result"]["small"]

    res=[]


    # if 検索したい食材ワード
    for i in small_list:
        if test in  i["categoryName"]:
            res.append(list((i.items())))

            

    URL=""
    for i in range(len(res)):
        for j in range(0,4):
            print (res[i][j])
            if(res[i][3]):
                URL=res[i][j][1]
        
    import re

    URLS=""
    URLS=re.search(r'[0-9]+-+[0-9]+-+[0-9]+', URL)
    re=URLS.group()
    re

    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId=1010512519693442205&categoryId='+re
    api_data = requests.get(url).json()
    for menu in api_data['result']:
        menu_title = menu['recipeTitle']
        menu_url = menu['recipeUrl'] 
        menu_image = menu['recipeMaterial']
        menu_description = menu['recipeDescription']

    print('【' + menu_title + '】')
    print(menu_url)
    print(menu_image)
    print(menu_description)
