#baostock的调用

import baostock as bs
import pandas as pd

class Fbao:

    def __init__(self):
        # 初始化
        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

    # 获取单只股票的一天到另一天的信息
    def st_info(self,stock_id,start_date,end_date,frequency="d",adjustflag=3):
        #adjustflag:默认不复权：3；1：后复权；2：前复权
        #frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据
        self.stock_id = stock_id
        self.start_date = start_date
        self.end_date = end_date

        rs = bs.query_history_k_data_plus(self.stock_id,
                                          "date,code,open,close,low,high,volume,amount,pctChg",
                                          start_date=self.start_date, end_date=self.end_date, frequency="d")
        # 省去了preclose
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())

        return data_list

    def __del__(self):
        lg = bs.logout()



    # 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
    # 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
    # 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
    # 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
    # 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
    # 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
    # 成长指数，例如：sz.399376 小盘成长 等；
    # 价值指数，例如：sh.000029 180价值 等；
    # 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；

    # 详细指标参数，参见“历史行情指标参数”章节
