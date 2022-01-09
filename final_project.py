# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:16:05 2022

@author: LIN
"""
import bs4 as bs
import urllib.request
from summarizer.sbert import SBertSummarizer
from tkinter import *
from tkinter import ttk

def bbc_top_stories():
   '''取得title, summary, link'''
   bbc_web = urllib.request.urlopen('http://feeds.bbci.co.uk/news/rss.xml')
   news = bbc_web.read()
   parsed_news = bs.BeautifulSoup(news,'lxml')
   #將連結放進list
   link_list=[]
   for link in parsed_news.find_all('guid'):
       link_list.append(link.text)
    #print(link_list)
   num = 0
   #取得文章
   for link in link_list:
       article = urllib.request.urlopen(link_list[num])
    
       parsed_article = bs.BeautifulSoup(article,'lxml')
            
       #取得標題
       ntitle = parsed_article.find('h1').string
       #print(f'{num+1}. {ntitle}')
       #得到文章內容
       article_text = ""
       paragraphs = parsed_article.find_all('p',class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")
       for paragraph in paragraphs:
           content = paragraph.text
           article_text+=content
       #取得連結   
       l = str(link_list[num])
        
       #利用SBERT取得摘要
       body = article_text
       model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
       #設定輸出的摘要:3句
       result = model(body, num_sentences=3)
       print(result)
       print(l)
       #將得到的結果寫成txt檔
       with open(f'articles_t1_{num+1}.txt', 'w+', encoding="utf-8") as f:
           f.write(f'{ntitle}\n')
           f.write(f'{result}\n')
           f.write(f'{l}\n')
       num+=1
       
def bbc_technology():
   '''取得title, summary, link'''
   bbc_web = urllib.request.urlopen('http://feeds.bbci.co.uk/news/technology/rss.xml')
   news = bbc_web.read()
   parsed_news = bs.BeautifulSoup(news,'lxml')
   #將連結放進list
   link_list=[]
   for link in parsed_news.find_all('guid'):
       link_list.append(link.text)
    #print(link_list)
   num = 0
   #取得文章
   for link in link_list:
       article = urllib.request.urlopen(link_list[num])
    
       parsed_article = bs.BeautifulSoup(article,'lxml')
            
       #取得標題
       ntitle = parsed_article.find('h1').string
       #print(f'{num+1}. {ntitle}')
       #得到文章內容
       article_text = ""
       paragraphs = parsed_article.find_all('p',class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")
       for paragraph in paragraphs:
           content = paragraph.text
           article_text+=content
       #取得連結   
       l = str(link_list[num])
        
       #利用SBERT取得摘要
       body = article_text
       model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
       result = model(body, num_sentences=3)
       print(result)
       print(l)
       #將得到的結果寫成txt檔
       with open(f'articles_t2_{num+1}.txt', 'w+', encoding="utf-8") as f:
           f.write(f'{ntitle}\n')
           f.write(f'{result}\n')
           f.write(f'{l}\n')
       num+=1
       
def bbc_health():    
   '''取得title, summary, link'''
   bbc_web = urllib.request.urlopen('http://feeds.bbci.co.uk/news/health/rss.xml')
   news = bbc_web.read()
   parsed_news = bs.BeautifulSoup(news,'lxml')
   #將連結放進list
   link_list=[]
   for link in parsed_news.find_all('guid'):
       link_list.append(link.text)
   #print(link_list)
   num = 0
   #取得文章
   for link in link_list:
       article = urllib.request.urlopen(link_list[num])
    
       parsed_article = bs.BeautifulSoup(article,'lxml')
            
       #取得標題
       ntitle = parsed_article.find('h1').string
       #print(f'{num+1}. {ntitle}')
       #得到文章內容
       article_text = ""
       paragraphs = parsed_article.find_all('p',class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")
       for paragraph in paragraphs:
           content = paragraph.text
           article_text+=content
       #取得連結   
       l = str(link_list[num])
        
       #利用SBERT取得摘要
       body = article_text
       model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
       result = model(body, num_sentences=3)
       print(result)
       print(l)
       #將得到的結果寫成txt檔
       with open(f'articles_t3_{num+1}.txt', 'w+', encoding="utf-8") as f:
           f.write(f'{ntitle}\n')
           f.write(f'{result}\n')
           f.write(f'{l}\n')
       num+=1
          
def open_txt_insert_1(tab, a_num):
    '''開啟txt檔並寫入欄位'''
    global times_1
    with open(f'articles_{tab}_{a_num}.txt', encoding="utf-8") as f:
        lines = f.readlines()
        list = []
        for line in lines:
            list.append(line)
        #print(list)
        t = list[0]
        s = list[1]
        l = list[2]
        title_1.insert(1.0, f"{t}" )
        summary_1.insert(1.0, f"{s}")
        links_1.insert(1.0, f"{l}")
        times_1+=1
        
def open_txt_insert_2(tab, a_num):
    '''開啟txt檔並寫入欄位'''
    global times_2
    with open(f'articles_{tab}_{a_num}.txt', encoding="utf-8") as f:
        lines = f.readlines()
        list = []
        for line in lines:
            list.append(line)
        #print(list)
        t = list[0]
        s = list[1]
        l = list[2]
        title_2.insert(1.0, f"{t}" )
        summary_2.insert(1.0, f"{s}")
        links_2.insert(1.0, f"{l}")
        times_2+=1
        
def open_txt_insert_3(tab, a_num):
    '''開啟txt檔並寫入欄位'''
    global times_3
    with open(f'articles_{tab}_{a_num}.txt', encoding="utf-8") as f:
        lines = f.readlines()
        list = []
        for line in lines:
            list.append(line)
        #print(list)
        t = list[0]
        s = list[1]
        l = list[2]
        title_3.insert(1.0, f"{t}" )
        summary_3.insert(1.0, f"{s}")
        links_3.insert(1.0, f"{l}")
        times_3+=1
        
def clean_1():
    '''清除欄位裡的資料'''
    title_1.delete(1.0,'end')
    summary_1.delete(1.0,'end')
    links_1.delete(1.0,'end')
    
def clean_2():
    '''清除欄位裡的資料'''
    title_2.delete(1.0,'end')
    summary_2.delete(1.0,'end')
    links_2.delete(1.0,'end')
    
def clean_3():
    '''清除欄位裡的資料'''
    title_3.delete(1.0,'end')
    summary_3.delete(1.0,'end')
    links_3.delete(1.0,'end')

#%%建立GUI
#利用tkinter來製作GUI    
window = Tk()
window.title("Lazy News Reader")
window.geometry('600x320')
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
notebook.add(tab1,text = "Top Stories")
#%%TOP_STORIES
#標題
tlabel = Label(tab1, text='Title')
tlabel.pack()

title_1 = Text(tab1, height=1, width=80)
title_1.config(bg='#dddddd')
title_1.pack()
#摘要
slabel = Label(tab1, text='Summary')
slabel.pack()

summary_1 = Text(tab1, height=10, width=80)
summary_1.config(bg='#dddddd')
summary_1.pack()
#連結
llabel = Label(tab1, text='Link')
llabel.pack()

links_1 = Text(tab1, height=1, width=80)
links_1.config(bg='#dddddd')
links_1.pack()

#按鈕
b1 = Button(tab1, text='start collecting data',command=bbc_top_stories)
times_1 = 1
b2 = Button(tab1, text='next one',command = clean_1)
b3 = Button(tab1, text='read', command= lambda:open_txt_insert_1('t1', times_1))
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=RIGHT)


#%%TECHNOLOGY
tab2 = Frame(notebook)
notebook.add(tab2, text = "Technology")
tlabel = Label(tab2, text='Title')
tlabel.pack()

title_2 = Text(tab2, height=1, width=80)
title_2.config(bg='#dddddd')
title_2.pack()
#摘要
slabel = Label(tab2, text='Summary')
slabel.pack()

summary_2 = Text(tab2, height=10, width=80)
summary_2.config(bg='#dddddd')
summary_2.pack()
#連結
llabel = Label(tab2, text='Link')
llabel.pack()

links_2 = Text(tab2, height=1, width=80)
links_2.config(bg='#dddddd')
links_2.pack()
#按鈕
b1 = Button(tab2, text='start collecting data',command= bbc_technology)
times_2 = 1
b2 = Button(tab2, text='next one',command= clean_2)
b3 = Button(tab2, text='read', command=lambda:open_txt_insert_2('t2', times_2))
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=RIGHT)


#%%HEALTH
tab3 = Frame(notebook)
notebook.add(tab3, text = "Health")
#標題
tlabel = Label(tab3, text='Title')
tlabel.pack()

title_3 = Text(tab3, height=1, width=80)
title_3.config(bg='#dddddd')
title_3.pack()
#摘要
slabel = Label(tab3, text='Summary')
slabel.pack()

summary_3 = Text(tab3, height=10, width=80)
summary_3.config(bg='#dddddd')
summary_3.pack()
#連結
llabel = Label(tab3, text='Link')
llabel.pack()

links_3 = Text(tab3, height=1, width=80)
links_3.config(bg='#dddddd')
links_3.pack()
#按鈕
b1 = Button(tab3, text='start collecting data',command=bbc_health)
times_3 = 1
b2 = Button(tab3, text='next one',command = clean_3)
b3 = Button(tab3, text='read', command=lambda:open_txt_insert_3('t3', times_3))
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=RIGHT)


#%%
notebook.pack()
window.mainloop()

