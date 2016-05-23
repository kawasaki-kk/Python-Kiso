# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスの多言語版レストラン検索APIで緯度経度検索を実行しパースするプログラム
# 注意：ここでは緯度と経度の値は固定でいれています。言語は英語を指定しています。
# 　　　APIアクセスキーの値にはユーザ登録で取得したものを入れてください。
#*****************************************************************************************

def gurunavi_search_multiLang(keyid, freeword):
  import sys
  import urllib
  import urllib.parse
  import urllib.request
  import json

  ####
  # 変数の型が文字列かどうかチェック
  ####
  def is_str( data = None ) :
    if isinstance( data, str ) or isinstance( data, unicode ) :
      return True
    else :
      return False
   
  ####
  # 初期値設定
  ####
  # APIアクセスキー
  # keyid     = 
  # エンドポイントURL
  url       = "http://api.gnavi.co.jp/ForeignRestSearchAPI/20150630/"
  # 緯度・経度、範囲を変数に入れる
  # 緯度経度は日本測地系で日比谷シャンテのもの。範囲はrange=1で300m以内を指定している。
  # 緯度
  latitude  = "35.670083"
  # 経度
  longitude = "139.763267"
  # 範囲
  range     = "1"
   
  ####
  # APIアクセス
  ####
  # URLに続けて入れるパラメータを組立
  query = [
    ( "format",    "json"    ),
    ( "keyid",     keyid     ),
    ( "lang",      "en"      ),
    ( "latitude",  latitude  ),
    ( "longitude", longitude ),
    ( "range",     range     ),
    ( "freeword", freeword),
  ]
  # URL生成
  url += "?{0}".format( urllib.parse.urlencode( query ) )
  # API実行
  try :
    result = urllib.request.urlopen( url ).read().decode('utf8')
  except ValueError :
    print(u"APIアクセスに失敗しました。")
    sys.exit()
   
  ####
  # 取得した結果を解析
  ####
  data = json.loads( result )
   
  # エラーの場合
  if "error" in data :
    if "message" in data :
      print(u"{0}".format( data["message"] ))
    else :
      print(u"データ取得に失敗しました。")
    sys.exit()
   
  # ヒット件数取得
  total_hit_count = None
  if "total_hit_count" in data :
    total_hit_count = int(data["total_hit_count"])
   
  # ヒット件数が0以下、または、ヒット件数がなかったら終了
  if total_hit_count is None or total_hit_count <= 0 :
    print(u"指定した内容ではヒットしませんでした。")
    sys.exit()
   
  # レストランデータがなかったら終了
  if not "rest" in data :
    print(u"レストランデータが見つからなかったため終了します。")
    sys.exit()
   
  # ヒット件数表示
  print("{0}件ヒットしました。".format( total_hit_count ))
  print("----")
   
  #ヒット件数が1件だった場合の処理
  if total_hit_count == 1:
    data["rest"] = [data["rest"]]

  # 出力件数
  disp_count = 0
   

  # print("data",data)

  # レストランデータ取得
  for rest in data["rest"] :
    line                 = []
    id                   = ""
    name                 = ""
    access               = ""
   
    # 店舗番号
    if "id" in rest and is_str( rest["id"] ) :
      id = rest["id"]
    line.append( id )
   
    if "name" in rest :
      name = rest["name"]
      # 最寄の路線
      if "name" in name and is_str( name["name"] ) :
        name = u"{0}".format( name["name"] )
      line.append( name )
    #　アクセス情報
    if "access" in rest and is_str( rest["access"] ) :
      access = u"{0}".format( rest["access"] )
    line.append( access )
   
    # タブ区切りで出力
    print("\t".join( line ))
    disp_count += 1
   
  # 出力件数を表示して終了
  print("----")
  print(u"{0}件出力しました。".format( disp_count ))
  sys.exit()