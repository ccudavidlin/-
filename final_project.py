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
       
def open_txt_insert(tab, a_num):
    '''開啟txt檔並寫入欄位'''
    global times
    with open(f'articles_{tab}_{a_num}.txt', encoding="utf-8") as f:
        lines = f.readlines()
        list = []
        for line in lines:
            list.append(line)
        #print(list)
        t = list[0]
        s = list[1]
        l = list[2]
        title.insert(1.0, f"{t}" )
        summary.insert(1.0, f"{s}")
        links.insert(1.0, f"{l}")
        times+=1
        
def clean():
    '''清除欄位裡的資料'''
    title.delete(1.0,'end')
    summary.delete(1.0,'end')
    links.delete(1.0,'end')

# bbc_top_stories()
# bbc_technology()
# bbc_health()

#利用tkinter來製作GUI    
window  =Tk()
window.title("Lazy News Reader")
window.geometry('600x320')
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

#Top Stories分頁
notebook.add(tab1,text = "Top Stories")

#標題
tlabel = Label(tab1, text='Title')
tlabel.pack()

title = Text(tab1, height=1, width=80)
title.config(bg='#dddddd')
title.pack()
#摘要
slabel = Label(tab1, text='Summary')
slabel.pack()

summary = Text(tab1, height=10, width=80)
summary.config(bg='#dddddd')
summary.pack()
#連結
llabel = Label(tab1, text='Link')
llabel.pack()

links = Text(tab1, height=1, width=80)
links.config(bg='#dddddd')
links.pack()

#按鈕
b1 = Button(tab1, text='start collecting data',command=bbc_top_stories)
times = 1
b2 = Button(tab1, text='next one',command = clean)
b3 = Button(tab1, text='read', command=lambda:open_txt_insert('t1', times))
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=RIGHT)



#Technology分頁
notebook.add(tab2, text = "Technology")
tlabel = Label(tab2, text='Title')
tlabel.pack()

title = Text(tab2, height=1, width=80)
title.config(bg='#dddddd')
title.pack()
#摘要
slabel = Label(tab2, text='Summary')
slabel.pack()

summary = Text(tab2, height=10, width=80)
summary.config(bg='#dddddd')
summary.pack()
#連結
llabel = Label(tab2, text='Link')
llabel.pack()

links = Text(tab2, height=1, width=80)
links.config(bg='#dddddd')
links.pack()
#按鈕
b1 = Button(tab2, text='start collecting data',command= bbc_technology())
times = 1
b2 = Button(tab2, text='next one',command= clean)
b3 = Button(tab2, text='read', command=lambda:open_txt_insert('t2', times))
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=RIGHT)


#Health分頁
notebook.add(tab3, text = "Health")
#標題
tlabel = Label(tab3, text='Title')
tlabel.pack()

title = Text(tab3, height=1, width=80)
title.config(bg='#dddddd')
title.pack()
#摘要
slabel = Label(tab3, text='Summary')
slabel.pack()

summary = Text(tab3, height=10, width=80)
summary.config(bg='#dddddd')
summary.pack()
#連結
llabel = Label(tab3, text='Link')
llabel.pack()

links = Text(tab3, height=1, width=80)
links.config(bg='#dddddd')
links.pack()
#按鈕
b1 = Button(tab3, text='start collecting data',command=bbc_health)
times = 1
b2 = Button(tab3, text='next one',command = clean)
b3 = Button(tab3, text='read', command=lambda:open_txt_insert('t3', times))
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=RIGHT)


notebook.pack()

window.mainloop()