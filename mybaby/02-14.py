import pandas as pd
import matplotlib.pyplot as plt
from get_baostock import Fbao
from show_result import show_all

stock_id = 'sh.601155'
start_date = '2019-01-01'
end_date = '2020-02-13'
data_list = []
Kline_data = []
Kline_time = []

bao = Fbao()
shows = show_all()
data_list = bao.st_info(stock_id,start_date,end_date,adjustflag = 2)
shows.show_kline(data_list)
