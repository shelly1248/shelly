f=open('C:\\sqlite\\mysql\\code\\pandas\\friends101.txt','r')
output=open('C:\\sqlite\\mysql\\code\\pandas\\friends1012.txt','w')

for line in f:
    if 'Monica:' in line:
        output.write(line)
output.close()