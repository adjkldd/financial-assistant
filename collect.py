#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen
import os
import sys
from stock_list import set_stock_list, search_stock


BaseUrl = 'http://f10.eastmoney.com/NewFinanceAnalysis/zcfzbAjax'


def get_year_report(code, year=""):
    url = "{base}?companyType=4&reportDateType=1&reportType=1&endDate={endDate}&code={code}"
    url = url.format(base=BaseUrl, code=code, endDate=year)

    response = urlopen(url).read()
    jsonReport = json.loads(response)
    return jsonReport


def pretty_print_year_report(code):
    report = get_year_report(code)
    f = open('foo.json', 'w')
    f.write(str(report))
    f.close()
    os.system("python3 -m json.tool < foo.json")


if __name__ == '__main__':
    name = '海康威视'
    if len(sys.argv) > 1:
        name = sys.argv[1]

    set_stock_list()
    pretty_print_year_report(search_stock(name))
