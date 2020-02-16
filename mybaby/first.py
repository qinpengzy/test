import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
import get_baostock

stock_id = 'sh.601155'
start_date = '2020-01-01'
end_date = '2020-02-13'

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

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
rs = bs.query_history_k_data_plus(stock_id,
    "date,code,open,high,low,close,volume,amount,pctChg",
    start_date=start_date, end_date=end_date, frequency="d")
    #省去了preclose
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
Kline_data = []
Kline_time = []
for i in data_list:
    aim = []
    Kline_time.append(i[0:1])
    aim = i[2:6]
    aim.append(aim.pop(1))
    aim.append(aim.pop(1))
    for s in aim:
        s = float(s)
    Kline_data.append(aim)
result = pd.DataFrame(data_list, columns=rs.fields)

# 结果集输出到csv文件
result.to_csv("/Users/qinpengzy/Documents/编程/baby/adjust_factor_data.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()

#k线生成
from pyecharts.charts import Kline
from pyecharts import options as opts

kline=(
     Kline()
        .add_xaxis(["{}".format(i) for i in Kline_time])
        #数据项具体为 [open, close, lowest, highest]
        .add_yaxis("kline", Kline_data)
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(is_scale=True),
            xaxis_opts=opts.AxisOpts(is_scale=True),
            title_opts=opts.TitleOpts(title="Kline-基本示例"),
        )
     )
kline.render()

