import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

infilename = 'C:\\sqlite\\mysql\\code\\Code11\\singer.xlsx'
outfilename = 'C:\\sqlite\\mysql\\code\\Code11\\singer_over6.xlsx'
# ===========================엑셀 읽기==============================
df_seniro = pd.read_excel(infilename, 'senior', index_col=None) # senior, junior 시트
df_juniro = pd.read_excel(infilename, 'junior', index_col=None)

df_singer = pd.concat( [df_seniro, df_juniro] ) # concat 합치다
df_singer_over6 = df_singer[df_singer['인원'] >= 6]
df_singer_over6 = df_singer_over6.sort_values(by=['인원'], axis=0, ascending=False) # 인원column으로sort ascending올림차순

df_singer_over6 = df_singer_over6.loc[:,['아이디', '이름', '인원', '유튜브 조회수']]

x_data = df_singer_over6['아이디']
y_data = df_singer_over6['인원']
colorAry = [ np.random.choice(['red', 'green', 'blue', 'brown', 'gold', 'lime', 'aqua', 'magenta', 'purple']) for _ in range(len(x_data))]
plt.bar(x_data, y_data, color=colorAry)
plt.show()

writer = pd.ExcelWriter(outfilename)
df_singer_over6.to_excel(writer, sheet_name='singer', index=False)
writer.close()
print('save')
