import requests 
res = requests.get("http://tw.taobao.com/category/53670017/x.htm?cat=53670017&module=sortList&sort=_deal&_ksTS=1431406892168_357&spm=a213z.1224559.20150331F102.1.XccrpD&_input_charset=utf-8&_lang=zh_CN%3ATB-GBK&navigator=all&s=0&json=on&cna=O8kKDY4DbwACAbTaoj81aDL2&callback=__jsonp_cb&abtest=_AB-LR492-LR501-LR517-PR492-PR501-PV517_1274")
print res.text