from urllib.request import urlopen
import pickle
from bs4 import BeautifulSoup

StockCodeList = []


def save_stock_list():
    try:
        with open('stock_list.pkl', 'wb') as output:
            pickle.dump(StockCodeList, output)
    except Exception as e:
        print('failed to save stock list: {}'.format(e))


def load_stock_list():
    global StockCodeList
    try:
        with open('stock_list.pkl', 'rb') as f:
            StockCodeList = pickle.load(f)
        return True
    except:
        return False


def set_stock_list():
    global StockCodeList
    if load_stock_list():
        return

    html = urlopen("http://quote.eastmoney.com/stock_list.html").read()
    # NOTE: 网页编码被指定为 gb2312 方式，这里 decode 的参数只能用 gbk
    soup = BeautifulSoup(html.decode('gbk'), "html.parser")
    quotesearch = soup.find("div", id="quotesearch")
    shStockList = quotesearch.ul

    szStockList = shStockList.next_sibling
    while szStockList.name != 'ul':
        szStockList = szStockList.next_sibling

    for item in shStockList.find_all('li'):
        name, code = item.a.string.strip(')').split('(')
        StockCodeList.append(('sh' + code, name, code))

    for item in szStockList.find_all('li'):
        name, code = item.a.string.strip(')').split('(')
        StockCodeList.append(('sz' + code, name, code))

    save_stock_list()


def search_stock(name_or_code):
    global StockCodeList
    for tu in StockCodeList:
        if tu[1] == name_or_code or tu[2] == name_or_code:
            return tu[0]
