import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

infilename = r'C:\\sqlite\\mysql\\code\\Code11\\1023_file\\covid.csv'
# ===========================엑셀 읽기==============================
df = pd.read_csv(infilename, encoding='cp949') # senior, junior 시트

df_singer_youtube = df.sort_values(by=['증가'], axis=0, ascending=False)
df_singer_youtube = df.loc[:, ['항목', '사례수', '증가', '감소', '변화없음']]

x_data = df_singer_youtube['항목']
y_data = df_singer_youtube['증가']
sizeAry = np.sqrt(df_singer_youtube['증가'])
colorAry = [ np.random.choice(['red', 'green', 'blue', 'brown', 'gold', 'lime', 'aqua', 'magenta', 'purple']) for _ in range(len(x_data))]


plt.bar(x_data, y_data, color=colorAry)
plt.show()