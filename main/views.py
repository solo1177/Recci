from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .python.code import *
from .python.driver import *
from .models import *
from .python.code.forms import *
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin  

# Create your views here.
def index(req):
    return render(req, 'main/index.html')
def Top(req):
    return render(req,'main/Top.html')
def foodindex(req):
    return render(req,'main/foodindex.html')
def foodwisdom(req):
    if 'text1'in req.GET:
        a=req.GET['text1']
        if not a:
            msg="空白やめてくださいよ"
            paramas={
                'Title':msg,
            }
            return render(req,'main/foodwisdom.html',paramas) 

        r = requests.get("https://www.yasainavi.com/zukan/")
        soup = BeautifulSoup(r.content, "html.parser")

        #textで正規表現でほしいデータを抽出
    
        link=soup.find_all("a", text=re.compile(a))
        res=[]
        url=[]
        if link==[]:
            msg="ありません。カタカナ|漢字でtryしてみてください。"
            paramas={
                'Title':msg,
            }
            return render(req,'main/foodwisdom.html',paramas) 


        for i in range(0,len(link)):
            res.append(link[i].get('href'))
        for i in range(0,len(res)):
            q=requests.get("https://www.yasainavi.com/"+res[i])
            print(q.url)
            url=q.url
        paramas  ={
            'url': url,

        }
        return render(req,'main/foodwisdom.html',paramas) 
    if 'text2' in req.GET:
        a = req.GET['text2']
        if not a:
            msg="空白やめてくださいよ"
            paramas={
                'Title':msg,
            }
            return render(req,'main/foodwisdom.html',paramas) 

        r = requests.get("https://www.yasainavi.com/column/")
        soup = BeautifulSoup(r.content, "html.parser")

        #textで正規表現でほしいデータを抽出
        
        link=soup.find_all("a", text=re.compile(a))
        res=[]
        url=[]
        if link==[]:
            msg="ありません。カタカナ|漢字でtryしてみてください。"
            paramas={
                'Title':msg,
            }
            return render(req,'main/foodwisdom.html',paramas) 


        
        for i in range(0,len(link)):
            res.append(link[i].get('href'))
        for i in range(0,len(res)):
            q=requests.get("https://www.yasainavi.com/"+res[i])
            print(q.url)
            url=q.url
        paramas ={
            'url': url,

        }

        return render(req,'main/foodwisdom.html',paramas) 

    return render(req,'main/foodwisdom.html') 

def recipe(req):
    if (req.method == 'POST'):
        test = req.POST['text']

    
        url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&applicationId=1010512519693442205&categoryType=small&formatVersion=2'
        api_data = requests.get(url).json()
        api_data.values()
        for menu in api_data["result"]:
            print(menu)
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
            menu_imageurl = menu['foodImageUrl']
            menu_image = menu['recipeMaterial']
            menu_time = menu['recipeIndication']
            menu_cost = menu['recipeCost']
            menu_description = menu['recipeDescription']

            t=Recipe(title=menu_title,url=menu_url,image_url=menu_imageurl,image=menu_image,time=menu_time,cost=menu_cost,description=menu_description)
            t.save()
 

        return redirect(to="/food_rank")     
    return render(req,'main/recipe.html') 

