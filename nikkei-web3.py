# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

# アクセスするURL
url = "https://www.nikkei.com/markets/kabu/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string


# タイトル要素を出力
print (title_tag)

# タイトルの文字列を出力
print (title)

# 以下、日経平均
# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
span = soup.find_all("span")

# print時のエラーとならないように最初に変数を宣言しておきます。
nikkei_heikin = ""

for tag in span:
        # tagについて、span分繰り返す
        # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        string_=tag.get("class").pop(0)
        #get関数とpop関数
        #string_リストにtagにclassがついていたら全部ぶち込む
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する

        if string_ in "mkc-stock_prices":#string_リストの中にこのクラスがあったら
            nikkei_heikin = tag.string
            break
    except:
        pass

print (nikkei_heikin)