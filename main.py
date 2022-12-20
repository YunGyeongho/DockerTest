from fastapi import FastAPI
import requests
import urllib
from _datetime import datetime
from datetime import timedelta
import pandas as pd
import os, sys

app = FastAPI()

apiID = "API ID를 입력해 주세요"
apiKey = "API Key를 입력해 주세요"
googleAPIUrl = "https://customsearch.googleapis.com/customsearch/v1"

setPage = 10
#원하시는 페이지 정수(1 ~ 10)를 입력해 주세요.

def getItems(query, page):
    global apiID, apiKey, googleAPIUrl
    googleAPIResponse = requests.get("%s?q=%s&sort=date&start=%d&cx=%s&key=%s" % (googleAPIUrl, query, page, apiID, apiKey))
    
    return googleAPIResponse.json()["items"]


def writeTSV(items, file):
    item = None

    for item in items:

        file.write("%s\t%s\t%s\n" % (item["title"], item["link"], item["snippet"]))
        # 순서는 제목, url, 글 내용 입니다.   


def reWriteTSV():

    df = pd.read_csv("/googleSearchResult.tsv", sep="\t", names=["title", "url", "content"])

    content = df["content"].to_numpy()
    dateAr = []
    now = datetime.today()
    postDate, date, c = None, None, None

    for c in content:
        date = c.split("...")[0]
        postDate = date.split(" ")

        if postDate[2].__contains__("ago"):
            postDate = now - timedelta(days=int(postDate[0]))
            postDate = int(datetime.strftime(postDate, '%Y%m%d'))
        else:
            postDate = datetime.strptime(date, '%b %d, %Y ')
            postDate = int(datetime.strftime(postDate, '%Y%m%d'))

        dateAr.append(postDate)

    df["date"] = dateAr
    df = df.sort_values(by="date")
    df = df[["date", "title", "url", "content"]]
    df.to_csv("/gsrSortByDate.tsv", encoding="utf-8", index=False, sep="\t")


@app.get("/search")
def searchGoogle(keyword):
    try:
        global setPage
        query = requests.utils.quote(keyword)
        setPage = setPage * 10 - 8
        f = open("/googleSearchResult.tsv", "a", encoding="utf-8")

        page, items = None, None

        for page in range(1, setPage, 10):
            try:
                items = getItems(query, page)
                writeTSV(items, f)
            except KeyError:
                # 글 내용 키 값인 "snippet" 이 없는 경우가 존재합니다.
                continue
        f.close()

        reWriteTSV()

        return {'result': "성공"}

    except Exception as e:
        print(e)
        return {'result': "실패"}


@app.post("/search")
def searchGoogle(keyword):
    try:
        global setPage
        query = requests.utils.quote(keyword)
        setPage = setPage * 10 - 8
        f = open("/googleSearchResult.tsv", "a", encoding="utf-8")

        page, items = None, None

        for page in range(1, setPage, 10):
            try:
                items = getItems(query, page)
                writeTSV(items, f)
            except KeyError:
                # 글 내용 키 값인 "snippet" 이 없는 경우가 존재합니다.
                continue
        f.close()

        reWriteTSV()

        return {'result': "성공"}

    except Exception as e:
        print(e)
        return {'result': "실패"}