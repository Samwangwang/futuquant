from futuquant.examples.app.stock_alarm.data_acquisition import quote_test
from futuquant.examples.app.stock_alarm.config import config

config.appid = 'wx7a25fbe5fc90799a'
config.secrect = 'f34624551ea8f5f784f2622378fe91f8'
config.test_user_nickname = 'zhangsan'    # 自己的微信昵称
config.template_id = 'jr67sFJ5w4ln_ty6e0BHSBLZNOUOgMXOC-ph9u6xWwQ'

config.premium_rate = 0.005           # parameter: 越价率
config.warning_threshold = 1000000    # 成交额报警阈值，即成交额超过多少报警。当越价率超过阈值后才会判断次阈值
config.large_threshold = 5000000      # 大单报警阈值，即成交额超过多少就一定报警。此报警与上面越价率无关。
config.warning_limit = 5    # 1分钟内最多发出几次报警

config.host = '127.0.0.1'   # FutuOpenD的ip
config.port = 11111         # FutuOpenD的端口号

stock_list = ['HK.02318', 'HK.02828']  # 监控的股票列表
quote_test(stock_list, config.host, config.port)   # 开始监控