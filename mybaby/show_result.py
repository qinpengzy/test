import pandas as pd
#k线生成
from pyecharts.charts import Kline
from pyecharts import options as opts


class show_all:

    def show_kline(self,data_list):
        Kline_data = []
        Kline_time = []

        for i in data_list:
            Kline_time.append(i[0:1])
            aim = i[2:6]
            for s in aim:
                s = float(s)
            Kline_data.append(aim)

        kline = (
             Kline()
                .add_xaxis(["{}".format(i) for i in Kline_time])
                # 数据项具体为 [open, close, lowest, highest]
                .add_yaxis("kline", Kline_data)
                .set_global_opts(
                yaxis_opts=opts.AxisOpts(is_scale=True),
                xaxis_opts=opts.AxisOpts(is_scale=True),
                title_opts=opts.TitleOpts(title="Kline-基本示例"),
            )
        )
        kline.render()



