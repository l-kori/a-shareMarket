import requests
import re
from django.http import JsonResponse
from ashareAll.models import allstock_a
def updatesStockAll(request):
    r = requests.get("http://www.bestopview.com/stocklist.html")
    stock_id = re.findall('stockcode=(.*?)" target="_blank">', r.text)
    print(len(stock_id))
    # stock_id = ['600601','600500','600323','454857']
    # # 读数据库判断股票是否存在，不存在则写入
    stockall = list(allstock_a.objects.all().values())
    stockallList = []
    for i in stockall:
        stockallList.append(i['stock_id'])
    # 循环检查数据库里的股票是否为最新
    for i in stock_id:
        if i in stockallList:
            pass
        else:
            stockalla = allstock_a()
            stockalla.stock_id = i
            stockalla.save()
    return JsonResponse({"code":1})