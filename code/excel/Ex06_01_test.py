import glob
import os

input_path = r'C:\\sqlite\\mysql\\code\\excel\\'
output_file = r'C:\\sqlite\\mysql\\code\\excel\\excel_merge.csv'

file_list = glob.glob(input_path + '*.csv')

with open(output_file,'w') as f:
    for i, file in enumerate(file_list):
        if i == 0:
            with open(file,'r') as f2:
                while True:
                    line = f2.readline()
                    if not line:
                        break
                    f.write(line)
                print(file.split('\\')[-1])
        else:
            with open(file,'r') as f2:
                n = 0
                while True:
                    line = f2.readline()
                    if n != 0:
                        f.write(line)
                    if not line:
                        break
                    n += 1
            print(file.split('\\'[-1]))
file_num = len(next(os.walk('C:\\sqlite\\mysql\\code\\excel\\'))[2])
print(file_num, '파일')
