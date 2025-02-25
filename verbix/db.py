import os
import sqlite3
from dotenv import load_dotenv


load_dotenv()
api_url = os.getenv("API_URL")
local_db = os.getenv("Local_DB")

con = sqlite3.connect(local_db)

con.execute("CREATE TABLE IF NOT EXISTS wordlist (keyword TEXT NOT NULL, meanings TEXT NOT NULL)")
