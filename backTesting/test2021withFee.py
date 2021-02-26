import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df = df['2021']
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

"""
numpy 모듈의 where() 함수를 사용해서 고가와 목표가를 비교
고가가 목표가보다 큰 경우 매수 조건에 해당
매수가 된 경우 해당 거래일의 매도가는 당일 종가, 매수가는 목표가
-> 수익률 =  df[‘close’]/df[‘target’]
매수 조건을 만족하지 않은 경우 매매가 이뤄지지 않으므로 수익률은 1
"""
fee = 0.0032
# 누적 수익률
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

ror = df['ror'].cumprod()[-2]
print(ror)

df.to_excel("trade2021WithFee.xlsx")
