import os
from dotenv import load_dotenv
import requests
import urllib.robotparser as urobot

load_dotenv()
SEARXNG_URL = os.getenv("SEARXNG_URL")

def search(query):
    resp = requests.get(f"{SEARXNG_URL}/search?q={query}&format=json")
    
# rp = urobot.RobotFileParser()
# rp.set_url(url + "/robots.txt")
# rp.read()
# if rp.can_fetch("*", url):