from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key="PXYKaL48a02rqg9oY8vyEkVGeL8FBTRVF9aJkngK7jeKNlce225WOjYyGDKvl7bt", secret_key="38DGxNBjErbLLOvRelADvecaE4GWr4MRyGE5Pkxu6JKGTXvoMprqDdvpUB6gBmmE")
result = request_client.get_balance()

deposit = 100
symbol = "BTCUSDT"
liqpricerefresh = 300;

AvariableBalance = 0

for key in result:
    if key.asset == "BNB":
        AvariableBalance = key.balance

get_candlestick_data = request_client.get_candlestick_data(symbol=symbol, interval=CandlestickInterval.HOUR4,
												startTime=None, endTime=None, limit=2)

for key in get_candlestick_data:
    open = key.open
    close = key.close
    lenth = float(key.high) - float(key.low)
    trend = "UP" if float(close) > float(open) else "DOWN"
    print(""+open+" "+close+" "+str(trend)+" "+str(lenth)+"")

get_position = request_client.get_position()
for key in get_position:
    if key.symbol == symbol:
         if float(key.unrealizedProfit) < 0 and float(key.positionAmt) > 0:
             if float(key.liquidationPrice) / float(key.markPrice) > 0.7:
                 post_order = request_client.post_order(symbol=symbol, side=OrderSide.BUY,
                                                    ordertype=OrderType.STOP_MARKET, stopPrice=float(key.markPrice),
                                                    closePosition=True, positionSide="LONG")


