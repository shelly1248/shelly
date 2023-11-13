import pandas as pd
data = {'이름': ['유정', '유나', '민영', '은지'],
        '나이': [30, 28, 31, 29],
        '생일': ['1991.5.2', '1993.4.6', '1990.9.12', '1922.7.19']}
# df1 = pd.DataFrame(data)
# print(df1)

df2 = pd.DataFrame(data, index = ['하나', '둘', '셋', '넷'])
# print(df2)

# print(df2.index)
# print(df2.columns)

sr_name = df2['이름']
# print(sr_name)
# print(type(sr_name))

sr_name.name='브브걸'
# print(sr_name)
sr_two = df2.loc['둘']
# print(type(sr_name))
# print(sr_two)

# print(df2.loc['넷']['생일'])
# print(df2.loc['넷', '생일'])
# print(df2.iloc[3][2])
# print(df2.iloc[3, 2])

df2['키'] = [163, 165, 168, 166]
# print(df2)

sr_vision = pd.Series([1.8, 0.9, 1.2], index=['셋', '하나', '넷'])
df2['시력'] = sr_vision
# print(df2)

df2.insert(1, '꽃', ['장비', '백합', '튤립', '데이지'])
# print(df2)

df2.loc['다섯'] = ['재남', '들꽃', 33, '1988.8.8', 177, 1.1]
# print(df2)

df2.loc['여섯'] = {'이름':'보라','꽃':'민들레','키':163,'나이':34}
# print(df2)

new_data = {'이름':['리사', '제니'], '나이':[23, 22]}
new_df = pd.DataFrame(new_data, index=['블핑', '블핑'])
# print(new_df)
df = pd.concat([df2, new_df])
# print(df)

df2 = df2.drop(['키'], axis=1)
df2 = df2.drop(['셋'], axis=0)
# print(df2)

df2 = df2.drop(['꽃', '시력'], axis=1)
# print(df2)
df = df.drop(['블핑', '하나'])
# print(df)