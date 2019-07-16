#!/usr/bin/env python3
import requests
import urllib.request
import json
import csv
import time

# 各都市のURLリスト
city_ids = ['013010',
'013020',
'013030',
'014010',
'014020',
'014030',
'015010',
'015020',
'016010',
'016020',
'016030',
'017010',
'017020',
'020010',
'020020',
'020030',
'030010',
'030020',
'030030',
'040010',
'040020',
'050010',
'050020',
'060010',
'060020',
'060030',
'060040',
'070010',
'070020',
'070030',
'080010',
'080020',
'090010',
'090020',
'100010',
'100020',
'110010',
'110020',
'110030',
'120010',
'120020',
'120030',
'130010',
'130020',
'130030',
'130040',
'140010',
'140020',
'150010',
'150020',
'150030',
'150040',
'160010',
'160020',
'170010',
'170020',
'180010',
'180020',
'190010',
'190020',
'200010',
'200020',
'200030',
'210010',
'210020',
'220010',
'220020',
'220030',
'220040',
'230010',
'230020',
'240010',
'240020',
'250010',
'250020',
'260010',
'260020',
'270000',
'280010',
'280020',
'290010',
'290020',
'300010',
'300020',
'310010',
'310020',
'320010',
'320020',
'320030',
'330010',
'330020',
'340010',
'340020',
'350010',
'350020',
'350030',
'350040',
'360010',
'360020',
'370000',
'380010',
'380020',
'380030',
'390010',
'390020',
'390030',
'400010',
'400020',
'400030',
'400040',
'410010',
'410020',
'420010',
'420020',
'420030',
'420040',
'430010',
'430020',
'430030',
'430040',
'440010',
'440020',
'440030',
'440040',
'450010',
'450020',
'450030',
'450040',
'460010',
'460020',
'460030',
'460040',
'471010',
'471020',
'471030',
'472000',
'473000',
'474010',
'474020']

# CSVファイルオープン
f = open('tenki_data.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

# CSVヘッダー
writer.writerow(['id','area','prefecture','city','label_1','day_1','telop_1','label_2','day_2','telop_2'])


for city_id in city_ids:
    
    # 天気情報を取得(JSON形式)
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    payload = {'city':city_id}
    tenki_data = requests.get(url, params=payload).json()

    area = tenki_data['location']['area']
    prefecture = tenki_data['location']['prefecture']
    city = tenki_data['location']['city']
    label_0 = tenki_data['forecasts'][0]['dateLabel']
    day_0 = tenki_data['forecasts'][0]['date']
    telop_0 = tenki_data['forecasts'][0]['telop']
    label_1 = tenki_data['forecasts'][1]['dateLabel']
    day_1 = tenki_data['forecasts'][1]['date']
    telop_1 = tenki_data['forecasts'][1]['telop']

# Debug
#    print(city_id)
#    print(area)
#    print(prefecture)
#    print(city)
#    print(label)
#    print(day)
#    print(telop)

    # データをリストに保持
    csvlist = []
    csvlist.append(city_id)
    csvlist.append(area)
    csvlist.append(prefecture)
    csvlist.append(city)
    csvlist.append(label_0)
    csvlist.append(day_0)
    csvlist.append(telop_0)
    csvlist.append(label_1)
    csvlist.append(day_1)
    csvlist.append(telop_1)

    # 出力
    writer.writerow(csvlist)

    # 1秒スリープ
    time.sleep(0.1)

# ファイルクローズ
f.close()

####### 予備 #######
#for number in range(line_count):
#    try:
#        location = tenki_data['pinpointLocations'][number]['name']
#        link = tenki_data['pinpointLocations'][number]['link']
#        
#        # データをリストに保持
#        csvlist = []
#        csvlist.append(number + 1)
#        csvlist.append(location)
#        csvlist.append(location)
#        csvlist.append(link)
#
#        # 出力
#        writer.writerow(csvlist)
#
#        print(location,link)
#
#    except:
#        pass


# JSONファイル作成
#write_file = open('tenki_data.json','w')
#json.dump(tenki_data,write_file,ensure_ascii=False,indent=2)
#write_file.close()

# JSONファイルの行数取得
#with open('tenki_data.json') as f:
#    for line_count, _ in enumerate(f, 1):
#        pass

#print(line_count)
