# Finds next airdate, storyline and imdb rating of requested TVshow as in the parameter (name)
from bs4 import BeautifulSoup
import requests
import datetime
from dateutil.parser import parse
from multiprocessing import Pool

def findURL(name):
  try:
    name = name.strip()
    name = name.replace(" ","%20")
    #Placed in the imdb searchbar
    urlb="https://www.imdb.com/find?ref_=nv_sr_fn&q="+str(name)+"&s=tt&ttype=tv&ref_=fn_tv"
    rb = requests.get(urlb)
    soupb = BeautifulSoup(rb.text, "html.parser")
    tag = soupb.find("td", {"class": "result_text"})
    #selects the topmost TVshow avaiable according to imdb search
    name = str(tag.a.text+" "+tag.contents[2].split(" ")[1])

    url = "https://www.imdb.com"+str(tag.a["href"])
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    isDone = str(soup.find("a",{"title":"See more release dates"}).text)

    mydate = 'no information on next season'
    #Gets storyline from imdb site
    Storyline = str(soup.find("div",{"class":"inline canwrap"}).p.span.text)
    #Gets rating from imdb site
    rating = str(soup.find("span",{"itemprop":"ratingValue"}).text)
    #checks if streaming is finished from given duration in title bar of imdb site
    if(len(isDone.split(" "))==3):
      mydate = 'The show has finished streaming all its episodes'

    elif(len(isDone.split(" "))==4):
      #navigates to the last season page of given TVshow
      tag = soup.find("div",{"class": "seasons-and-year-nav"})
      containers = tag.findAll("div")
      code = containers[2].a["href"]
      url = "https://www.imdb.com"+code
      r = requests.get(url)
      soup = BeautifulSoup(r.text,'html.parser')
      #stores all airdates in list dates
      dates = soup.findAll("div", {"class": "airdate"})
      dates = [d.string.strip() for d in dates]

      a = []
      for date in dates:
        if date=='':
          mydate='Release date not known'
          break
        split_date = date.split(' ')
        if len(split_date)==3:
          a.append(date)
        else:
          mydate='Next season begins in '+ date
          break
      dates = [parse(date) for date in a ]
      for date in dates:
        #Changes format of date
        if date.date() >= datetime.date.today():
          mydate= 'The next episode airs on ' + date.strftime('%Y-%m-%d')
          break
    val  = (name,mydate,Storyline,rating)
    return val

  except:
    #if an error occurs or name entered gives no search result
    name = name.replace('%20'," ")
    val = (name,'-1','-1','-1')
    return val