def ocr(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = Document.objects.all()
            print(Document.objects.values('photo'))

            return redirect (to='/detailbook')
    else:
        form = DocumentForm()
        

    return render(request, 'main/ocr.html', {
        'form': form,
      
    })
    



def index_top(req):
    data=User.objects.all()
    paramas = {
        'data':data,
    }
    
    return render(req,'main/index_top.html',paramas) 


def create_index(req):
    
    if(req.method == 'POST'):
        obj = User()
        user = IndexForm(req.POST,instance=obj)
        user.save()
        return redirect(to='/find_index')
    name=req.user
    initial={
        'user':name,
    }
    form=IndexForm(req.POST or None, initial=initial)
    paramas = {
        'form':form,
    }
    return render(req,'main/create_index.html',paramas) 


def edit_index(req,num):
    obj = User.objects.get(id=num)
    if(req.method == 'POST'):
        user = IndexForm(req.POST,instance=obj)
        user.save()
        return redirect(to='/find_index')
    paramas = {
        'id':num,
        'form':IndexForm(instance=obj),
    }
    return render(req,'main/edit_index.html',paramas) 


def delete_index(req,num):
    user = User.objects.get(id=num)
    if(req.method == 'POST'):
        user.delete()
        return redirect(to='/find_index')
    paramas = {
        'id':num,
        'obj':user,
    }
    return render(req,'main/delete_index.html',paramas) 

def find_index(req):
    user=req.user
    


    if(req.method == 'POST'):
        form = FindIndex(req.POST)
        find = req.POST['find']
        data = User.objects.filter(name__contains=find,user__contains=user)
        msg = 'Result:'+str(data.count())
    else:
        msg ='search words...'
        form = FindIndex()
        data = User.objects.filter(user__contains=user)


        
        
    paramas = {
        'message':msg,
        'form':form,
        'all':data,
        
    }

    return render(req,'main/find_index.html',paramas) 

def food_rank(req):
    obj=Recipe.objects.all().order_by("id").reverse()[:4]
       
    paramas = {
        "all":obj,
        }   
    return render(req,"main/food_rank.html",paramas)





# coding:utf-8
#レシピ提案完成
import csv
import pprint
import requests
from collections import defaultdict
import os
import re


def detail_recipe(req,num):
    obj = Recipe.objects.get(id=num)
    paramas={
        "obj":obj,
    }
      

    return render(req,'main/detail_recipe.html',paramas) 

        

# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import csv

    



module_dir = os.path.dirname(__file__)
json_path = os.path.join(module_dir, './python/driver/poised-tenure-286203-8ad31de3b8ee.json')

image_path =os.path.join(module_dir, '../media')
food_pass = os.path.join(module_dir, './python/driver/food_list.txt')
def detailbook(req):
    obj = Document.objects.latest('id')
    res=str(obj.photo)
    pas=image_path + "/" + res
    
    #各種インポート
    import io 
    import os
    from google.protobuf.json_format import MessageToJson
    import json
    from google.cloud import vision_v1
    #from google.cloud.vision import types


    #サービスアカウントキーへのパスを通す
 
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_path
    #visionクライアントの初期化
    client = vision_v1.ImageAnnotatorClient()

    #対象となる画像のファイル名
    file_name = pas

    
    #画像を読み込み
    try:
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = vision_v1.types.Image(content=content)
    except FileNotFoundError:
        msg="空白は、だめですよ！"
        form = DocumentForm()
        paramas={
            'Title':msg,
            'form': form,
        }
        return render(req,'main/ocr.html',paramas) 

    response = client.text_detection(image=image)
    #最初のtextのまとめが[0]に格納されている。
    texts = response.text_annotations[0]
    #print('Texts:')


    #print('\n"{}"'.format(texts.description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    #検索
    f = open(food_pass, encoding='CP932')
    data1 = f.read()
    lines = data1.split('\n')
    f.close()

    text=texts.description
    tex=text.split('\n')

    # レシートから読み込んだ文字列を表示
    search_words = []
    for word in lines:
        for receipt in tex:
            if word in receipt:
                #空行削除
                if word !='':
                    search_words.append(word)
                #print("True")


    paramas={
        'obj':res,
        'item':search_words,

    }
    if req.method == 'POST':
        msg=req.POST.getlist('text')
        print(msg)

        par={
            'msg':msg,

        }
        return render(req, 'main/create_index2.html', par)



    return render(req, 'main/detailbook.html', paramas)
    

def create_index2(req):

    name=req.user
    
    msg = req.POST['text']
    item=IndexForm(initial={'name':msg})
    paramas = {
        'form':item,
    }
    req.POST.update()

    if(req.method == 'POST'):
        if(req.POST['text']):
            msg = req.POST['text']
            item=IndexForm(initial={'name':msg,'user':name})
            paramas = {
                    'form':item,
                    'name':name,
            }
            return render(req,'main/create_index2.html',paramas)
    obj = User()
    user = IndexForm(req.POST,instance=obj)
    user.save()
    return redirect(to='/find_index')
   


    
