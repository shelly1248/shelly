import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

infilename = 'C:\\sqlite\\mysql\\code\\Code11\\singer.xlsx'
outfilename = 'C:\\sqlite\\mysql\\code\\Code11\\singer_over6_2.xlsx'
# ===========================엑셀 읽기==============================
df_seniro = pd.read_excel(infilename, 'senior', index_col=None)
df_junior = pd.read_excel(infilename, 'junior', index_col=None)

df_singer = pd.concat( [df_seniro, df_junior] )
df_singer_youtube = df_singer.sort_values(by=['유튜브 조회수'], axis=0, ascending=False)
df_singer_youtube = df_singer_youtube.loc[:, ['아이디', '이름', '인원', '유튜브 조회수']]

x_data = df_singer_youtube['아이디']
y_data = df_singer_youtube['유튜브 조회수']
sizeAry = np.sqrt(df_singer_youtube['유튜브 조회수'])
colorAry = np.random.rand(len(x_data))
plt.scatter(x_data, y_data, s=sizeAry, c=colorAry, alpha = 0.5, cmap='Spectral')
plt.show()

writer = pd.ExcelWriter(outfilename)
df_singer_youtube.to_excel(writer, sheet_name='singer', index=False)
writer.save()
print('Save. OK~')