# -*- coding: utf-8 -*-

#*****************************************************************************************
# ぐるなびWebサービスのレストラン検索APIで緯度経度検索を実行しパースするプログラム
# 入力言語によって、レストラン検索API（日本語版のAPI）と多言語版レストラン検索APIの切り替えなどを行う。
#*****************************************************************************************

import sys
import unicodedata
import yaml

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name:
            return True
    return False

# APIアクセスキー
# keyid = open("GURUNAVI_API_ACCESS_KEY","r").read()
f = open("API_ACCESS_KEY.yaml","r")
api_data = yaml.load(f)
keyid=api_data["name"=="ぐるなびレストラン検索API"]["key"]
f.close()

if __name__ == "__main__":
	# print("ぐるなびのレストラン検索へようこそ")
	# print("検索したいお店のフリーワードを入れてください(日本語/English)")
	# freeword = input()

	freeword = sys.argv[1]

	if is_japanese( freeword ):
		from extra_kadai_Jp import *
		gurunavi_search_jp(keyid, freeword)
		# gurunavi_search_jp(keyid, freeword)
	else:
		from extra_kadai_multiLang import *
		gurunavi_search_multiLang(keyid, freeword)
