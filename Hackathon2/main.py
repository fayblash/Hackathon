import random
from tkinter import *
import requests
import datetime
import re
import webbrowser

# quote of the day function   
def quote():
      rquote = requests.get('https://zenquotes.io/api/random')
      jquote=rquote.json()
      quote_text.config(text=jquote[0]['q'])

# in this day in history function
def history(): 
      rhist=requests.get(f"https://apizen.date/api/{now.month}/{now.day}")
      jhist=rhist.json()
      hist=jhist['data']['Events'][-1]['text']
      hist =f"On {now.strftime('%B')} {now.day}, " + re.sub(r"&#\d+;", "", hist)           
      hist_text.config(text=hist)

# joke of the day function
def joke():
      rjoke = requests.get('https://official-joke-api.appspot.com/random_joke')
      jjoke=rjoke.json()
      joke_text.config(text=f"{jjoke['setup']} {jjoke['punchline']}")

# halacha of the day function
def halacha():
      rhalacha = requests.get('https://www.sefaria.org/api/calendars')
      jhalacha=rhalacha.json()
      hal=jhalacha['calendar_items'][-1]['url']
      halacha_text.config(text=hal)
      hal=re.sub(r",", "%2C", hal)
      url=f"https://www.sefaria.org.il/{hal}?lang=he"
      halacha_text.bind("<Button-1>", lambda e: callback(url))
      
#recipe of the day function   
def recipe():
      rrecipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
      jrecipe=rrecipe.json()
      recipe_name=jrecipe['meals'][0]['strMeal']
      url=jrecipe['meals'][0]['strSource']
      recipe_text.config(text=f"{recipe_name}: {url}")
      recipe_text.bind("<Button-1>", lambda e: callback(url))

# tip of the day function
def advice():
      radvice=requests.get('https://api.adviceslip.com/advice')  
      jadvice=radvice.json()    
      advice_text.config(text=jadvice['slip']['advice'])
      
#headline of the day function   
def headline():
      rhl=requests.get('https://newsapi.org/v2/top-headlines?country=il&apiKey=fa1deed99e7042e2b6718726efb0a338')
      jhl=rhl.json()
      alist=[0,1,2,3]
      random_article=random.choice(alist)
      title=jhl['articles'][random_article]['title']
      url=jhl['articles'][random_article]['url']
      headline_text.config(text=title)
      headline_text.bind("<Button-1>", lambda e: callback(url))

# daily forecast function
def weather():
      rw=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Jerusalem,Il&units=metric&APPID=7036bab78741c80b61a3957a27dbc27e')
      jw=rw.json()
      forecast=f"The current weather in Jerusalem is {jw['weather'][0]['main'].lower()} and {jw['main']['temp']} degrees." 
      weather_text.config(text=forecast)
      
#function to open link in browser   
def callback(url):
    webbrowser.open_new(url)

# open window in Tkinter
window=Tk()
window.title("Your Daily Dose of Inspiration")
window.config(bg='white') 

# background image
C = Canvas(window, bg="white", height=800, width=600)
filename = PhotoImage(file="bgd.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# getting today's date
now = datetime.datetime.now()
date=Label(text=f"Today's date is {now.strftime('%B')} {now.day}, {now.year}",font=("Raleway", 20))
date.grid(row =0,column=0,columnspan=2,pady=10)

intro=Label(text="Start your day off right",font=("Raleway",10))
intro.grid(row=1,column=0,columnspan=2,pady=10)

#buttons and labels 
 
quote_button=Button(text='Quote of the Day',width=18,command=quote)
quote_button.grid(row=2,column=0,padx=10)

quote_text= Label(width=100,height=2)
quote_text.config(bg="white")
quote_text.grid(row=2,column=1,padx=5,pady=5)

hist_button=Button(text='On this Day in History',width=18,command=history)
hist_button.grid(row=3,column=0,padx=10)

hist_text= Label(width=100,height=2)
hist_text.config(bg="white")
hist_text.grid(row=3,column=1,padx=5,pady=5)

joke_button=Button(text='Joke of the Day',width=18,command=joke)
joke_button.grid(row=4,column=0,padx=10)

joke_text= Label(width=100, height=2)
joke_text.config(bg='white')
joke_text.grid(row=4,column=1,padx=5,pady=5)

halacha_button=Button(text='Halacha of the Day',width=18,command=halacha)
halacha_button.grid(row=5,column=0,padx=10)

halacha_text= Label(width=100,fg="blue", cursor="hand2",height=2,bd=3)
halacha_text.config(bg='white')
halacha_text.grid(row=5,column=1,padx=5,pady=5)

recipe_button=Button(text='Recipe of the Day',width=18,command=recipe)
recipe_button.grid(row=6,column=0,padx=10)

recipe_text= Label(width=100,fg="blue", cursor="hand2",height=2)
recipe_text.config(bg='white')
recipe_text.grid(row=6,column=1,padx=5,pady=5)

advice_button=Button(text='Tip of the Day',width=18,command=advice)
advice_button.grid(row=7,column=0,padx=10)

advice_text= Label(width=100, height=2)
advice_text.config(bg='white')
advice_text.grid(row=7,column=1,padx=5,pady=5)

headline_button=Button(text='Headline of the Day',width=18,command=headline)
headline_button.grid(row=8,column=0,padx=10)

headline_text= Label(width=100,fg="blue", cursor="hand2",height=2)
headline_text.config(bg='white')
headline_text.grid(row=8,column=1,padx=5,pady=5)

weather_button=Button(text="Today's Weather",width=18,command=weather)
weather_button.grid(row=9,column=0,padx=10)

weather_text= Label(width=100,height=2)
weather_text.config(bg='white')
weather_text.grid(row=9,column=1,padx=5,pady=5)

window.mainloop()


