import os
import requests
from dotenv import load_dotenv
from verbix.db import con

load_dotenv()
cur = con.cursor()
api_url = os.getenv("API_URL")

def search_word(word):
    try:
        data = get_word(word)
        if data != None:
            print("from db")
            return data
        req = requests.get(api_url+word)
        if req.status_code != 200:
            return "NOT found"
        data = req.json()
        list = []
        for m in data[0]["meanings"]:
            list.append(m["definitions"][0]["definition"])
        meaning  = ";".join(list)
        save_word(word, meaning)
        return meaning
    except:
        return "error"

def save_word(word, meaning):
    try:
        cur.execute("INSERT INTO wordlist (keyword, meanings) VALUES (?, ?)", (word, meaning))
        con.commit()
    except:
        return None

def get_word(word):
    try:
        cur.execute("SELECT * from wordlist WHERE keyword = ?", (word, ))
        meanings = cur.fetchone()
        return meanings[1]
            
    except:
        return None
     
