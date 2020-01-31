#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen
import os
import sys
from stock_list import set_stock_list, search_stock


BaseUrl = 'http://f10.eastmoney.com/NewFinanceAnalysis'


def get_year_report(code, year="", item="zcfzb"):
    url = "{base}/{item}Ajax?companyType=4&reportDateType=1&reportType=1&endDate={endDate}&code={code}"
    url = url.format(base=BaseUrl, item=item, code=code, endDate=year)

    response = urlopen(url).read()
    jsonReport = json.loads(response)
    return jsonReport


def get_year_report_zcfzb(code, year=""):
    return get_year_report(code, year, item="zcfzb")


def get_year_report_lrb(code, year=""):
    return get_year_report(code, year, item="lrb")


def get_year_report_xjllb(code, year=""):
    return get_year_report(code, year, item="xjllb")


def pretty_print_year_report(code):
    report = get_year_report_xjllb(code)
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
