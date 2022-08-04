import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.nulearn.in/"
r = requests.get(URL)
urlSoup = BeautifulSoup(r.content, 'html.parser')




# Fetch All the URLs

mica = urlSoup.find_all("div",class_ = "mob-inst-course-accordian")

urls = []
for m in mica:
    micw = m.find_all("div",class_ = "mob-inst-course-wrapper")
    for mw in micw:
        ta = mw.find_all("a")
        for a in ta:
            urls.append(a["href"])


# Fetch The Page Content

df = {"Title":[],"Discription":[],"Institution":[],"Course Duration"
  :[],"Data of Commencement":[],"online session":[],"enrollment":[]}

dfkey = ["Institution","Course Duration","Data of Commencement","online session","enrollment"]

m = 1
print("scrapping....")
for url in urls: 
  r = requests.get(url)
  cont = BeautifulSoup(r.content, 'html.parser')

  pageName = cont.find("h1",class_="course-page-name").text
  disc = cont.find("p",class_="course-banner-para").text
  courseKey = cont.find_all("div",class_="course-icon-block")

  df["Title"] = pageName
  df["Discription"] = disc
  i = 0;
  for key in courseKey:
    try:
      if i == 4:
        m+=1
        break
      df[dfkey[i]].append(key.h4.text)
      i+=1
    except:
      pass
    
del df["enrollment"]
dfc = pd.DataFrame(df)

dfc.to_csv("scarped.csv")
print("scarped.csv saved!!")

