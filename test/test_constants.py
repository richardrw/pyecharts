# coding=utf-8

from __future__ import unicode_literals

import pyecharts.constants as constants
from nose.tools import eq_


DEFAULT_JS_LIBRARIES = dict(
    echarts='echarts.min',
    echartsgl='echarts-gl.min',
    liquidfill='echarts-liquidfill.min',
    world='world',
    china='china',
    wordcloud='echarts-wordcloud.min'
)

CITY_NAME_PINYIN_MAP = {
    "广东": "guangdong",
    "安徽": "anhui",
    "澳门": "aomen",
    "北京": "beijing",
    "重庆": "chongqing",
    "福建": "fujian",
    "甘肃": "gansu",
    "广西": "guangxi",
    "贵州": "guizhou",
    "海南": "hainan",
    "河北": "hebei",
    "黑龙江": "heilongjiang",
    "河南": "henan",
    "湖北": "hubei",
    "湖南": "hunan",
    "江苏": "jiangsu",
    "江西": "jiangxi",
    "吉林": "jilin",
    "辽宁": "liaoning",
    "内蒙古": "neimenggu",
    "宁夏": "ningxia",
    "青海": "qinghai",
    "山东": "shandong",
    "上海": "shanghai",
    "山西": "shanxi",
    "四川": "sichuan",
    "台湾": "taiwan",
    "天津": "tianjin",
    "香港": "xianggang",
    "新疆": "xinjiang",
    "西藏": "xizang",
    "云南": "yunnan",
    "浙江": "zhejiang"
}


def test_core_js_libraries():
    for key, value in DEFAULT_JS_LIBRARIES.items():
        assert key in constants.DEFAULT_JS_LIBRARIES, key
        eq_(value, constants.DEFAULT_JS_LIBRARIES[key])


def test_province_names():
    for key, value in CITY_NAME_PINYIN_MAP.items():
        assert key in constants.CITY_NAME_PINYIN_MAP
        eq_(value, constants.CITY_NAME_PINYIN_MAP[key])


def test_map():
    from pyecharts import Map

    value = [1]
    attr = ["渝水区"]
    map = Map("新余地图示例", width=1200, height=600)
    map.add("", attr, value, maptype='新余', is_visualmap=True,
            visual_text_color='#000')
    # To avoid potential pinyin crash, all cities have a province prefix
    assert "jiang1_xi1_xin1_yu2" in map._repr_html_()
