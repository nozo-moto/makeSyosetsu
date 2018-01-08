import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import MeCab
from collections import Counter

class PosData():
    def __init__(self):
        self.pos_list = []
        self.pos_words_dict = {}

    def splitting_per_pos(self, text: str):
        mecab = MeCab.Tagger("-Ochasen")
        data = mecab.parse(text).split('\n')
        data = [
            d.split('\t')
            for d in data
        ]
        data.pop(-1)
        data.pop(-1)
        pos_list_data = [
            d[3] for d in data
        ]
        for d in data:
            if d[3] not in self.pos_words_dict:
                self.pos_words_dict.update({d[3]: []})
            self.pos_words_dict[d[3]].append([d[0]])
        self.pos_list.append(pos_list_data)

    def split_text(self, quote_list):
        [
            self.splitting_per_pos(quote)
            for quote in quote_list
        ]

def scraping(url="http://www.aozora.gr.jp/cards/000035/files/301_14912.html"):
    global quote_list
    global narrator_list
    htmldata = urllib.request.urlopen(url).read().decode('shift-jis')
    soup = BeautifulSoup(htmldata, 'lxml')
    data = soup.find_all("div", attrs={"class": "main_text"})
    data = re.sub(r'<(.+?)>', "", str(data))
    data = re.sub(r'［(.+?)］', "", str(data))
    data = re.sub(r'（(.+?)）', "", str(data))
    data = re.sub(r'\r', "", str(data))
    data = re.sub(r'\u3000', "", str(data))
    datalist = data.split('\n')
    quote_list = [
        data
        for data in datalist
        if not data.find("「")
    ]
    narrator_list = [
        data
        for data in datalist
        if data.find("「") and data != ''
    ]
    narrator_list.pop(0)
    narrator_list.pop(-1)

def run(url="http://www.aozora.gr.jp/cards/000035/files/301_14912.html"):
    scraping(url)
    quote.split_text(quote_list)
    narrator.split_text(narrator_list)

quote = PosData()
narrator = PosData()

run('http://www.aozora.gr.jp/cards/000035/files/305_20174.html')
run('http://www.aozora.gr.jp/cards/000035/files/306_20009.html')
run('http://www.aozora.gr.jp/cards/000035/files/42365_15875.html')
run('http://www.aozora.gr.jp/cards/000035/files/1584_13915.html')
run('http://www.aozora.gr.jp/cards/000035/files/52460_45490.html')
run('http://www.aozora.gr.jp/cards/000035/files/260_34634.html')
run('http://www.aozora.gr.jp/cards/000035/files/280_19990.html')
run('http://www.aozora.gr.jp/cards/000035/files/282_45418.html')
run('http://www.aozora.gr.jp/cards/000035/files/276_45435.html')
run('http://www.aozora.gr.jp/cards/000035/files/241_15081.html')
run('http://www.aozora.gr.jp/cards/000035/files/1593_18101.html')
run('http://www.aozora.gr.jp/cards/000035/files/42362_34746.html')
run('http://www.aozora.gr.jp/cards/000035/files/42359_15871.html')
run('http://www.aozora.gr.jp/cards/000035/files/2253_14908.html')

