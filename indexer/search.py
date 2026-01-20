import os
from dotenv import load_dotenv
import requests
import urllib.robotparser as urobot
from trafilatura import fetch_url, extract
from trace import Trace
import signal

load_dotenv()
SEARXNG_URL = os.getenv("SEARXNG_URL")

def timeout_handler(signum, frame):
    raise Exception()

def can_scrape(domain, path):
    rp = urobot.RobotFileParser()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(1)
    try:
        rp.set_url(domain + "/robots.txt"  )
        rp.read()
        return rp.can_fetch(path, domain)
    except Exception:
        return False

def get_text(url):
    text = None
    try:
        text = extract(fetch_url(url), favor_precision=True)
    except Exception:
        pass
    return text

def search(query, pull_text=False):
    resp = requests.get(f"{SEARXNG_URL}/search?q={query}&format=json")
    resp = resp.json()

    # Filter for scrapable results, and drop irrelevant fields
    resp["results"] = [r for r in resp["results"] if can_scrape("://".join(r["parsed_url"][0:2]), r["url"])]
    resp["results"] = [{
        "url": r["url"],
        "title": r["title"],
        "content": r["content"],
        "text": get_text(r["url"] if pull_text else None),
        "publishedDate": r["publishedDate"]
    } for r in resp["results"]]

    resp["results"] = [r for r in resp["results"] if not pull_text or r["text"] is not None]
    resp["infoboxes"] = [{
        "infobox": i["infobox"],
        "id": i["id"],
        "content": i["content"],
        "img_src": i["img_src"],
        "urls": i["urls"],
        "attributes": i["attributes"],
        "publishedDate": i["publishedDate"]
    } for i in resp["infoboxes"]]

    Trace.log([f"search results for {query}", resp])
    
    return resp