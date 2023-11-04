inFp = open("C:\\sqlite\\mysql\\code\\Code06\\singer1.csv","r")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()