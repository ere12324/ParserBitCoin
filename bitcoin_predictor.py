import csv
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bits = pd.read_csv('bitcoin.csv', index_col = 'date', parse_dates = True)

print(bits.head())


# зададим размер графика
plt.figure(figsize = (15,8))
 
# поочередно зададим кривые (перевозки и скользящее среднее) с подписями и цветом
plt.plot(bits, label = 'Курс', color = 'steelblue')
plt.plot(bits.rolling(window = 4).mean(), label = 'Скользящее среднее за минуту', color = 'orange')
 
# добавим легенду, ее положение на графике и размер шрифта
plt.legend(title = '', loc = 'upper left', fontsize = 14)
 
# добавим подписи к осям и заголовки
plt.xlabel('Время', fontsize = 14)
plt.ylabel('Биткоин', fontsize = 14)
plt.title('Динамика', fontsize = 16)
 
# выведем обе кривые на одном графике
plt.show()
